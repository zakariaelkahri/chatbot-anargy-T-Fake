from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

# from app.llm.tools import items, customers, sales_orders 
from app.core.config import settings



def local_model():
    llm = ChatOllama(
        model=settings.OLLAMA_MODEL,
        temperature=0,
        base_url=settings.OLLAMA_BASE_URL,
        num_ctx=settings.OLLAMA_NUM_CTX,
        num_predict=settings.OLLAMA_NUM_PREDICT,
    )
    return llm


def gemini_model():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        google_api_key="AIzaSyDDpopB1WtyIR0KjOxxzYfZhRSiticDJfg",
    )
    return llm

# llm = local_model()
# question = llm.invoke("What is the capital of France?")
# print(question.content)  # Output: "The capital of France is Paris."
