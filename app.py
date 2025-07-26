import streamlit as st
from src.helper import voice_input, llm_model, text_to_speech
import os

def main():
    st.title("🌍 Multilingual AI Voice Assistant")
    st.markdown("---")
    st.write("✨ Click the button below and speak for 5 seconds. AI will understand and respond to you.")
    
    if st.button("🗣️ Ask me anything"):
        with st.spinner("Listening for 5 seconds..."):
            try:
                text = voice_input()
                
                if text:
                    st.success(f"**You said:** {text}")
                    
                    with st.spinner("Generating response..."):
                        response = llm_model(text)
                        text_to_speech(response)
                        
                        st.markdown("### AI Response:")
                        st.info(response)
                        
                        if os.path.exists("response.mp3"):
                            with open("response.mp3", "rb") as audio_file:
                                audio_bytes = audio_file.read()
                            
                            st.markdown("### 🔊 Listen to the Response:")
                            st.audio(audio_bytes)
                            st.download_button(
                                label="Download Audio Response",
                                data=audio_bytes,
                                file_name="response.mp3",
                                mime="audio/mp3"
                            )
                        else:
                            st.warning("Audio response unavailable")
                else:
                    st.warning("🔇 No speech detected. Please try speaking again clearly.")
                    
            except Exception as e:
                st.error(f"Oops! Something went wrong: {str(e)}")
    
    st.markdown("---")
    st.markdown("💡 **Tip:** Speak clearly and at a normal pace for best results!")

if __name__ == "__main__":
    main()

st.markdown("""
        <style>
        .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgb(39 48 66);
        text-align: center;
        font-size: 0.875rem;
        color: #888;
        padding: 0.75rem 0.75rem;
        box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.05);
        font-family: 'Segoe UI', sans-serif;
        z-index: 999;
    }
    </style>
    <div class="footer">
        Made by <strong>Chirag Singhvi</strong>👨‍💻
    </div>
""", unsafe_allow_html=True)
