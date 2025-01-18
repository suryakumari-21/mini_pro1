from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get quiz responses from frontend
        responses = request.json['responses']  # List of 0 (No) and 1 (Yes)

        # Calculate the total number of "Yes" answers
        yes_count = sum(responses)

        # Determine stress level based on "Yes" count
        if yes_count > 7:
            stress_level = 'High Stress'
        elif yes_count < 3:
            stress_level = 'Low Stress'
        else:
            stress_level = 'Moderate Stress'

        return jsonify({'stress_level': stress_level})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)