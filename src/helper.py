import whisper
from google import genai
import pyttsx3 as tts
from dotenv import load_dotenv
import os
import numpy as np
import sounddevice as sd

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

whisper_model = whisper.load_model("base")

def voice_input():
    print("🎤 Listening...")
    audio = sd.rec(80000, samplerate=16000, channels=1, dtype='float32')
    sd.wait()
    audio_data = audio.flatten().astype(np.float32)
    
    result = whisper_model.transcribe(audio_data)
    text = result["text"]
    
    return text.strip()

def llm_model(user_text):
    client = genai.Client(api_key=GOOGLE_API_KEY)
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=user_text
    )
    result = response.text
    return result

def text_to_speech(text):
    try:
        engine = tts.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.8)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        engine.save_to_file(text, 'response.wav')
        engine.runAndWait()
        
        import shutil
        if os.path.exists('response.wav'):
            shutil.move('response.wav', 'response.mp3')
        
        print(f"TTS: Audio file created successfully")
        
    except Exception as e:
        print(f"TTS Error: {str(e)}")
        with open('response.mp3', 'w') as f:
            f.write("dummy audio file")