
# Malaria Prediction Using Hematological Indicators

This project applies machine learning techniques to predict malaria positivity using hematological blood parameters.

## Project Objective

Malaria remains one of the leading infectious diseases worldwide, especially in tropical and subtropical regions. Early diagnosis is essential for timely treatment and reduction of mortality.

This project compares multiple machine learning algorithms to classify malaria positivity using routinely collected hematological indicators.

## Machine Learning Models Used

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

## Best Model

The best-performing model was:

- Gradient Boosting
- Accuracy: ~76%

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Features Used

- Age
- Hemoglobin(Hb%)
- Total WBC count(/cumm)
- Neutrophils
- Lymphocytes
- Total Circulating Eosinophils
- HTC/PCV(%)
- MCH(pg)
- MCHC(g/dl)
- RDW-CV(%)
- Platelet Count
- Sex
## Model Performance

| Model | Accuracy |
|---|---|
| XGBoost | 76.48% |
| Gradient Boosting | 76.26% |
| Random Forest | 73.74% |
| SVM | 73.06% |
| Logistic Regression | 70.09% |
| KNN | 69.86% |
| Decision Tree | 67.35% |

## ROC-AUC Analysis

The Gradient Boosting model achieved:

- ROC-AUC Score: **0.816**

This indicates strong discriminatory ability between malaria positive and negative cases.

## Feature Importance

Feature importance analysis identified hematological indicators strongly associated with malaria positivity, including:

- Platelet Count
- RDW-CV(%)
- Total Circulating Eosinophils
- MCHC(g/dl)
- Neutrophils
- HTC/PCV(%)

## Deployment

The application was deployed using:

- Gradio
- Hugging Face Spaces

## Disclaimer 

This project is for educational and research purposes only and should not replace professional medical diagnosis.
