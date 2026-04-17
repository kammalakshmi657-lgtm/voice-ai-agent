import os
import ollama

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_filename(text):
    words = text.split()
    for w in words:
        if "." in w:
            return w
    return "default.txt"

def create_file(filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write("")
    return f"File '{filename}' created."

def generate_code(prompt):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": f"Write clean Python code for: {prompt}"}]
    )
    return response["message"]["content"]

def write_code(filename, code):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    return f"Code saved to '{filename}'."

def summarize_text(text):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": f"Summarize this text clearly: {text}"}]
    )
    return response["message"]["content"]