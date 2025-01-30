import streamlit as st
import requests

# Define the Flask API URL
API_URL = "http://127.0.0.1:5000/predict"

# Streamlit UI
st.title("Sports Performance and Injury Prediction")

# Collect user inputs
age = st.number_input("Age", min_value=10, max_value=50, value=25)
height = st.number_input("Height (cm)", min_value=100, max_value=220, value=180)
weight = st.number_input("Weight (kg)", min_value=30, max_value=150, value=75)
experience = st.number_input("Experience (Years)", min_value=0, max_value=30, value=5)
matches = st.number_input("Matches Played", min_value=0, max_value=200, value=20)
endurance = st.number_input("Endurance Score", min_value=0, max_value=100, value=80)
strength = st.number_input("Strength Score", min_value=0, max_value=100, value=90)

# Button to send the request
if st.button("Predict Performance & Injury Risk"):
    data = {
        "Age": age,
        "Height_cm": height,
        "Weight_kg": weight,
        "Experience_years": experience,
        "Matches_Played": matches,
        "Endurance_Score": endurance,
        "Strength_Score": strength
    }
    
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"**Performance Score:** {result['Performance_Score']}")
            st.warning(f"**Injury Risk:** {result['Injury_Risk']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

