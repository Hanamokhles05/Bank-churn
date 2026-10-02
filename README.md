#  Customer Intelligence: Churn, Value & Segmentation

A complete Machine Learning pipeline built to tackle practical issues faced by banks. This capstone utilizes both predictive modeling and unsupervised learning to predict financial customer value, churn risk, and create meaningful customer segments.

---

##  Project Overview

Retail banks face constant challenges to retain their customers and maximize Customer Lifetime Value (CLV). Applying **a dataset consisting of 165,034 client entries with 13 features** (based on Kaggle Playground Series S4E1 dataset), the capstone project covers an entire data science process from data cleansing and feature engineering to regression, classification, clustering, and interactive web deployment.

---

##  End-to-End Pipeline Architecture
Raw Data (165K Records)

│

▼

 Data Cleansing & Preprocessing (Encoding & Scaling)

│

├──►  Phase 1: Exploratory Data Analysis (EDA)

├──►  Phase 2: Regression (Balance Estimation)

├──►  Phase 3: Classification (Churn Prediction)

└──►  Phase 4: Clustering (K-Means & DBSCAN Segmentation)

│

▼

 Phase 5: Streamlit Web App Deployment 

 ##  Project Phases & Implementation Details

### **1. Data Preprocessing & EDA**
* **Integrity Check:** No missing data and no duplicated rows.
* **Feature Selection:** Non-predictive identifiers `id`, `CustomerId`, and `Surname` were dropped.
* **Feature Transformation:** Used `OneHotEncoder` to encode categorical variables (Geography, Gender) and `StandardScaler` for numerical parameters.
* **EDA:** Created 8 exploratory graphs analyzing distributions of churns, ages, geography, and feature correlations.

### **2. Phase 2: Regression (Customer Balance Estimation)**
* **Target Variable:** `Balance` (continuous variable).
* **Models Developed:** Baseline Linear Regression, Polynomial Regression (Degree 2), Ridge Regression, and Lasso Regression.
* **Metrics of Evaluation:** RMSE, MAE, and $R^2$ Score.

### **3. Phase 3: Classification (Churn Risk Prediction)**
* **Target Variable:** `Exited` (churn indicator).
* **Imbalance Handling:** Used balanced class weight for classification model (class_weight='balanced').
* **Benchmarked Models:**
  * Logistic Regression
  * Decision Trees
  * K-Nearest Neighbors (KNN)
  * Naïve Bayes
  * Random Forest
  * Gradient Boosting
* **Evaluation:** Focus on Precision, Recall, F1-Score, ROC-AUC, and confusion matrix.

### **4. Phase 4: Unsupervised Learning (Customer Segmentation)**
* **Clustering Techniques:** Used **K-Means Clustering** with the **Elbow Method** to determine optimal clusters number ($K=3$), and compared results with **DBSCAN**.
* **Customer Clusters Identified:**
  1.  **High-Value at Risk:** Clients who are older, have high balances, and have a high probability of churn.
  2.  **Loyal Active Savers:** Highly engaged and active credit card users with a low probability of churn.
  3.  **Low-Engagement Starters:** Younger population who use few products and have low balances.

### **5. Phase 5: Interactive Web Application and Business Intelligence**
* **Interactive UI:** Created an interactive web application using **Streamlit**, which allows retention teams from banks to input customer metrics and get instant churn predictions and risk scores.
* **Retain Strategies:** Developed strategies for retention that are specific to the cluster.



---




