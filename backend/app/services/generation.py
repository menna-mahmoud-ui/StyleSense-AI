import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class GenerationService:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.6-flash"
        )

    def generate(
        self,
        question: str,
        outfit_context: str,
        retrieved_sources: list,
    ):
        context = "\n\n".join(
            [
                f"Source {i + 1}:\n{source['content']}"
                for i, source in enumerate(retrieved_sources)
            ]
        )

        prompt = f"""
You are StyleSense AI, an AI fashion assistant.

Your task is to give practical and concise fashion recommendations.

Detected outfit:
{outfit_context}

User question:
{question}

Fashion knowledge retrieved from the RAG knowledge base:
{context}

Instructions:
- Answer based on the retrieved fashion knowledge.
- Use the detected outfit information when relevant.
- Do not invent fashion facts that are not supported by the retrieved context.
- If the retrieved knowledge is insufficient, clearly say that.
- Give a direct and useful answer.
- You can answer in Arabic if the user asks in Arabic.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are StyleSense AI, a helpful fashion recommendation assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content


generation_service = GenerationService()