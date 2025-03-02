# Bank Loan Classification

## Overview

This project focuses on classifying bank loan data to predict whether customers will accept a personal loan offer. The notebook includes data preprocessing, exploratory analysis, feature engineering, and machine learning model building to address this classification problem.

---

## Problem Statement

The goal is to predict customer acceptance of personal loan offers using attributes such as income, education, family size, and financial behavior. The challenge lies in handling imbalanced data, preprocessing features, and building an accurate predictive model.

---

## Solution Approach

### 1. Data Preprocessing

- Handled missing values by imputing mode (categorical) and mean (numerical)
- Encoded categorical features (`Gender`, `Home Ownership`, `Personal Loan`)
- Cleaned inconsistent values in categorical columns

### 2. Exploratory Data Analysis (EDA)

- Analyzed distributions of key features:
  - Income vs. Loan Acceptance
  - Education Level vs. Loan Status
  - Family Size impact on Loan Decisions
- Visualized categorical feature distributions using count plots

### 3. Feature Engineering

- Created interaction features (e.g., `Income_CCAvg`)
- Addressed class imbalance using SMOTE oversampling
- Scaled numerical features using StandardScaler

### 4. Model Building & Evaluation

- Implemented and compared multiple classifiers:
  - Random Forest
  - Logistic Regression
  <!-- - SVM -->
  - AdaBoost
- Optimized hyperparameters using GridSearchCV
- Evaluated performance using:
  - Accuracy
  - Precision-Recall metrics
  - Confusion matrices

### 5. Model Deployment

- Saved best-performing model (Random Forest) using joblib

---

## Key Findings

- **Top Predictors**: Income, Education Level, and Credit Card Spending (CCAvg)
- **Class Imbalance**: Only 9.6% of customers accepted loans (original distribution)
- **Best Model**: Random Forest achieved 95% accuracy after hyperparameter tuning
- **Critical Insights**:
  - Higher income customers (>$50K) were 3x more likely to accept loans
  - Customers with CD accounts showed 60% higher acceptance rates
