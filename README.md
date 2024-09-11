# Streamlit Audio Sentiment Analysis

## Overview

This Streamlit application allows users to upload audio files, which are then transcribed to text and analyzed for sentiment. The sentiment is classified as Positive, Negative, or Neutral based on the analysis of the transcribed text.

## Features

- **Audio File Upload**: Upload audio files through the Streamlit interface.
- **Audio Transcription**: Transcribe audio files to text using Google's Web Speech API.
- **Sentiment Analysis**: Analyze the sentiment of the transcribed text using TextBlob.

## Prerequisites

- Python 3.10 or higher
- Streamlit
- SpeechRecognition
- TextBlob

## Installation

### Clone the Repository

Clone the repository to your local machine:
git clone <repository-url>
cd <repository-directory>

# Install Required Packages
##Install the required Python packages using pip:
pip install -r requirements.txt

# Running the Application Locally
## Navigate to the Project Directory: Ensure you're in the directory containing app.py:

cd path/to/your/streamlit_app
## Run the Streamlit Application: Start the Streamlit server:
streamlit run app.py
# Access the Application: Open a web browser and go to the URL provided in the terminal, typically http://localhost:8501.
# # Application Usage
### Upload an Audio File: Use the file uploader to select and upload an audio file (supported formats: .wav).

View Results: After uploading the file, the application will display:

The transcribed text from the audio file.
The sentiment of the transcribed text (Positive, Negative, or Neutral).
Deployment
AWS Elastic Beanstalk
For deploying the Streamlit application to AWS Elastic Beanstalk:

Prepare the Project for Deployment: Ensure you have the necessary files and configurations, such as requirements.txt and Procfile.

Create and Configure Elastic Beanstalk Application: Follow the AWS Elastic Beanstalk Deployment Guide to set up your environment and deploy your application.

Heroku
For deploying to Heroku:

Prepare Your Heroku Application:

Make sure you have a Procfile with the following content:
text
Copy code
web: streamlit run app.py
Deploy to Heroku:

Follow the Heroku Deployment Guide for detailed steps on deploying a Python application to Heroku.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Streamlit
SpeechRecognition
TextBlob
css
Copy code

Feel free to adjust any details according to your specific project needs or deployment setup
