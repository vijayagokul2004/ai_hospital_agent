from langchain_ollama import ChatOllama

from .prompts import SYSTEM_PROMPT
from .tools import (
    get_hospital_timings,
    get_doctor_availability,
    book_token,
    cancel_token,
)


class HospitalAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="qwen3:4b",
            temperature=0
        )

        self.tools = {
            "get_hospital_timings": get_hospital_timings,
            "get_doctor_availability": get_doctor_availability,
            "book_token": book_token,
            "cancel_token": cancel_token,
        }

    def run(self, user_query, context=""):

        prompt = f"""
{SYSTEM_PROMPT}

Hospital information:
{context}

User:
{user_query}

Answer the user based on the available hospital information.
"""

        response = self.llm.invoke(prompt)

        return response.content
