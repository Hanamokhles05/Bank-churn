import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load('churn_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

st.title("🏦 Bank Customer Churn Prediction App")
st.write("Enter customer details to predict whether they will leave the bank.")

credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 100, 35)
tenure = st.slider("Tenure (Years)", 0, 10, 5)
num_of_products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_cr_card = st.selectbox("Has Credit Card?", [0, 1])
is_active = st.selectbox("Is Active Member?", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

if st.button("Predict Churn"):
    input_data = pd.DataFrame([{
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'NumOfProducts': num_of_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active,
        'EstimatedSalary': estimated_salary
    }])
    
    input_prep = preprocessor.transform(input_data)
    prediction = model.predict(input_prep)
    probability = model.predict_proba(input_prep)[0][1]
    
    if prediction[0] == 1:
        st.error(f" High Churn Risk! (Probability: {probability:.2%})")
    else:
        st.success(f"Low Churn Risk. Customer is likely to stay. (Probability: {probability:.2%})")