
import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("Amazon Delivery Time Predictor")
st.write("Enter order details to predict delivery time (in hours).")

# Load best model
model = joblib.load("best_model.pkl")

# Input fields
agent_age = st.number_input("Agent Age", min_value=18, max_value=60, value=25)
agent_rating = st.number_input("Agent Rating (1-5)", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
store_lat = st.number_input("Store Latitude", value=0.0)
store_lon = st.number_input("Store Longitude", value=0.0)
drop_lat = st.number_input("Drop Latitude", value=0.0)
drop_lon = st.number_input("Drop Longitude", value=0.0)
weather = st.selectbox("Weather Condition", ["Clear", "Rainy", "Cloudy", "Storm"])
traffic = st.selectbox("Traffic Condition", ["Low", "Medium", "High"])

# Function to calculate approximate distance (simple Euclidean for demo)
def calc_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

distance = calc_distance(store_lat, store_lon, drop_lat, drop_lon)

# Predict button
if st.button("Predict Delivery Time"):
    # Create DataFrame for model
    input_df = pd.DataFrame([[agent_age, agent_rating, distance, weather, traffic]],
                            columns=["Agent_Age","Agent_Rating","Distance","Weather","Traffic"])
    
    # One-hot encoding for categorical features
    input_df = pd.get_dummies(input_df)
    
    # Align columns with training data (optional: you may need to adjust this)
    model_columns = model.feature_names_in_
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[model_columns] 
    
    # Prediction
    pred = model.predict(input_df)
    st.success(f"Estimated Delivery Time: {pred[0]:.2f} hours")
