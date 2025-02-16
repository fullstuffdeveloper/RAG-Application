import pdfplumber
import pandas as pd

def extract_text_from_file(file_path: str):
    """Extract text from different file formats."""
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        return df.to_string()
    return ""