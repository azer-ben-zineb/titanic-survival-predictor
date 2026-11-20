import os
import sys
import json
import joblib
import pandas as pd
import numpy as np
from typing import Dict, Any

# Ensure TabPFN and Matplotlib environment variables
os.environ["SKB_DATA_DIRECTORY"] = "/tmp/skrub_data"
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
os.environ["TABPFN_ALLOW_CPU_LARGE_DATASET"] = "1"

from tabpfn import TabPFNClassifier, load_fitted_tabpfn_model

# Project root paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FITTED_MODEL_PATH = os.path.join(BASE_DIR, "ml", "artifacts", "fitted_tabpfn_model.tabpfn_fit")
TRAINING_CONTEXT_PATH = os.path.join(BASE_DIR, "ml", "artifacts", "training_context.joblib")
FEATURE_LIST_PATH = os.path.join(BASE_DIR, "ml", "artifacts", "feature_list.json")
MODEL_CKPT_PATH = os.path.join(BASE_DIR, "ml", "artifacts", "tabpfn-v2-classifier.ckpt")

class MLService:
    _instance = None

    def __init__(self):
        self.model = None
        self.feature_meta = None
        self._load_metadata()
        self._load_or_fit_model()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _load_metadata(self):
        if os.path.exists(FEATURE_LIST_PATH):
            with open(FEATURE_LIST_PATH, "r") as f:
                self.feature_meta = json.load(f)
        else:
            self.feature_meta = {
                "required_features": ["Sex", "Age", "Pclass", "Person_Role"],
                "optional_features": [
                    "SibSp", "Parch", "Fare", "Embarked", "Height_cm", "Weight_kg",
                    "Title", "Home_Dest", "Occupation"
                ],
                "all_features": [
                    "Sex", "Age", "Pclass", "Person_Role", "SibSp", "Parch", "Fare",
                    "Embarked", "Height_cm", "Weight_kg", "Title", "Home_Dest", "Occupation"
                ],
                "categorical_features": ["Sex", "Pclass", "Person_Role", "Embarked", "Title", "Home_Dest", "Occupation"],
                "numeric_features": ["Age", "SibSp", "Parch", "Fare", "Height_cm", "Weight_kg"]
            }

    def _load_or_fit_model(self):
        print("[MLService] Loading TabPFN model once at startup...")
        # Refit in-context using local training context and local checkpoint (takes ~0.10s, 100% offline)
        if os.path.exists(TRAINING_CONTEXT_PATH) and os.path.exists(MODEL_CKPT_PATH):
            ctx = joblib.load(TRAINING_CONTEXT_PATH)
            X_tr = ctx["X_train"]
            y_tr = ctx["y_train"]
            self.model = TabPFNClassifier(
                model_path=MODEL_CKPT_PATH,
                device="cpu",
                ignore_pretraining_limits=True,
                n_estimators=4,
                random_state=42
            )
            self.model.fit(X_tr, y_tr)
            print("[MLService] TabPFN initialized and conditioned in-context in <0.2s from local checkpoint.")
        elif os.path.exists(FITTED_MODEL_PATH):
            try:
                self.model = load_fitted_tabpfn_model(FITTED_MODEL_PATH, device="cpu")
                print(f"[MLService] Successfully loaded fitted model from {FITTED_MODEL_PATH}")
            except Exception as e:
                raise RuntimeError(f"Could not load fitted model: {e}")
        else:
            raise FileNotFoundError("Could not find fitted model or training context in ml/artifacts!")

    def predict(self, raw_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Runs TabPFN inference on user input.
        Returns survival_probability, confidence, data_completeness, and predicted_class.
        """
        all_features = self.feature_meta["all_features"]
        cat_features = self.feature_meta["categorical_features"]
        num_features = self.feature_meta["numeric_features"]

        # Calculate data completeness among the 13 model features
        filled_count = 0
        row_dict = {}

        for col in all_features:
            val = raw_input.get(col)
            # Check if filled
            if val is not None and str(val).strip() != "" and str(val).strip().lower() != "none":
                filled_count += 1
                if col in num_features:
                    try:
                        row_dict[col] = float(val)
                    except (ValueError, TypeError):
                        row_dict[col] = np.nan
                else:
                    row_dict[col] = str(val).strip()
            else:
                row_dict[col] = np.nan

        completeness_pct = round((filled_count / float(len(all_features))) * 100.0, 1)

        # Build single-row DataFrame
        df_input = pd.DataFrame([row_dict])
        for col in cat_features:
            df_input[col] = df_input[col].astype('category')
        for col in num_features:
            df_input[col] = pd.to_numeric(df_input[col], errors='coerce')

        # Predict probability
        probs = self.model.predict_proba(df_input)[0]
        prob_died = float(probs[0])
        prob_survived = float(probs[1])

        # Confidence: max(p, 1 - p)
        confidence = float(max(prob_survived, 1.0 - prob_survived))
        predicted_class = 1 if prob_survived >= 0.5 else 0

        # Percentage as integer
        p_percent = int(round(prob_survived * 100.0))

        return {
            "survival_probability": prob_survived,
            "survival_percentage": p_percent,
            "confidence": confidence,
            "confidence_percentage": round(confidence * 100.0, 1),
            "data_completeness": completeness_pct,
            "predicted_class": predicted_class,
            "survived": bool(predicted_class == 1),
            "filled_fields": filled_count,
            "total_fields": len(all_features)
        }
