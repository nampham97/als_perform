from groq import Groq
import os
from dotenv import load_dotenv

def create_client() -> Groq:
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    return Groq(
        api_key=GROQ_API_KEY,
    )


if __name__ == "__main__":
    pass