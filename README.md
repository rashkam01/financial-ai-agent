# Financial AI Agent (RAG + Tools)

A prototype **Agentic AI system** that analyzes company financial reports using **Retrieval Augmented Generation (RAG)** and **deterministic financial tools**.

The system ingests annual reports (PDF), stores their semantic embeddings in a **vector database**, retrieves relevant financial information, and calculates key financial KPIs such as **revenue growth**.

The goal is to build a **trustworthy AI analyst** that answers financial questions using **grounded data from company reports**, not hallucinated information.

---

# Project Overview

This project demonstrates a minimal **Agent + Retrieval + Tool architecture**.

The agent can:

* Ingest financial reports (PDF)
* Store document embeddings in **ChromaDB**
* Retrieve relevant report sections
* Extract numerical values
* Calculate financial KPIs deterministically
* Generate grounded explanations using an LLM

Example query:

```
What is the revenue growth between 2024 and 2025?
```

Example output:

```
Revenue increased from $21,939M to $23,823M.

Using the formula:
(current - previous) / previous × 100

Revenue growth = 8.59%
```

---

# Architecture

The system follows a **RAG + Tool pattern** used in modern AI agents.

```
Financial Reports (PDF)
        ↓
PDF Ingestion
        ↓
Text Chunking
        ↓
Embeddings
        ↓
Vector Database (ChromaDB)
        ↓
Retriever
        ↓
Financial Agent
      /        \
LLM reasoning   Financial Tools
```

### Responsibilities

**Retriever**

* Searches financial reports
* Returns relevant document sections

**Tools**

* Perform deterministic calculations
* Prevent math hallucinations

**LLM**

* Interprets retrieved context
* Explains financial insights

---

# Repository Structure

```
financial-agent/
│
├── data/
│   └── raw/                 # Financial report PDFs
│   └── processed/           # Currently empty, if needed to stored some processed data
│
├── storage/
│   └── vector_db/           # Chroma vector database
│
├── src/
│   ├── agents/              # Financial agent logic
│   ├── ingestion/           # PDF ingestion pipeline
│   ├── retrieval/           # Vector database + retriever
│   ├── tools/               # Financial KPI tools
│   ├── utils/               # Helper functions
│   └── interfaces/          # UI layer 
│   ├── config/              # configuration files
│   └── workflows/           # RAG pipelines
│
├── scripts/
│   ├── run_ingestion.py     # Build vector database
│   └── run_agent.py         # Ask questions
│
├── docs/
│   ├── architechture.md     # Architecture diagram 
│
├── notebooks/
│   ├── exploration.ipynb     # For experiments
│
├── .gitignore               # Add the storage/vector_db, venv, cache etc. 
├── requirements.txt
├── .env.example             # copy and replace with .env and API_KEYS
└── README.md

```

---

# Technologies Used

| Component       | Technology        |
| --------------- | ----------------- |
| LLM             | OpenAI GPT models |
| Framework       | LangChain         |
| Vector Database | ChromaDB          |
| Embeddings      | OpenAI embeddings |
| Language        | Python            |

---

# How ChromaDB Works

ChromaDB stores **vector embeddings of document chunks**.

Each stored record contains:

```
Text chunk
Embedding vector
Metadata
```

Example:

```
Text:
"Total revenue for 2025 was $23,823M"

Embedding:
[0.21, -0.13, 0.55, ...]

Metadata:
source: Qantas_2025.pdf
page: 45
```

When a user asks a question, the system:

1. Converts the question into an embedding
2. Finds the **most similar vectors**
3. Returns the most relevant document chunks

This enables **semantic search** rather than keyword search.

---

# Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/rashkam01/financial-ai-agent.git
cd financial-ai-agent
```

---

## 2. Create a Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

# Ingest Financial Reports

Place PDFs in:

```
data/raw/
```

Then run:

```
python scripts/run_ingestion.py
```

This will:

* read PDFs
* split text into chunks
* create embeddings
* store them in ChromaDB

The vector database will be saved in:

```
storage/vector_db/
```

---

# Run the Financial Agent

Start the agent:

```
python scripts/run_agent.py
```

Example query:

```
What is the revenue growth between 2024 and 2025?
```

---

# Financial Tools

The system uses deterministic Python tools to calculate KPIs.

Example tool:

```python
def calculate_growth(current, previous):
    return (current - previous) / previous * 100
```

This prevents LLM hallucination in financial calculations.

---

# Example Agent Workflow

```
User Question
      ↓
Retriever searches ChromaDB
      ↓
Relevant report sections returned
      ↓
Numbers extracted
      ↓
Financial tool calculates KPI
      ↓
LLM generates explanation
```

---

# Current Capabilities

✔ Document ingestion
✔ Vector database search
✔ Semantic retrieval
✔ Revenue growth calculation
✔ Grounded financial explanations

---

# Future Improvements

Possible next steps:

* Segment revenue analysis
* Profit margin calculations
* Cashflow analysis
* Multi-agent financial analysis
* Table extraction from financial statements
* Automated report ingestion
* Web UI dashboard
* CI pipeline for testing

---

# License

MIT License
