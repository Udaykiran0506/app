import streamlit as st


page_bg_img="""
<style>
[data-testid="stMain"] {
background-image: url("https://unsplash.com/photos/a-woman-working-on-a-laptop-6uAssP0vuPs");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


with open('app.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Define a simple prediction function
def predict_performance_and_injury(data):
    # Dummy calculation for demonstration
    performance_score = (data["Endurance_Score"] * 0.4 + 
                         data["Strength_Score"] * 0.3 + 
                         data["Experience_years"] * 0.2 + 
                         data["Matches_Played"] * 0.1)
    
    injury_risk = "High" if data["Strength_Score"] < 50 else "Low"
    
    return {"Performance_Score": round(performance_score, 2), "Injury_Risk": injury_risk}

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

# Button to predict
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
    
    # Call local function instead of sending API request
    result = predict_performance_and_injury(data)

    st.success(f"**Performance Score:** {result['Performance_Score']}")
    st.warning(f"**Injury Risk:** {result['Injury_Risk']}")
