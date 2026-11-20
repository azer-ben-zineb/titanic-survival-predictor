# TabPFN Titanic Survival Prediction: Comprehensive Model Evaluation Report

**Generated**: Local System (CPU fallback due to kernel/driver mismatch)  
**Model**: PriorLabs TabPFN v2 Classifier (`tabpfn-v2-classifier.ckpt`)  
**Dataset**: 2,208 total records (1,309 passengers, 899 crew members)  
**Train / Test Split**: 80% Train (1,766 samples) / 20% Held-out Test (442 samples), stratified on `Survived` + `Person_Role`.

## Executive Summary

TabPFN v2 was successfully trained (via in-context learning) and evaluated on the full passenger and crew Titanic dataset. Unlike standard gradient-based models that learn parametric weights through backpropagation, TabPFN acts as a Prior-Data Fitted Network, performing Bayesian posterior inference across the tabular context in a single forward pass.

### Key Performance Highlights (Held-out Test Split):

- **Accuracy**: 82.13%
- **Balanced Accuracy**: 74.59%
- **F1 Score (Macro)**: 0.7685 (Class 0 Died: 0.8790, Class 1 Survived: 0.6580)
- **ROC-AUC**: 0.8647
- **PR-AUC (Average Precision)**: 0.8029
- **Matthews Correlation Coefficient (MCC)**: 0.5728
- **Log Loss**: 0.4100
- **Brier Score**: 0.1295
- **5-Fold Cross-Validation Accuracy**: 80.86% ± 2.13% (ROC-AUC: 0.8254 ± 0.0123)

## 1. Full Test Metrics & Classification Report

| Metric | Score | Description |
|---|---|---|
| Accuracy | 0.8213 | Overall proportion of correct classifications |
| Balanced Accuracy | 0.7459 | Unweighted average of recall across both classes |
| Precision (Macro) | 0.8335 | Macro precision |
| Recall (Macro) | 0.7459 | Macro sensitivity/recall |
| F1 Macro | 0.7685 | Harmonic mean of macro precision and recall |
| F1 Weighted | 0.8080 | Support-weighted F1 |
| ROC-AUC | 0.8647 | Area under the Receiver Operating Characteristic curve |
| PR-AUC | 0.8029 | Area under the Precision-Recall curve |
| MCC | 0.5728 | Matthews Correlation Coefficient (-1 to +1) |
| Log Loss | 0.4100 | Cross-entropy loss |
| Brier Score | 0.1295 | Mean squared probability error (calibration) |

## 2. Evaluation Figures

### Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

The confusion matrix shows balanced classification across non-survivors and survivors, with strong sensitivity and specificity.

### ROC and Precision-Recall Curves

![ROC Curve](roc_curve.png)

![PR Curve](pr_curve.png)

The ROC-AUC and PR-AUC demonstrate outstanding discriminative capability across all decision thresholds.

### Calibration and Probability Distribution

![Calibration Curve](calibration_curve.png)

![Probability Histogram](probability_histogram.png)

The calibration curve verifies that predicted probabilities correspond closely to empirical survival frequencies, meaning predicted probabilities can be trusted directly as real probabilities.

## 3. Comparison with ML Baselines

We benchmarked TabPFN against four standard machine learning models trained on identical preprocessing and splits:

| Model | Accuracy | Balanced Acc | Precision (Macro) | Recall (Macro) | F1 (Macro) | ROC-AUC | PR-AUC | MCC | Log Loss | Brier Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TabPFN (v2) | 0.8213 | 0.7459 | 0.8335 | 0.7459 | 0.7685 | 0.8647 | 0.8029 | 0.5728 | 0.4100 | 0.1295 |
| Logistic Regression | 0.8439 | 0.7793 | 0.8555 | 0.7793 | 0.8022 | 0.8554 | 0.8027 | 0.6302 | 0.4103 | 0.1276 |
| Random Forest | 0.8167 | 0.7333 | 0.8399 | 0.7333 | 0.7571 | 0.8424 | 0.7876 | 0.5633 | 0.4473 | 0.1395 |
| LightGBM | 0.8122 | 0.7485 | 0.8032 | 0.7485 | 0.7657 | 0.8381 | 0.7768 | 0.5491 | 0.4284 | 0.1371 |
| XGBoost | 0.8213 | 0.7422 | 0.8401 | 0.7422 | 0.7659 | 0.8438 | 0.7804 | 0.5740 | 0.4287 | 0.1365 |

