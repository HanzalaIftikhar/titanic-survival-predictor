# Titanic Survival Predictor 🚢

A machine learning web app that predicts whether a Titanic passenger would survive or not.

## Live Demo
Run locally with: `streamlit run app.py`

## Project Overview
This is an end-to-end ML project covering the complete data science pipeline:
- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Feature Engineering
- Training & comparing 4 ML models
- Deploying a live web app with Streamlit

## Models Trained
| Model | Accuracy |
|---|---|
| Random Forest | 82.1% |
| Logistic Regression | 81.0% |
| Decision Tree | 78.0% |
| SVM | 65.9% |

**Winner: Random Forest**

## Tech Stack
- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Joblib

## How to Run
1. Clone the repo
git clone https://github.com/HanzalaIftikhar/titanic-survival-predictor.git
2. Install dependencies
pip install streamlit scikit-learn pandas numpy joblib
3. Run the app
streamlit run app.py

## Dataset
Titanic Dataset from Kaggle — 891 rows, 12 columns

## Key Learnings
- Label Encoding for categorical variables
- Median imputation for null values
- Feature Engineering (FamilySize from SibSp + Parch)
- Model comparison and selection
- Model persistence with joblib
- Web app deployment with Streamlit

## Author
Hanzala Iftikhar — [LinkedIn](https://linkedin.com/in/hanzala-iftikhar-783149213/)
