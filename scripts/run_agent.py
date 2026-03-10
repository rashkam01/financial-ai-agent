import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.financial_agent import ask_financial_agent


def run():

    question = input("Ask a financial question: ")

    answer = ask_financial_agent(question)

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    run()