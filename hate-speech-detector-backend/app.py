import time
from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from flask_cors import CORS
import re
import string
from datetime import datetime
import joblib  # Used for loading the tokenizer
from collections import Counter

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model statically
#model = load_model("model_final_my_correct.h5")
model1 = load_model("hate_speech_detector.h5")

print("Model loaded successfully.")

# Load the tokenizer from a file (replace 'tokenizer.pkl' with the actual file name)
# Assuming the tokenizer was saved with joblib
tokenizer_file = 'tokenizer_final_my_correct.pkl'
tokenizer = joblib.load(tokenizer_file)
print("Tokenizer loaded successfully.")
vectorizer = joblib.load('tfidf_vectorizer.pkl')
print("vectorizer loaded successfully.")

# Preprocess text for prediction

# Load hate words from CSV
# hate_words_file = 'hate_words.csv'
# if os.path.exists(hate_words_file):
#     hate_words_df = pd.read_csv(hate_words_file)
#     hate_words = set(hate_words_df['word'].str.lower())
# else:
#     hate_words = set()
#     print("Hate words file not found. Ensure hate_words.csv is available.")


def preprocess_text(text):
    # Ensure the input is a string
    if not isinstance(text, str):
        text = str(text)  # Convert to string if it's not already

    text = text.lower()
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\w*\d\w*", "", text)
    text = re.sub(r" {2,}", " ", text)
    text = text.strip()
    seq = tokenizer.texts_to_sequences([text])
    return pad_sequences(seq, maxlen=100)


def preprocess_text1(text):
    # Ensure the input is a string
    if not isinstance(text, str):
        text = str(text)  # Convert to string if it's not already

    text = text.lower()
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\w*\d\w*", "", text)
    text = re.sub(r" {2,}", " ", text)
    text = text.strip()
    speech = vectorizer.transform([text])

    return speech
# Endpoint to predict hate speech on a single input text

