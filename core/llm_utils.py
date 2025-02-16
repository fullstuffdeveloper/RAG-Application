# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def generate_summary(docs):
#     """Summarize retrieved documents."""
#     input_text = " ".join(docs)
#     summary = summarizer(input_text, max_length=100, truncation=True)
#     return summary[0]['summary_text']

def generate_summary(docs):
    """Temporary function to test if LLM is the issue."""
    return "Dummy summary"

# from transformers import pipeline


# # Load Summarization Model with CPU mode
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

# def generate_summary(docs):
#     """Summarize retrieved documents using BART."""
#     input_text = " ".join(docs)[:1024]  # Limit text size
#     summary = summarizer(input_text, max_length=150, min_length=30, truncation=True)
#     return summary[0]['summary_text']


# # Load Summarization Model with CPU mode
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

# def generate_summary(docs):
#     """Summarize retrieved documents using BART."""
#     input_text = " ".join(docs)[:1024]  # Limit text size
#     summary = summarizer(input_text, max_length=150, min_length=30, truncation=True)
#     return summary[0]['summary_text']

# from transformers import pipeline

# # Load Summarization Model (forcing CPU for stability)
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

# def generate_summary(docs):
#     """Summarize retrieved documents using BART with correct truncation."""
#     input_text = " ".join(docs)
    
#     # Ensure the max_length does not exceed input length
#     max_length = min(len(input_text.split()) * 2, 100)  # Ensuring sensible truncation
    
#     summary = summarizer(input_text, max_length=max_length, min_length=30, truncation=True)
    
#     return summary[0]['summary_text']


# from transformers import pipeline
# import asyncio

# Load Summarization Model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

# async def generate_summary(docs):
#     """Asynchronous summarization using BART."""
#     input_text = " ".join(docs)
#     max_length = min(len(input_text.split()) * 2, 100)  # Ensuring correct truncation

#     loop = asyncio.get_running_loop()
#     summary = await loop.run_in_executor(None, lambda: summarizer(input_text, max_length=max_length, min_length=30, truncation=True))

#     return summary[0]['summary_text']


# from transformers import pipeline
# import asyncio

# Load Summarization Model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

# async def generate_summary(docs):
#     """Asynchronous summarization using BART."""
#     input_text = " ".join(docs)
#     max_length = min(len(input_text.split()) * 2, 100)  # Ensuring correct truncation

#     loop = asyncio.get_running_loop()
#     summary = await loop.run_in_executor(None, lambda: summarizer(input_text, max_length=max_length, min_length=30, truncation=True))

#     return summary[0]['summary_text']


# from transformers import pipeline
# import asyncio

# # Load Summarization Model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)  # -1 for CPU, change to 0 if using GPU

# async def generate_summary(docs):
#     """Asynchronous summarization using BART."""
#     input_text = " ".join(docs)
    
#     # Ensure proper truncation
#     max_length = min(len(input_text.split()) * 2, 100)  
#     min_length = max(30, max_length // 3)  # Set min_length for better output

#     loop = asyncio.get_running_loop()
#     summary = await loop.run_in_executor(None, lambda: summarizer(input_text, max_length=max_length, min_length=min_length, truncation=True))

#     return summary[0]['summary_text']


# from transformers import pipeline
# import asyncio

# # Load Summarization Model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)  # CPU (-1) or GPU (0)

# def generate_summary_sync(docs):
#     """Synchronous summarization function"""
#     input_text = " ".join(docs)

#     # Ensure proper truncation
#     max_length = min(len(input_text.split()) * 2, 100)
#     min_length = max(30, max_length // 3)

#     return summarizer(input_text, max_length=max_length, min_length=min_length, truncation=True)[0]['summary_text']

# async def generate_summary(docs):
#     """Asynchronous wrapper for LLM inference"""
#     loop = asyncio.get_event_loop()
#     return await loop.run_in_executor(None, generate_summary_sync, docs)