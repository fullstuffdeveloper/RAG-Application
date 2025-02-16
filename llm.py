# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# test_text = "Software requirements specification is an important document in the software development lifecycle. It outlines the functional and non-functional requirements for a system."

# print(summarizer(test_text, max_length=100, truncation=True))


# from core.llm_utils import generate_summary

# test_docs = ["Software requirements specification is an important document in the software development lifecycle. It outlines the functional and non-functional requirements for a system."]

# print(generate_summary(test_docs))

import asyncio
from core.llm_utils import generate_summary

test_docs = ["Software requirements specification is an important document in the software development lifecycle. It outlines the functional and non-functional requirements for a system."]

async def main():
    summary = await generate_summary(test_docs)
    print(summary)

asyncio.run(main())