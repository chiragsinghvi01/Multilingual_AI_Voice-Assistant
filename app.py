import streamlit as st
from src.helper import voice_input, llm_model, text_to_speech

def main():
    st.title("Multilingual AI Voice Assistant")
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = llm_model(text)
            text_to_speech(response)

            audio_file = open("response.mp3", "rb")
            audio_bytes = audio_file.read()

            st.text_area("Response", value=response, height=300)

            st.audio(audio_bytes)
            st.download_button(
                label="Download Response",
                data=audio_bytes,
                file_name="response.mp3",
                mime="audio/mp3"
            )

if __name__ == "__main__":
    main()