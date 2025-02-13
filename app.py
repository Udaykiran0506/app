import streamlit as st
import pickle
import numpy as np

# Load CSS file for styling
with open('app.css', 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load pre-trained models
with open('/mnt/data/performance_model.pkl', 'rb') as f:
    performance_model = pickle.load(f)

with open('/mnt/data/injury_risk_model.pkl', 'rb') as f:
    injury_risk_model = pickle.load(f)

# Prediction function
def predict_performance_and_injury(data):
    try:
        # Convert inputs to float
        features = np.array([
            float(data["Age"]), float(data["Height_cm"]), float(data["Weight_kg"]),
            float(data["Experience_years"]), float(data["Matches_Played"]),
            float(data["Endurance_Score"]), float(data["Strength_Score"])
        ]).reshape(1, -1)
        
        # Predict using the models
        performance_score = performance_model.predict(features)[0]
        injury_risk = injury_risk_model.predict(features)[0]
        
        return {"Performance_Score": round(performance_score, 2), "Injury_Risk": injury_risk}
    
    except ValueError:
        return None  # Return None if inputs are invalid

# Streamlit UI
st.title("🏆 Sports Performance & Injury Prediction")

# Collect user inputs with default values
age = st.text_input("Age", placeholder="Enter your age")
height = st.text_input("Height (cm)", placeholder="Enter your height in cm")
weight = st.text_input("Weight (kg)", placeholder="Enter your weight in kg")
experience = st.text_input("Experience (Years)", placeholder="Enter years of experience")
matches = st.text_input("Matches Played", placeholder="Enter total matches played")
endurance = st.text_input("Endurance Score", placeholder="Enter endurance score (0-100)")
strength = st.text_input("Strength Score", placeholder="Enter strength score (0-100)")

# Button to predict
if st.button("Predict Performance & Injury Risk"):
    if age and height and weight and experience and matches and endurance and strength:
        data = {
            "Age": age,
            "Height_cm": height,
            "Weight_kg": weight,
            "Experience_years": experience,
            "Matches_Played": matches,
            "Endurance_Score": endurance,
            "Strength_Score": strength
        }
        
        # Call prediction function
        result = predict_performance_and_injury(data)
        
        if result:
            st.success(f"🏅 **Performance Score:** {result['Performance_Score']}")
            if result["Injury_Risk"] == "Low":
                st.success(f"✅ **Injury Risk:** {result['Injury_Risk']}")
            elif result["Injury_Risk"] == "Medium":
                st.warning(f"⚠️ **Injury Risk:** {result['Injury_Risk']}")
            else:
                st.error(f"❌ **Injury Risk:** {result['Injury_Risk']}")
        else:
            st.error("❌ Invalid input! Please enter only numerical values.")
    else:
        st.error("❌ Please fill in all fields before predicting.")
