from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your saved models
performance_model = pickle.load(open("C:/Users/udayk/sports-performance-backend/performance_model.pkl", "rb"))
injury_model = pickle.load(open("C:/Users/udayk/sports-performance-backend/injury_risk_model.pkl", "rb"))

# Root route
@app.route('/', methods=['GET'])

def predict_model():
    try:
        # Get the input data from the request
        data = request.json

        # Extract features from the input data
        features = np.array([
            data['Age'], data['Height_cm'], data['Weight_kg'], data['Experience_years'],
            data['Matches_Played'], data['Endurance_Score'], data['Strength_Score']
        ]).reshape(1, -1)
        if isinstance(performance_model, np.ndarray):
            print("Error: performance_model is a NumPy array, not a model.")
        if isinstance(injury_model, np.ndarray):
            print("Error: injury_model is a NumPy array, not a model.")


        # Make predictions using the models
        performance_score = performance_model.predict(features)[0]
        injury_risk = injury_model.predict(features)[0]

        # Return the predictions as a JSON response
        return jsonify({
            "Performance_Score": performance_score,
            "Injury_Risk": injury_risk
        })

    except KeyError as e:
        # Handle missing keys in the request
        return jsonify({"error": f"Missing feature: {e}"}), 400


if __name__ == '__main__':
    app.run(debug=True)
