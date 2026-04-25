import os
import re


def create_folder(path):
    os.makedirs(path, exist_ok=True)


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def detect_severity(text):
    text = text.lower()

    if "leakage" in text or "seepage" in text:
        return "High"

    elif "dampness" in text or "efflorescence" in text:
        return "Moderate"

    elif "crack" in text:
        return "Moderate"

    return "Low"


def split_chunks(text, size=3000):
    return [text[i:i+size] for i in range(0, len(text), size)]