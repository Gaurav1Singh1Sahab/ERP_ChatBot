from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def build_rag_chain(llm, retriever):
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
Context:
{context}

Question:
{question}

Answer using only the above document information.
"""
    )

    return LLMChain(llm=llm, prompt=prompt, retriever=retriever)
