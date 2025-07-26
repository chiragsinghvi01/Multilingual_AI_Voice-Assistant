import whisper
from google import genai
import pyttsx3 as tts
from dotenv import load_dotenv
import os
import sounddevice as sd
import soundfile as sf
import tempfile
import numpy as np

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def voice_input():
    pass

def llm_model(user_text):
    pass

def text_to_speech(text):
    pass