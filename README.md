# Titanic Survival Predictor (TabPFN + Django, Bilingual FR/EN)

An end-to-end machine learning web application that predicts individual Titanic survival probability using **PriorLabs TabPFN v2** (Prior-Data Fitted Network for Tabular Data) conditioned on the complete historical dataset of **2,208 passengers and crew members**. Built with Django and styled with a modular, responsive CSS variable architecture.

---

## 1. Project Overview & Architecture

### TabPFN & In-Context Learning
Unlike classical parametric classifiers (e.g., Logistic Regression) or decision tree ensembles (e.g., Random Forest, XGBoost, LightGBM) that optimize weights through gradient descent or greedy heuristic splits, **TabPFN** is an attention-based Transformer foundation model pre-trained on millions of synthetic tabular datasets with Bayesian priors.
- `fit(X, y)` does **not** update weights. Instead, it ingests the 1,766 historical records into the model's in-context memory.
- Inference computes the Bayesian posterior predictive probability across test instances in a single forward pass.
- TabPFN natively accommodates missing values without synthetic imputation.

### Bilingual (EN / FR) & Historical Immersion
- **Session-Persisted Language Toggle**: Users can switch between English and French at any time.
- **Historical Outcome Sentences**: Custom hard-coded sentences for normal passengers across 4 probability tiers, dedicated crew recognition sentences, and an interactive **Musician Easter Egg** tribute to Wallace Hartley's band with CSS night-sky and tilting-ship animations.
- **Historical Passenger Matching ("You might be this person")**: Real-time fuzzy name matching and multi-attribute record matching against the historical passenger manifest.

---

## 2. Directory Structure

```
minprojai/
├── titanicall.csv              # Full dataset (2,208 records: passengers & crew)
├── inspect_data.py             # Data profiling script
├── README.md                   # Top-level setup and operation guide
│
├── ml/                         # Phase 1: Machine Learning Pipeline
│   ├── train.py                # Fitting, 5-fold CV, baseline benchmarks & report generation
│   ├── evaluate.py             # Metrics calculation and plotting utilities
│   ├── requirements.txt        # Pinned ML dependencies
│   ├── artifacts/              # Model weights, metadata, serialized context
│   │   ├── tabpfn-v2-classifier.ckpt  # TabPFN v2 weights (28 MB)
│   │   ├── fitted_tabpfn_model.tabpfn_fit
│   │   ├── training_context.joblib    # Training data & conditioning metadata
│   │   └── feature_list.json          # 13 model features & category schema
│   ├── reports/                # Evaluation outputs
│   │   ├── data_profile.md     # Initial dataset profiling & split audit
│   │   ├── REPORT.md           # Comprehensive evaluation report with embedded figures
│   │   ├── metrics.json        # Test set metrics
│   │   ├── classification_report.txt
│   │   ├── baseline_comparison.csv & .png
│   │   ├── permutation_importance.csv & .png (overall, passengers, crew)
│   │   ├── ablation_comparison.csv & .png
│   │   ├── confusion_matrix.csv & .png
│   │   ├── roc_curve.png, pr_curve.png, calibration_curve.png, probability_histogram.png
│   └── README.md
│
└── website/                    # Phase 2: Django Web Application
    ├── manage.py
    ├── config/                 # Project configuration (settings, urls)
    └── predictor/              # Predictor app
        ├── ml_service.py       # Singleton TabPFN service (preloaded at startup)
        ├── matching.py         # "You might be this person" historical matcher
        ├── messages_i18n.py    # English & French translations & historical texts
        ├── forms.py            # Form validation (4 required + 9 optional fields)
        ├── views.py            # Predictor, Easter egg, and How-it-works views
        ├── urls.py
        ├── tests.py            # 17 unit and integration tests
        ├── templates/predictor/# base.html, index.html, result.html, easter_egg.html, how_it_works.html
        └── static/             # style.css (CSS variables), main.js
```

---

## 3. Quick Start & Execution

### Prerequisites
- Python 3.10+ (Python 3.11 recommended)
- `uv` (or standard `python3 -m venv`)

### Step 1: Create Virtual Environment & Install Dependencies
```bash
# Clone or navigate to the repository directory
cd /home/azer/Documents/minprojai

# Create virtual environment with Python 3.11 using uv
uv venv --python 3.11 .venv

# Activate virtual environment
source .venv/bin/activate

# Install pinned dependencies
uv pip install -r ml/requirements.txt
```

