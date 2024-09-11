import streamlit as st
import speech_recognition as sr
from textblob import TextBlob

# Title of the application
st.title('Audio Sentiment Analysis')

# File uploader widget
uploaded_file = st.file_uploader("Choose an audio file", type=["wav"])

if uploaded_file is not None:
    # Save the uploaded file
    with open("/tmp/uploaded_file.wav", "wb") as f:
        f.write(uploaded_file.getvalue())
    
    # Function to transcribe audio to text
    def transcribe_audio(file_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return text

    # Function to analyze sentiment of the text
    def analyze_sentiment(text):
        analysis = TextBlob(text)
        sentiment = 'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'
        return sentiment

    # Transcribe and analyze
    text = transcribe_audio("/tmp/uploaded_file.wav")
    sentiment = analyze_sentiment(text)

    # Display results
    st.write("Transcribed Text:")
    st.write(text)
    st.write("Sentiment:")
    st.write(sentiment)
import streamlit as st
import speech_recognition as sr
from textblob import TextBlob

# Title of the application
st.title('Audio Sentiment Analysis')

# File uploader widget
uploaded_file = st.file_uploader("Choose an audio file", type=["wav"])

if uploaded_file is not None:
    # Save the uploaded file
    with open("/tmp/uploaded_file.wav", "wb") as f:
        f.write(uploaded_file.getvalue())
    
    # Function to transcribe audio to text
    def transcribe_audio(file_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return text

    # Function to analyze sentiment of the text
    def analyze_sentiment(text):
        analysis = TextBlob(text)
        sentiment = 'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'
        return sentiment

    # Transcribe and analyze
    text = transcribe_audio("/tmp/uploaded_file.wav")
    sentiment = analyze_sentiment(text)

    # Display results
    st.write("Transcribed Text:")
    st.write(text)
    st.write("Sentiment:")
    st.write(sentiment)

