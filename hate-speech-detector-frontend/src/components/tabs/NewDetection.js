import React, { useState } from "react";
import { Input, Button, Progress, message } from "antd";
import axios from "axios";

const NewDetection = () => {
  const [inputText, setInputText] = useState("");
  const [resultText, setResultText] = useState("");
  const [progress, setProgress] = useState(0);
  const [isInputDisabled, setIsInputDisabled] = useState(false); // New state to disable input

  // Handle prediction by sending the text to the Flask backend
  const handlePredict = async () => {
    if (!inputText) {
      message.error("Please enter some text");
      return;
    }

    try {
      // Send a POST request to Flask backend with the input text
      const response = await axios.post("http://localhost:5000/predict", {
        text: inputText,
      });

      // Extract prediction result from the backend response
      const { label, probability } = response.data;

      // Update the result and progress based on the response
      setResultText(
        label === 1 ? "This is hate speech" : "This is not hate speech"
      );
      setProgress(probability * 100); // Convert to percentage

      // Disable the input after checking
      setIsInputDisabled(true);
    } catch (error) {
      message.error("Error while checking the text");
    }
  };

  // Handle saving the text and label (validating) by sending it to the backend
  const handleSave = async () => {
    const label = progress >= 50 ? 1 : 0;

    try {
      // Send a POST request to the Flask backend to save the validated data
      await axios.post("http://localhost:5000/save", {
        text: inputText,
        label,
      });

      message.success("Text saved successfully!");
      handleClear(); // Clear the input after saving
    } catch (error) {
      message.error("Error while saving the data");
    }
  };

  // Clear the input and reset the result
  const handleClear = () => {
    setInputText("");
    setResultText("");
    setProgress(0);
    setIsInputDisabled(false); // Re-enable input when starting a new one
  };

  return (
    <div>
      <Input.TextArea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text here"
        style={{ marginBottom: 16 }}
        disabled={isInputDisabled} // Disable input when isInputDisabled is true
      />
      <Button
        type="primary"
        onClick={handlePredict}
        style={{ marginBottom: 16 }}
        disabled={isInputDisabled} // Disable button when input is disabled
      >
        Check
      </Button>

      <div
        style={{
          padding: 16,
          border: "1px solid #f0f0f0",
          borderRadius: 4,
          marginBottom: 16,
        }}
      >
        <h3>Result</h3>
        <p>{resultText}</p>
        <Progress percent={progress} />
      </div>
      <Button style={{ marginRight: 8 }} onClick={handleClear}>
        Not Valid and Start New One
      </Button>
      <Button type="primary" onClick={handleSave}>
        Valid and Save
      </Button>
    </div>
  );
};

export default NewDetection;
