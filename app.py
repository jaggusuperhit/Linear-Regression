from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

# Sample locations data
locations = [
    "1st Phase JP Nagar",
    "1st Block Jayanagar",
    "2nd Phase Judicial Layout",
    "2nd Stage Nagarbhavi",
    "5th Block Hbr Layout",
    # Add more locations as needed
]

@app.route('/')
def index():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.get_json()
        location = data.get('location')
        bhk = float(data.get('bhk'))
        bath = float(data.get('bathrooms'))
        sqft = float(data.get('sqft'))

        # Dummy prediction logic - replace with your actual model
        base_price = sqft * 5000  # ₹5000 per sqft as base
        location_factor = 1.2 if location == "1st Phase JP Nagar" else 1.0
        bhk_factor = 1 + (bhk - 1) * 0.1
        bath_factor = 1 + (bath - 1) * 0.05
        
        price = base_price * location_factor * bhk_factor * bath_factor
        price_rounded = round(price / 100000) * 100000  # Round to nearest lakh
        
        return jsonify({
            'price': f"₹{price_rounded:,.2f}",
            'estimate': "(estimate)"
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)