### Step 2: (Optional) Re-run the Training & Evaluation Pipeline
To train TabPFN from scratch, compute 5-fold cross validation, run all baselines (Logistic Regression, Random Forest, LightGBM, XGBoost), generate all evaluation plots, and produce `ml/reports/REPORT.md`:
```bash
PYTHONPATH=ml python ml/train.py
```

### Step 3: Run the Test Suite
Run the 17 automated tests covering form validation, probability tier selection, crew recognition, musician easter egg, matching logic, and test client scenarios:
```bash
cd website
python manage.py test predictor -v 2
```

### Step 4: Start the Django Development Server
```bash
cd website
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

---

## 4. Key Performance Results

| Model | Accuracy | Balanced Acc | F1 (Macro) | ROC-AUC | PR-AUC | Log Loss | Brier Score |
|---|---|---|---|---|---|---|---|
| **TabPFN (v2)** | **82.13%** | **74.59%** | **0.7685** | **0.8647** | **0.8029** | **0.4100** | **0.1295** |
| Logistic Regression | 84.39% | 77.93% | 0.8022 | 0.8554 | 0.8027 | 0.4103 | 0.1276 |
| Random Forest | 81.67% | 73.33% | 0.7571 | 0.8424 | 0.7876 | 0.4473 | 0.1395 |
| LightGBM | 81.22% | 74.85% | 0.7657 | 0.8381 | 0.7768 | 0.4284 | 0.1371 |
| XGBoost | 82.13% | 74.22% | 0.7659 | 0.8438 | 0.7804 | 0.4287 | 0.1365 |

- **Stratified 5-Fold Cross-Validation (Train set)**:
  - Accuracy: **80.86% ± 2.13%**
  - ROC-AUC: **0.8254 ± 0.0123**
- **Ablation Study**:
  - 4 Required fields only (`Sex`, `Age`, `Pclass`, `Person_Role`): 78.28% Accuracy, 83.57% ROC-AUC.
  - 12 Features without noisy text `Home_Dest`: **83.71% Accuracy**, **85.86% ROC-AUC**, **79.08% F1**.
  - Full 13 Features: 82.13% Accuracy, **86.47% ROC-AUC**.

---

## 5. Summary of Decisions Made on Your Behalf

1. **Model Checkpoint**: TabPFN v3.5 requires browser authentication and token acceptance on PriorLabs/HuggingFace. As instructed, we utilized **TabPFN v2** (`tabpfn-v2-classifier.ckpt`, 28 MB), which is open, un-gated, and fully self-contained.
2. **Hardware Path**: The Linux kernel NVIDIA module was running version 615 while user space was on 580, causing CUDA Error 803 (`system has unsupported display driver / cuda driver combination`). We executed the pipeline in CPU mode with `TABPFN_ALLOW_CPU_LARGE_DATASET=1` and `ignore_pretraining_limits=True`. In-context conditioning completes in **0.10s** and single web request inference executes in **~2-3 seconds**.
3. **Train/Test Split Policy**: The legacy `Split` column in `titanicall.csv` only covered passengers (891 train, 418 test) while marking all 899 crew members as `Split == 'crew'`. Using it would have omitted 100% of the crew. We created a **stratified 80/20 train/test split** with fixed seed (`random_state=42`) stratified across `Survived` and `Person_Role`.
4. **Feature Policy (`Title` vs. `Home_Dest`)**:
   - `Title` (19 compact categories) is retained; it conveys strong social deference and age/marital indicators.
   - `Home_Dest` (372 sparse string categories) was evaluated in the ablation study and shown to introduce slight categorical noise. It is supported as an optional field in the UI.
   - `Occupation` was curated from the 100% complete CSV occupation column, including "Musician".
5. **Fast Startup Architecture**: Rather than re-contacting remote servers at startup, `ml_service.py` refits the in-context memory in <0.2s directly from the local serialized training context and cached checkpoint.
6. **CSS Design**: Designed with standard CSS custom properties (`:root` variables) in `static/css/style.css` for effortless one-click theme restyling.

---

## 6. Known Limitations

- **Historical Scope**: The model predicts probability of survival during a sudden maritime catastrophe in 1912 under strict Edwardian maritime protocols.
- **No Outcome Leakage**: Features such as lifeboat assignment (`Boat`), recovered body identifier (`Body`), or cabin numbers are strictly prohibited from model training.
- **CPU Execution**: Predictions take approximately 2–3 seconds on CPU due to the 1,766-row in-context transformer attention. If the machine is rebooted to synchronize the NVIDIA driver and kernel module, TabPFN can run on CUDA to deliver sub-50ms inference.
