def get_kimi_k2_llm():
    from langchain_groq import ChatGroq
    return ChatGroq(
        model="moonshotai/kimi-k2-instruct",
        temperature=0.3,
        max_tokens=8000,
        api_key=GROQ_API_KEY,
        max_retries = 4,
    )

kimi_k2_llm = get_kimi_k2_llm()