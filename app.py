import streamlit as st
from stt import transcribe
from intent import detect_intent
from tools import create_file, write_code, generate_code, summarize_text, extract_filename
from utils import save_temp_audio
from audio import record_audio

st.set_page_config(page_title="Advanced Voice AI Agent", layout="wide")

st.title("🎙 Advanced Voice AI Agent")

if "history" not in st.session_state:
    st.session_state.history = []

# INPUT MODE
mode = st.radio("Choose Input Mode", ["Upload Audio", "Record Audio"])

audio_path = None

if mode == "Upload Audio":
    uploaded_audio = st.file_uploader("Upload Audio", type=["wav", "mp3"])
    if uploaded_audio:
        audio_path = save_temp_audio(uploaded_audio)

else:
    duration = st.slider("Recording Duration (seconds)", 3, 10, 5)
    if st.button("🎤 Start Recording"):
        with st.spinner("Recording..."):
            audio_path = record_audio(duration)

# PROCESS
if audio_path:
    with st.spinner("Transcribing..."):
        text = transcribe(audio_path)

    st.subheader("📝 Transcription")
    st.write(text)

    if text.startswith("ERROR"):
        st.error(text)
        st.stop()

    with st.spinner("Detecting Intent..."):
        intents = detect_intent(text)

    st.subheader("🧠 Detected Intents")
    st.write(intents)

    results = []

    for intent in intents:
        intent = intent.strip()

        if intent == "create_file":
            filename = extract_filename(text)
            if st.button(f"Confirm create {filename}"):
                results.append(create_file(filename))

        elif intent == "write_code":
            code = generate_code(text)
            st.code(code, language="python")

            filename = extract_filename(text)
            if st.button(f"Save code to {filename}"):
                results.append(write_code(filename, code))

        elif intent == "summarize":
            results.append(summarize_text(text))

        elif intent == "chat":
            results.append("General conversation detected.")

    st.subheader("⚙️ Results")
    for r in results:
        st.write(r)

    st.session_state.history.append({
        "text": text,
        "intents": intents,
        "results": results
    })

# HISTORY
st.sidebar.title("📜 History")
for item in st.session_state.history[::-1]:
    st.sidebar.write(f"Text: {item['text']}")
    st.sidebar.write(f"Intents: {item['intents']}")
    st.sidebar.write(f"Results: {item['results']}")
    st.sidebar.write("---")