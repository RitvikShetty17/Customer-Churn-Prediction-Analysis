# Customer Churn Prediction Analysis 
_____________________________________

# Project Objective

The goal of this project is to analyze customer data to identify the key factors contributing to customer churn and suggest actionable strategies to retain customers. The analysis aims to:

Understand churn patterns across demographics and services.

Identify the major features affecting customer decisions to leave.

Provide actionable insights to improve customer retention.

_____________________________________

# Dataset Overview

The dataset used contains information about customer demographics, service plans, billing methods, tenure, and churn status. 

Some of the key columns include:

gender, SeniorCitizen, Partner, Dependents, tenure, MonthlyCharges, TotalCharges, PhoneService, InternetService, 
Contract, PaymentMethod, Churn (target variable)

_____________________________________

# Business Insights

From the analysis, several important insights were discovered:

**Contract Type & Churn:**

Month-to-month contracts have the highest churn rate.

Customers with longer contracts (1 or 2 years) tend to stay longer.

**Tenure & Churn:**

New customers (tenure < 6 months) are more likely to churn.

Retaining customers past the 1-year mark significantly reduces churn.

**Service Usage:**

Customers with fiber optic internet churn more than those with DSL.

Lack of add-on services (e.g., Online Backup, Tech Support) is associated with higher churn.

**Monthly Charges:**

High monthly charges correlate with higher churn probability, especially when bundled with short contracts.

**Payment Method:**

Electronic check users have higher churn compared to those using credit card or bank transfer.

**Senior Citizens:**

Slightly higher churn rate than younger customers, possibly due to pricing or support needs.

_____________________________________


# Preprocessing and Changes Made

Handled missing values in TotalCharges.

Converted categorical variables using label encoding and one-hot encoding.

Visualized feature relationships using bar plots, histograms, and heatmaps.

Used correlation analysis and feature importance from tree-based models for insight extraction.

_____________________________________

# What can we do to Reduce Churn

Based on the insights above, we can do the following improvements:

**Incentivize Longer Contracts:**

Offer discounts or loyalty perks for customers switching to annual contracts.

**Early Engagement:**

Focus on retaining customers during the first 6 months with welcome benefits and personalized offers.

**Enhance Service Bundles:**

Encourage bundling of services (tech support, backup, etc.) with packages to increase customer dependency and satisfaction.

**Pricing Optimization:**

Create pricing tiers that offer better value to high-paying customers to reduce dissatisfaction.

**Change Payment Behavior:**

Offer incentives for switching to credit card or bank transfer to reduce churn from electronic check users.

**Targeted Communication:**

Provide targeted retention campaigns to high-risk segments like senior citizens and fiber optic users.

_____________________________________


# Churn Predictor Web App (Streamlit)

# What It Does

An interactive web app that allows users to input customer details and get a churn prediction instantly. Built using **Streamlit**, it brings the machine learning model to life in a user-friendly interface.

# How It Works

1. Trained model and expected features are loaded from `.pkl` files.
2. The app collects user input via dropdowns, sliders, and numeric inputs.
3. The inputs are encoded to match the training features.
4. The Logistic Regression model makes a prediction.
5. The result (Yes/No) is shown along with the probability.

# Benefits

- Empowers business users to understand churn risk
- No coding required to use the app
- Helps teams explore "what-if" scenarios

_____________________________________

# Conclusion

This project successfully demonstrates how data-driven analysis can uncover key drivers of customer churn in a telecom business. By leveraging visual exploration, feature engineering, and predictive modeling, we identified high-risk customer segments and proposed actionable strategies to enhance retention. These insights can directly support marketing, customer service, and product teams in reducing churn and increasing customer lifetime value.

For complete code, visualizations, and detailed explanations, please refer to the accompanying Jupyter Notebook.