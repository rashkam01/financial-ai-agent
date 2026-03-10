import numbers

from langchain_openai import ChatOpenAI
from typer.cli import docs
from src.retrieval.vector_store import load_vector_store
from src.utils.helpers import extract_monetary_values
from src.tools.financial_kpi_tools import calculate_growth

def ask_financial_agent(question):

    vector_db = load_vector_store()

    retriever = vector_db.as_retriever(search_kwargs={"k":3})

    docs = retriever.invoke(question)
    numbers = []

    for doc in docs:
        values = extract_monetary_values(doc.page_content)
        numbers.extend(values)

    numbers = sorted(numbers)

    previous_revenue = numbers[-2]
    current_revenue = numbers[-1]
    growth_percentage = calculate_growth(current_revenue, previous_revenue)
    context = ""

    for i, doc in enumerate(docs):
        context += f"\nSource {i+1}:\n{doc.page_content}\n"

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are a financial analyst.

Answer the question using only the provided context from financial reports.

If numbers are used, cite the source section.

Context:
{context}

Question:
{question}

Answer clearly and reference the source sections.
"""

    response = llm.invoke(prompt)

    return response.content