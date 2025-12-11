from langchain_ollama import Ollama

def init_llm(model_name: str):
    return Ollama(model=model_name)
