from fastapi import APIRouter, UploadFile, File, Query
from core.file_handler import extract_text_from_file
from core.faiss_index import add_to_index, search_index
from core.llm_utils import generate_summary
import os
import asyncio

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"data/uploads/{file.filename}"
    
    # Save file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text
    text = extract_text_from_file(file_path)
    add_to_index(text)
    
    return {"message": f"File {file.filename} uploaded & indexed!"}

@router.get("/search")
def search(query: str = Query(...)):
    results = search_index(query)
    return {"query": query, "results": results}

# @router.get("/ask")
# async def ask(query: str = Query(..., description="Ask a question")):
#     """API route for querying the LLM."""
#     retrieved_docs = [query]  # Simulated document retrieval for now

#     # Call generate_summary asynchronously
#     summary = await generate_summary(retrieved_docs)

#     return {"query": query, "summary": summary}

@router.get("/ask")
async def ask(query: str = Query(...)):
    """Handle queries with proper async execution."""
    summary = await generate_summary([query])
    return {"query": query, "summary": summary}