from groq import Groq

client = Groq(api_key="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")

def transcribe(audio_path):
    try:
        with open(audio_path, "rb") as f:
            response = client.audio.transcriptions.create(
                file=f,
                model="whisper-large-v3"
            )
        return response.text
    except Exception as e:
        return f"ERROR: {str(e)}"