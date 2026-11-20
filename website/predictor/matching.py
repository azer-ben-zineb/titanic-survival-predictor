import os
import unicodedata
import pandas as pd
import numpy as np
from typing import Dict, Any, Optional, Tuple
from .messages_i18n import format_match_message

# Load the historical dataset into memory once
CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "titanicall.csv"))
_HISTORICAL_DF = None

def get_historical_df() -> pd.DataFrame:
    global _HISTORICAL_DF
    if _HISTORICAL_DF is None:
        if os.path.exists(CSV_PATH):
            df = pd.read_csv(CSV_PATH)
        else:
            # Fallback path if running from root
            df = pd.read_csv("titanicall.csv")
        # Ensure string columns are stripped
        for c in ['Name', 'Sex', 'Pclass', 'Person_Role', 'Embarked', 'Home_Dest', 'Boat', 'Body']:
            if c in df.columns:
                df[c] = df[c].astype(str).str.strip()
        # Sort deterministically by PassengerId
        df = df.sort_values('PassengerId').reset_index(drop=True)
        _HISTORICAL_DF = df
    return _HISTORICAL_DF

def normalize_text(text: str) -> str:
    """Normalize text: lowercase, remove accents, strip punctuation/spaces."""
    if not text:
        return ""
    nfkd = unicodedata.normalize('NFKD', str(text))
    ascii_text = nfkd.encode('ASCII', 'ignore').decode('utf-8')
    return "".join(c.lower() for c in ascii_text if c.isalnum() or c.isspace()).strip()

def match_passenger(user_input: Dict[str, Any], lang: str = "en") -> Optional[Dict[str, Any]]:
    """
    Finds historical passenger matches based on Name or Key biographical features.
    Returns None if no match is found, or a dict containing formatted message and details.
    """
    df = get_historical_df()
    
    # 1. Fuzzy / Substring match on Name if provided
    raw_name = user_input.get("name")
    if raw_name and str(raw_name).strip():
        norm_query = normalize_text(raw_name)
        if len(norm_query) >= 3:
            # Check normalized names in dataset
            matches = []
            for idx, row in df.iterrows():
                row_norm_name = normalize_text(row['Name'])
                # Direct substring match or token match
                if norm_query in row_norm_name or all(token in row_norm_name for token in norm_query.split()):
                    matches.append(row)
            
            if matches:
                top_match = matches[0]
                additional = len(matches) - 1
                return _build_match_result(top_match, additional, lang)

    # 2. Key fields matching:
    # Requires: Sex + Age + Pclass + at least ONE of (SibSp, Parch, Fare)
    user_sex = user_input.get("Sex")
    user_age = user_input.get("Age")
    user_pclass = user_input.get("Pclass")
    user_sibsp = user_input.get("SibSp")
    user_parch = user_input.get("Parch")
    user_fare = user_input.get("Fare")
    user_embarked = user_input.get("Embarked")

    if not (user_sex and user_age is not None and user_pclass):
        return None

    has_third_key = (user_sibsp is not None) or (user_parch is not None) or (user_fare is not None)
    if not has_third_key:
        return None

    # Filter candidates
    candidates = df.copy()
    
    # Sex match
    candidates = candidates[candidates['Sex'].str.lower() == str(user_sex).lower()]
    
    # Age match (exact or within +/- 0.5)
    try:
        age_val = float(user_age)
        candidates = candidates[(candidates['Age'] >= (age_val - 0.5)) & (candidates['Age'] <= (age_val + 0.5))]
    except (ValueError, TypeError):
        return None

    # Pclass match (normalize both)
    pclass_str = str(user_pclass).strip()
    candidates = candidates[candidates['Pclass'].str.lower() == pclass_str.lower()]

    # SibSp
    if user_sibsp is not None and str(user_sibsp).strip() != "":
        try:
            s_val = int(user_sibsp)
            candidates = candidates[candidates['SibSp'] == s_val]
        except (ValueError, TypeError):
            pass

    # Parch
    if user_parch is not None and str(user_parch).strip() != "":
        try:
            p_val = int(user_parch)
            candidates = candidates[candidates['Parch'] == p_val]
        except (ValueError, TypeError):
            pass

    # Fare (within +/- 0.01)
    if user_fare is not None and str(user_fare).strip() != "":
        try:
            f_val = float(user_fare)
            candidates = candidates[(candidates['Fare'] >= (f_val - 0.01)) & (candidates['Fare'] <= (f_val + 0.01))]
        except (ValueError, TypeError):
            pass

    # Embarked
    if user_embarked and str(user_embarked).strip() != "":
        candidates = candidates[candidates['Embarked'].str.upper() == str(user_embarked).upper()]

    if len(candidates) == 0:
        return None

    top_match = candidates.iloc[0]
    additional = len(candidates) - 1
    return _build_match_result(top_match, additional, lang)

def _build_match_result(row: pd.Series, additional_matches: int, lang: str = "en") -> Dict[str, Any]:
    name = str(row['Name'])
    role = str(row['Person_Role'])
    age = str(int(round(float(row['Age'])))) if float(row['Age']).is_integer() else f"{float(row['Age']):.1f}"
    pclass = str(row['Pclass'])
    home_dest = str(row['Home_Dest'])
    survived = bool(int(row['Survived']) == 1)
    
    boat = str(row.get('Boat', ''))
    body = str(row.get('Body', ''))
    
    message = format_match_message(
        name=name,
        role=role,
        age=age,
        pclass=pclass,
        home_dest=home_dest,
        survived=survived,
        additional_matches=additional_matches,
        lang=lang
    )
    
    return {
        "name": name,
        "role": role,
        "age": age,
        "pclass": pclass,
        "home_dest": home_dest,
        "survived": survived,
        "boat": boat if boat and boat != "No Boat" else None,
        "body": body if body and body != "No Body Recovered" else None,
        "additional_matches": additional_matches,
        "message": message
    }
