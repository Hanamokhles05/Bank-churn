# Bank-churn
# 🏦 Customer Intelligence: Churn, Value & Segmentation

An end-to-end Machine Learning project developed as a Capstone for the Machine Learning Track. This project addresses real-world banking business challenges by predicting customer churn, estimating continuous financial targets (Balance), and discovering natural customer segments for targeted retention strategies.

---

## 📌 Project Overview

A retail bank aims to reduce customer churn and maximize long-term customer value. Using a dataset of **165,034 records and 13 features** (Kaggle Playground Series S4E1), this project implements the full classical machine learning pipeline—from rigorous data preprocessing and exploratory data analysis (EDA) to regression, classification, unsupervised clustering, and an interactive web demo.

---

## 🛠️ Project Structure & Key Phases

### **1. Data Preprocessing & Exploratory Data Analysis (EDA)**
* Verified dataset integrity (0 missing values, no duplicate rows)[cite: 5, 6].
* Removed non-predictive identifiers (`id`, `CustomerId`, `Surname`)[cite: 5, 6].
* Applied **One-Hot Encoding** for categorical features (`Geography`, `Gender`) and **StandardScaler** for numerical attributes.
* Created a full EDA suite with **8 visualizations** exploring churn distributions, age dynamics, geographic patterns, and feature correlations[cite: 1].

### **2. Phase 2: Regression (Predicting Customer Value)**
* **Target Variable:** `Balance` (continuous financial metric)[cite: 1].
* **Models Evaluated:** Baseline Linear Regression, Polynomial Regression (Degree 2), Ridge Regularization, and Lasso Regularization[cite: 1].
* **Evaluation Metrics:** RMSE, MAE, and $R^2$ Score[cite: 1].

### **3. Phase 3: Classification (Churn Prediction)**
* **Target Variable:** Binary churn status `Exited`[cite: 1].
* **Imbalance Handling:** Addressed class imbalance using balanced class weighting (`class_weight='balanced'`)[cite: 1].
* **Models Evaluated:** Logistic Regression, Decision Trees, K-Nearest Neighbors (KNN), Naive Bayes, Random Forest, and Gradient Boosting[cite: 1].
* **Best Performer:** Gradient Boosting / Ensemble models evaluated via Precision, Recall, F1-Score, and Confusion Matrix analysis[cite: 1].

### **4. Phase 4: Unsupervised Learning (Customer Segmentation)**
* Applied **KMeans Clustering** using the **Elbow Method** to identify optimal customer segments ($K=3$)[cite: 1].
* Evaluated against **DBSCAN** for density-based grouping comparison[cite: 1].
* **Key Customer Profiles Identified:**
  1. *High-Value at Risk:* Older customers with high balances showing elevated churn rates[cite: 1].
  2. *Loyal Active Savers:* Highly engaged active members with low churn probability.
  3. *Low-Engagement Starters:* Younger customers with fewer products and lower balances.



---

