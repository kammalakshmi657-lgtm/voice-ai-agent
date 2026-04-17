# 🎙 Voice-Controlled Local AI Agent

## 📌 Overview
This project is a voice-controlled AI agent that accepts audio input, converts it into text, detects user intent using an LLM, and performs actions such as file creation, code generation, and summarization.

---

## 🚀 Features
- 🎤 Audio Input (Upload + Microphone)
- 📝 Speech-to-Text using Groq API
- 🧠 Intent Detection using Ollama (Llama3)
- 📂 File Creation (safe in /output folder)
- 💻 Code Generation and saving
- 📄 Text Summarization
- 🔄 Multi-intent support
- 🧠 Session memory

---

## 🏗 Architecture
Audio → Text (STT) → Intent Detection → Tool Execution → Output

---

## 🛠 Tech Stack
- Python
- Streamlit
- Groq API (Whisper)
- Ollama (Llama3)

---

## ⚙️ Setup Instructions
```bash
pip install -r requirements.txt
ollama run llama3
python -m streamlit run app.py
