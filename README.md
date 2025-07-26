# 🌍 Multilingual AI Voice Assistant

A sophisticated voice-powered AI assistant that can understand speech in multiple languages, process natural language queries using Google's Gemini AI, and respond with both text and audio feedback through an intuitive Streamlit interface.

## ✨ Features

- **🎤 Voice Input**: Real-time speech recognition using OpenAI Whisper
- **🧠 AI-Powered Responses**: Leverages Google's Gemini 1.5 Flash model for intelligent conversations
- **🔊 Text-to-Speech**: Converts AI responses to natural-sounding audio
- **🌐 Multilingual Support**: Understands and processes multiple languages
- **📱 User-Friendly Interface**: Clean and intuitive Streamlit web interface
- **💾 Audio Download**: Download generated audio responses
- **⚡ Real-time Processing**: Fast response times with efficient processing

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.13.5** - Primary programming language
- **Streamlit** - Web interface framework
- **OpenAI Whisper** - Speech-to-text conversion
- **Google Gemini AI** - Large Language Model for responses
- **pyttsx3** - Text-to-speech synthesis

### Audio Processing
- **sounddevice** - Audio recording and playback
- **numpy** - Audio data manipulation

### Development Tools
- **python-dotenv** - Environment variable management
- **setuptools** - Package building and distribution

## 🎯 How It Works

1. **Voice Capture**: Uses `sounddevice` to record 5 seconds of audio
2. **Speech Recognition**: OpenAI Whisper converts speech to text
3. **AI Processing**: Google Gemini processes the text and generates a response
4. **Text-to-Speech**: pyttsx3 converts the response to audio
5. **User Interface**: Streamlit displays results and provides audio playback

## 👨‍💻 Author

**Chirag Singhvi**
- Email: csinghvi15@gmail.com
- GitHub: [@chiragsinghvi01](https://github.com/chiragsinghvi01)