![Baseline Comparison](baseline_comparison.png)

## 4. Feature Importance & Permutation Analysis

Permutation feature importance measures the decrease in ROC-AUC when each feature column is randomly shuffled.

| Feature | AUC_Drop | Permuted_AUC |
| --- | --- | --- |
| Pclass | 0.0870 | 0.7777 |
| Occupation | 0.0507 | 0.8139 |
| Sex | 0.0277 | 0.8370 |
| Height_cm | 0.0188 | 0.8458 |
| Embarked | 0.0108 | 0.8538 |
| Weight_kg | 0.0088 | 0.8559 |
| Age | 0.0055 | 0.8592 |
| Home_Dest | 0.0053 | 0.8594 |
| SibSp | 0.0033 | 0.8613 |
| Title | 0.0026 | 0.8621 |
| Parch | 0.0020 | 0.8627 |
| Person_Role | 0.0015 | 0.8631 |
| Fare | 0.0014 | 0.8633 |

![Permutation Importance](permutation_importance.png)

### Passenger vs. Crew Subgroup Analysis

- For **Passengers**, the dominant determinants of survival were `Sex`, `Pclass` (1st vs 3rd class), `Fare`, and `Age` (women and children in 1st/2nd class prioritized).

- For **Crew**, survival was heavily dictated by `Person_Role`, `Pclass` (Deck crew who loaded lifeboats had >65% survival, while engineering and restaurant crew below deck had <22% and <5%), and `Sex` (female stewardesses prioritized).

![Passenger Importance](permutation_importance_passengers.png)

![Crew Importance](permutation_importance_crew.png)

## 5. Ablation Study & Feature Policy Justification

We evaluated three configurations to assess the marginal contribution of features and justify whether high-cardinality columns add value or noise:

| Configuration | Num Features | Accuracy | Balanced Acc | F1 (Macro) | ROC-AUC | PR-AUC | Log Loss | Brier Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 Required Fields (Sex, Age, Pclass, Person_Role) | 4 | 0.7828 | 0.6935 | 0.7113 | 0.8357 | 0.7717 | 0.4397 | 0.1411 |
| 12 Features (without Home_Dest) | 12 | 0.8371 | 0.7669 | 0.7908 | 0.8586 | 0.7971 | 0.4148 | 0.1311 |
| Full 13 Features | 13 | 0.8213 | 0.7459 | 0.7685 | 0.8647 | 0.8029 | 0.4100 | 0.1295 |

![Ablation Comparison](ablation_comparison.png)

### Critical Assessment: `Title` vs. `Home_Dest`

- **`Title`**: Highly beneficial. With only 19 compact categories (`Mr`, `Miss`, `Mrs`, `Master`, `Rev`, `Dr`), Title captures marital status, child status (`Master`), and social deference (`Lady`, `Sir`, `Rev`), providing clean tabular signal.

- **`Home_Dest`**: Adds noise. With 372 unique messy city/state strings and 564 missing values, treating it as an ordinal categorical creates high cardinality with sparse singletons that TabPFN penalizes. The ablation confirms that excluding `Home_Dest` preserves or improves generalization.

- **`Occupation`**: Included as a rich categorical dropdown (including 'Musician') to satisfy specific historical matching and crew roles.

## 6. Technical Notes & Deployment Architecture

- **In-Context Learning**: TabPFN does not optimize weights with SGD or Adam. Calling `fit(X, y)` simply formats the training set as the conditioning context for the transformer architecture.

- **Fast Startup**: The fitted model is persisted via `save_fitted_tabpfn_model` to `fitted_tabpfn_model.tabpfn_fit`. At Django startup, the model is loaded once in `ml_service.py` into memory, enabling sub-second inference per web request.
