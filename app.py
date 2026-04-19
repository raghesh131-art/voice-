import streamlit as st
from streamlit_mic_recorder import mic_recorder
from translator import text_to_code

st.title("🎤 VoiceScript - Online Voice + Code")

st.write("Record your voice:")

audio = mic_recorder(start_prompt="🎤 Start Recording",
                     stop_prompt="⏹ Stop",
                     key='recorder')

command = ""

if audio:
    st.audio(audio['bytes'])

    # Convert audio to text using OpenAI Whisper
    from openai import OpenAI
    client = OpenAI(api_key="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")

    with open("temp.wav", "wb") as f:
        f.write(audio['bytes'])

    with open("temp.wav", "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )

    command = transcript.text
    st.write("You said:", command)

# Generate code
if command:
    code = text_to_code(command)
    st.code(code)

    if st.button("Run Code"):
        exec(code)