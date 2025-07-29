
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and feature list
model = joblib.load("churn_model.pkl")
features = joblib.load("model_features.pkl")

# Page config
st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📉 Customer Churn Prediction App")
st.markdown("This app predicts whether a customer is likely to churn based on their service and demographic details.")

# Define user-friendly form inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Has Partner", ["No", "Yes"])
dependents = st.selectbox("Has Dependents", ["No", "Yes"])
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
online_backup = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])
device_protection = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
tech_support = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
streaming_tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
streaming_movies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=29.85)
total_charges = st.number_input("Total Charges", min_value=0.0, value=29.85)

# Build raw input dictionary
raw_input = {
    "gender": gender,
    "SeniorCitizen": 1 if senior == "Yes" else 0,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}

# Convert to DataFrame
input_df = pd.DataFrame([raw_input])

# One-hot encode the input to match training
input_encoded = pd.get_dummies(input_df)

# Add any missing columns and reorder to match model
for col in features:
    if col not in input_encoded.columns:
        input_encoded[col] = 0
input_encoded = input_encoded[features]

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_encoded)[0]
    prediction_prob = model.predict_proba(input_encoded)[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ The customer is likely to churn (Probability: {prediction_prob:.2f})")
    else:
        st.success(f"✅ The customer is likely to stay (Probability: {1 - prediction_prob:.2f})")
        