import random

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Preprocess and predict using ML model
        processed_text = preprocess_text1(text)
        prediction = model1.predict(processed_text)
        label = int(prediction[0] > 0.5)
        probability = float(prediction[0])

        # Check for direct hate words match
        # words = set(re.findall(r'\b\w+\b', text.lower()))
        # if label == 0 and any(word in hate_words for word in words):
        #     return jsonify({
        #         'label': 1,  # Hate speech
        #         'probability': round(random.uniform(0.8, 0.9), 2),
        #         'message': "Text contains hate words but was predicted as non-hate."
        #     })

        # Return the prediction normally if no hate words are found
        return jsonify({
            'label': label,
            'probability': probability
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/save', methods=['POST'])
def save():
    data = request.json
    content = data.get('text')
    label = data.get('label')
    file_path = 'validated_data.csv'

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=['Label', 'Content', 'Date'])

    new_entry = pd.DataFrame({
        'Content': [content],
        'Label': [label],
        'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(file_path, index=False)

    return jsonify({'message': 'Data saved successfully'}), 200

# Endpoint to retrieve saved prediction history


@app.route('/history', methods=['GET'])
def get_history():
    file_path = 'validated_data.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        data = df.to_dict(orient='records')
    else:
        data = []

    return jsonify(data), 200

# Endpoint to upload a dataset


@app.route('/upload_dataset', methods=['POST'])
def upload_dataset():
    if 'dataset' not in request.files:
        return jsonify({"error": "No dataset file uploaded"}), 400
    file = request.files['dataset']
    upload_path = os.path.join("uploads", file.filename)
    file.save(upload_path)
    return jsonify({"message": "Dataset uploaded successfully", "path": upload_path}), 200

# Helper function to get the latest uploaded file


def get_latest_uploaded_file():
    uploads_dir = "uploads"
    if not os.path.exists(uploads_dir):
        return None
    files = [os.path.join(uploads_dir, f)
             for f in os.listdir(uploads_dir) if f.endswith('.csv')]
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

# Endpoint to calculate model statistics on the latest uploaded dataset


# Get the latest uploaded file from the uploads directory
UPLOADS_DIRECTORY = "uploads"


@app.route('/datasets', methods=['GET'])
def get_datasets():
    uploads_dir = "uploads"
    if not os.path.exists(uploads_dir):
        return jsonify([])
    
    datasets = [f for f in os.listdir(uploads_dir) if f.endswith('.csv')]
    return jsonify(datasets)



@app.route('/model-statistics', methods=['GET'])
def model_statistics():
    # Get dataset name from query parameters
    dataset_name = request.args.get('dataset')
    print(f"Received dataset: {dataset_name}")
    
    if not dataset_name:
        print("Error: Dataset not selected")
        return jsonify({"error": "Dataset not selected"}), 400

    # Construct the path to the dataset
    dataset_path = os.path.join('uploads', dataset_name)
    print(f"Dataset path: {dataset_path}")

    # Check if the dataset file exists
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_name} not found in uploads folder.")
        return jsonify({"error": "Dataset not found"}), 400

    try:
        # Load the dataset
        print(f"Loading dataset from: {dataset_path}")
        df = pd.read_csv(dataset_path)
        print(f"Dataset loaded successfully. Shape: {df.shape}")
        
        # Print the first few rows of the dataset
        print(f"First few rows of the dataset:\n{df.head()}")
        
        # Ensure the dataset has at least two columns
        if df.shape[1] < 2:
            print("Error: Dataset must contain at least two columns")
            return jsonify({"error": "Dataset must contain at least two columns"}), 400

        # Identify label (0/1) and text columns
        label_column = None
        text_column = None

        # Loop through the columns to find label and text columns
        for col in df.columns:
            unique_values = df[col].dropna().unique()
            print(f"Checking column: {col}, unique values: {unique_values}")
            
            if set(unique_values).issubset({0, 1})  :
                label_column = col
            else:
                text_column = col

        # Print the identified columns
        print(f"Identified label column: {label_column}, text column: {text_column}")

        # Validate the identified columns
        if label_column is None or text_column is None:
            print("Error: Unable to identify label and text columns.")
            return jsonify({"error": "Data incompatible: Unable to identify label (0/1) and text columns"}), 400

        # Prepare X_test and y_test
        y_test = df[label_column].values
        X_test = df[text_column].apply(preprocess_text).tolist()
        print(f"X_test (first 5 samples): {X_test[:5]}")

        # Convert to input shape suitable for the model
        X_test = np.array(X_test).reshape(-1, 100)
        print(f"X_test shape after reshaping: {X_test.shape}")

        # Measure inference time
        start_time = time.time()
        y_pred = [int(model.predict(np.expand_dims(x, axis=0))[0] > 0.5) for x in X_test]
        end_time = time.time()
        
        # Calculate inference time
        inference_time = end_time - start_time
        avg_inference_time_per_sample = inference_time / len(X_test)
        print(f"Inference time: {inference_time:.4f} seconds")
        print(f"Average inference time per sample: {avg_inference_time_per_sample:.4f} seconds")

        # Calculate evaluation metrics
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        class_distribution = dict(Counter(y_test))
        prediction_distribution = dict(Counter(y_pred))

        print(f"Accuracy: {accuracy:.4f}")
        print(f"F1 Score: {f1:.4f}")
        print(f"Confusion Matrix:\n{conf_matrix}")
        print(f"Class distribution (actual): {class_distribution}")
        print(f"Prediction distribution: {prediction_distribution}")

        # Save inference time to history (assuming the function save_cost_history is defined elsewhere)
        save_cost_history(inference_time)

        return jsonify({
            'accuracy': accuracy,
            'f1_score': f1,
            'confusion_matrix': conf_matrix.tolist(),
            'inference_time': inference_time,
            'avg_inference_time_per_sample': avg_inference_time_per_sample,
            'class_distribution': {int(k): v for k, v in class_distribution.items()},
            'prediction_distribution': {int(k): v for k, v in prediction_distribution.items()},
        })


    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Helper function to save cost history
def save_cost_history(inference_time):
    file_path = "cost_history.csv"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=['Timestamp', 'InferenceTime'])

    new_entry = pd.DataFrame({
        'Timestamp': [current_time],
        'InferenceTime': [inference_time]
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(file_path, index=False)


@app.route('/cost-history', methods=['GET'])
def get_cost_history():
    file_path = 'cost_history.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        data = df.to_dict(orient='records')
    else:
        data = []
    return jsonify(data), 200


if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)
