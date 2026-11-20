import os
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    matthews_corrcoef,
    log_loss,
    brier_score_loss,
    confusion_matrix,
    roc_curve,
    precision_recall_curve,
    classification_report
)
from sklearn.calibration import calibration_curve

def compute_all_metrics(y_true, y_pred, y_prob):
    """
    Computes all standard classification metrics:
    accuracy, balanced accuracy, precision, recall, f1 (per class, macro, weighted),
    roc-auc, pr-auc, mcc, log loss, brier score.
    """
    metrics = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "precision_class_0": float(precision_score(y_true, y_pred, pos_label=0, zero_division=0)),
        "precision_class_1": float(precision_score(y_true, y_pred, pos_label=1, zero_division=0)),
        "precision_macro": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "precision_weighted": float(precision_score(y_true, y_pred, average="weighted", zero_division=0)),
        "recall_class_0": float(recall_score(y_true, y_pred, pos_label=0, zero_division=0)),
        "recall_class_1": float(recall_score(y_true, y_pred, pos_label=1, zero_division=0)),
        "recall_macro": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_weighted": float(recall_score(y_true, y_pred, average="weighted", zero_division=0)),
        "f1_class_0": float(f1_score(y_true, y_pred, pos_label=0, zero_division=0)),
        "f1_class_1": float(f1_score(y_true, y_pred, pos_label=1, zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_weighted": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, y_prob)),
        "pr_auc": float(average_precision_score(y_true, y_prob)),
        "mcc": float(matthews_corrcoef(y_true, y_pred)),
        "log_loss": float(log_loss(y_true, y_prob)),
        "brier_score": float(brier_score_loss(y_true, y_prob)),
    }
    return metrics

def plot_confusion_matrix(y_true, y_pred, out_png, out_csv):
    cm = confusion_matrix(y_true, y_pred)
    cm_df = pd.DataFrame(cm, index=["Actual Died (0)", "Actual Survived (1)"], columns=["Pred Died (0)", "Pred Survived (1)"])
    cm_df.to_csv(out_csv)

    plt.figure(figsize=(6, 5), dpi=150)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=["Died (0)", "Survived (1)"],
                yticklabels=["Died (0)", "Survived (1)"])
    plt.title("Confusion Matrix (Held-out Test Set)")
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def plot_roc_curve(y_true, y_prob, out_png, auc_score=None):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    if auc_score is None:
        auc_score = roc_auc_score(y_true, y_prob)
    plt.figure(figsize=(6, 5), dpi=150)
    plt.plot(fpr, tpr, color="#1f77b4", lw=2, label=f"ROC curve (AUC = {auc_score:.4f})")
    plt.plot([0, 1], [0, 1], color="gray", lw=1, linestyle="--", label="Random Chance")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate (1 - Specificity)")
    plt.ylabel("True Positive Rate (Recall / Sensitivity)")
    plt.title("Receiver Operating Characteristic (ROC)")
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def plot_pr_curve(y_true, y_prob, out_png, pr_auc_score=None):
    precision, recall, _ = precision_recall_curve(y_true, y_prob)
    if pr_auc_score is None:
        pr_auc_score = average_precision_score(y_true, y_prob)
    baseline = np.mean(y_true)
    plt.figure(figsize=(6, 5), dpi=150)
    plt.plot(recall, precision, color="#2ca02c", lw=2, label=f"PR curve (AP = {pr_auc_score:.4f})")
    plt.axhline(y=baseline, color="gray", lw=1, linestyle="--", label=f"Baseline Prevalence ({baseline:.2f})")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall (PR) Curve")
    plt.legend(loc="lower left")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def plot_calibration_curve(y_true, y_prob, out_png):
    prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=10, strategy="uniform")
    plt.figure(figsize=(6, 5), dpi=150)
    plt.plot(prob_pred, prob_true, marker="o", color="#d62728", lw=2, label="Model Calibration")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Perfect Calibration")
    plt.xlabel("Mean Predicted Probability")
    plt.ylabel("Fraction of Positives (True Frequency)")
    plt.title("Calibration Curve (Reliability Diagram)")
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def plot_probability_histogram(y_prob, y_true, out_png):
    plt.figure(figsize=(7, 5), dpi=150)
    plt.hist(y_prob[y_true == 0], bins=20, alpha=0.6, label="Actual Died (0)", color="#d62728", density=True)
    plt.hist(y_prob[y_true == 1], bins=20, alpha=0.6, label="Actual Survived (1)", color="#2ca02c", density=True)
    plt.axvline(x=0.5, color="black", linestyle="--", lw=1.5, label="Decision Threshold (0.5)")
    plt.xlabel("Predicted Survival Probability P(Survived=1)")
    plt.ylabel("Density")
    plt.title("Predicted Probability Distribution by Actual Outcome")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()
