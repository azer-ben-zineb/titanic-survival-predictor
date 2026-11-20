# TabPFN Titanic Survival Predictor — Machine Learning Pipeline

## 1. Overview
This directory contains the training, evaluation, and serialization pipeline for the Titanic Survival Predictor using **TabPFN v2** (Prior-Data Fitted Network for Tabular Data).

### In-Context Learning vs. Gradient Training
Unlike classical machine learning models (Random Forest, XGBoost) or neural networks trained via backpropagation/gradient descent, TabPFN does **not** update weights during `fit()`. 
TabPFN is a pre-trained meta-learning transformer trained on millions of synthetic tabular datasets. Calling `fit(X, y)` simply ingests the dataset as conditioning tokens (in-context context). When `predict_proba(X_test)` is called, the model executes Bayesian inference over the test instances given the training context in a single forward pass.

## 2. Hardware Path
- Hardware environment: Linux, NVIDIA RTX 3060 (6 GB VRAM).
- Current system note: A mismatch between the running Linux kernel NVIDIA module (615.x) and user-space library (580.x) caused `cudaGetDeviceCount()` Error 803. As specified by project protocol, the pipeline automatically operates in CPU mode with `TABPFN_ALLOW_CPU_LARGE_DATASET=1` and `ignore_pretraining_limits=True`.
- Model checkpoint: PriorLabs TabPFN v2 (`tabpfn-v2-classifier.ckpt`, 28 MB), cached locally in `ml/artifacts/`.

## 3. Directory Layout
```
ml/
  train.py            # Complete fit, 5-fold CV, baseline comparison, permutation importance, ablation, and report generation
  evaluate.py         # Evaluation metrics and plotting routines
  requirements.txt    # Pinned Python package dependencies
  artifacts/          # Serialized fitted model, feature lists, and training context
  reports/            # Evaluation figures (PNG), data profile, baseline comparison, and REPORT.md
  README.md           # This document
```

## 4. Feature Policy
- **Excluded columns (leakage / identifiers / redundant)**:
  `Boat, Body, Date_Death, URL, Cabin, Ticket, PassengerId, DoB, Name, LastName, FirstName, Female, Male, Normal_Passenger, Engineering_Crew, Other_Crew, Class_Dept, Job, Split`.
- **Required Model Inputs**:
  - `Sex`: `'male'`, `'female'`
  - `Age`: Numeric (0.2 – 80)
  - `Pclass`: `'1'`, `'2'`, `'3'`, `'Deck Crew'`, `'Engineering Crew'`, `'Victualling Crew'`, `'Restaurant Staff'`, `'Band'`
  - `Person_Role`: `'Normal Passenger'`, `'Other Crew'`, `'Engineering Crew'`
- **Optional Model Inputs** (TabPFN handles missing values natively without imputation):
  - `SibSp`, `Parch`, `Fare`, `Embarked`, `Height_cm`, `Weight_kg`, `Title`, `Home_Dest`, `Occupation`

## 5. Execution Instructions
Activate the virtual environment and run the pipeline:
```bash
source .venv/bin/activate
python ml/train.py
```
All evaluation metrics, figures, and markdown reports will be written directly to `ml/reports/`.
