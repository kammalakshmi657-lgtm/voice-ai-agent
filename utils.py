import uuid

def save_temp_audio(uploaded_file):
    filename = f"temp_{uuid.uuid4()}.wav"
    with open(filename, "wb") as f:
        f.write(uploaded_file.read())
    return filename