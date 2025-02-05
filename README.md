# Hate-Speech
# Hate Speech/Offensive Language Detection
This web application uses deep learning to detect hate speech and offensive language in text. Built
with a microservices architecture, it offers scalable, real-time content moderation. The application
includes a feedback system that allows user input to improve the model's performance over time by
adding new data for future training, enhancing accuracy and adaptability.
## Features
- **Real-time content moderation**: Automatically detects offensive language or hate speech in
user-submitted text.
- **User feedback system**: Allows users to provide feedback, helping improve the model's
performance over time.
- **Deep Learning Model**: Uses advanced NLP models, such as transformers, to classify text into
offensive or non-offensive categories.
- **Analytics**: Provides detailed statistics and charts to visualize model performance and detected
patterns in the data.
---
## How to Start Using It
Follow these steps to get the application running on your local machine.
### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/hate-speech-detector.git
```
### 2. Set Up the Backend
- Navigate to the backend folder:
```bash
cd hate-speech-detector-backend
```
- Install the necessary Python dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
- Ensure you have all the required files in place:
 - `hate_speech_detector.h5`: Pre-trained model for detecting hate speech.
 - `model_final_my_correct.h5`: Model for prediction.
 - `tfidf_vectorizer.pkl` & `tokenizer_final_my_correct.pkl`: Files for text preprocessing.
- Start the backend server:
```bash
python app.py
```
The backend will run on a local server (e.g., `http://127.0.0.1:5000`).
### 3. Set Up the Frontend
- Navigate to the frontend folder:
```bash
cd hate-speech-detector-frontend
```
- Install the necessary Node.js dependencies:
```bash
npm install
```
- Start the frontend server:
```bash
npm start
```
The frontend will run on `http://localhost:3000` and connect to the backend to send user input for
moderation.
### 4. Test the Application
- Open your browser and visit `http://localhost:3000`.
- Use the input box to test hate speech detection by entering text.
- The app will return whether the text contains hate speech/offensive language and show relevant
analytics.
### 5. Provide Feedback
- After testing, you can contribute by providing feedback to the model. This will help enhance the
accuracy and adaptability of future versions.
---
## File Structure Overview
### Backend:
- `app.py`: Main application to run the backend server.
- `data.py`: Data processing utilities.
- `hate_speech_detector.h5`: Pre-trained model.
- `requirements.txt`: List of required Python dependencies.
- `tfidf_vectorizer.pkl`, `tokenizer_final_my_correct.pkl`: Tools for text preprocessing.
### Frontend:
- `app.js`: Main React application code.
- `Home.js`: Home page to interact with the application.
- `Report.js`: Page to display the model's performance statistics.
- `ModelChart.js`, `ConfusionMatrix.js`: Charts to visualize model statistics.
---
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---
