# from fastapi import FastAPI
# from sentence_transformers import SentenceTransformer
# import faiss
# import numpy as np

# # Initialize FastAPI app
# app = FastAPI()

# # Load embedding model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Sample documents
# documents = [
#     "Patient had high fever and cough.",
#     "Severe chest pain case reported.",
#     "Diabetes patient showing unusual symptoms.",
#     "Respiratory issues detected in elderly patients."
# ]

# # Convert documents into embeddings
# doc_vectors = model.encode(documents)

# # Set up FAISS index for vector search
# dimension = doc_vectors.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(np.array(doc_vectors))

# # Function to retrieve similar documents
# def retrieve_documents(query):
#     query_vector = model.encode([query])
#     _, retrieved_ids = index.search(np.array(query_vector), k=3)
#     return [documents[i] for i in retrieved_ids[0]]

# # API endpoint
# @app.get("/search")
# def search(query: str):
#     retrieved_docs = retrieve_documents(query)
#     return {"query": query, "results": retrieved_docs}

# # Run the API locally
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


from fastapi import FastAPI
from api.routes import router

app = FastAPI()

# Include all routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)