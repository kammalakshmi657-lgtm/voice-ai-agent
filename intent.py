import ollama

def detect_intent(text):
    prompt = f"""
Classify the user's intent(s) into one or more of these:
- create_file
- write_code
- summarize
- chat

Return as comma-separated values.

Text: {text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip().lower().split(",")