from dotenv import load_dotenv
import os
load_dotenv()
def get_kimi_k2_llm():
    from langchain_groq import ChatGroq
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    return ChatGroq(
        model="moonshotai/kimi-k2-instruct",
        temperature=0.3,
        max_tokens=8000,
        api_key=GROQ_API_KEY,
        max_retries = 4,
    )

kimi_k2_llm = get_kimi_k2_llm()


def get_openai_llm():
    from langchain_openai import OpenAI, ChatOpenAI
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    return ChatOpenAI(
        model="o3-mini",
        max_tokens=8000,
        openai_api_key=OPENAI_KEY,
        max_retries = 4,
    )

gpt_4o_llm = get_openai_llm()