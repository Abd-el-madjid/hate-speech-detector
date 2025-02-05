from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text")
    # Replace this with your model's prediction logic
    result = {"text": text, "is_hate_speech": False}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
