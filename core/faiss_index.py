import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize FAISS and Model
model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384
index = faiss.IndexFlatL2(dimension)
documents = []

def add_to_index(text: str):
    """Convert text to embedding and store in FAISS."""
    documents.append(text)
    vector = model.encode([text])
    index.add(np.array(vector))

def search_index(query: str, k=3):
    """Retrieve top-k results from FAISS."""
    query_vector = model.encode([query])
    _, retrieved_ids = index.search(np.array(query_vector), k)
    return [documents[i] for i in retrieved_ids[0]]