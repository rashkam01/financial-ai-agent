# System Architecture

This document describes the architecture of the **Financial AI Agent**, a prototype agentic system designed to analyze company financial reports using **Retrieval Augmented Generation (RAG)** and **deterministic financial tools**.

The goal of the system is to provide **trustworthy financial analysis** grounded in company reports rather than hallucinated knowledge.

---

# High-Level Architecture

The system follows a **RAG + Tool pattern** commonly used in modern AI agent systems.

```
User Question
      │
      ▼
Financial Agent
      │
      ▼
Retriever
      │
      ▼
Vector Database (ChromaDB)
      │
      ▼
Financial Reports (PDF)
```

When financial calculations are required, the system uses deterministic Python tools.

```
Financial Agent
   │
   ├── LLM reasoning
   │
   └── Financial KPI Tools
        ├── revenue growth
        ├── margin analysis (future)
        └── financial ratios (future)
```

---

# Detailed System Pipeline

```
Financial Reports (PDF)
        │
        ▼
PDF Ingestion Pipeline
(src/ingestion)
        │
        ▼
Document Chunking
        │
        ▼
Embeddings (OpenAI)
        │
        ▼
Vector Database (ChromaDB)
(storage/vector_db)
        │
        ▼
Retriever
(src/retrieval)
        │
        ▼
Financial Agent
(src/agents)
        │
        ▼
Financial Tools
(src/tools)
        │
        ▼
LLM Explanation
```

---

# Component Overview

## 1. Data Layer

Location:

```
data/
```

This layer contains the raw financial reports used for analysis.

```
data/raw/
```

Example:

```
Qantas_2024.pdf
Qantas_2025.pdf
```

These reports serve as the **knowledge base** for the system.

---

# 2. Ingestion Layer

Location:

```
src/ingestion/
```

Responsible for:

* Loading PDF files
* Extracting text
* Splitting documents into smaller chunks

Main file:

```
pdf_ingestion.py
```

This uses:

* `PyPDFLoader`
* `RecursiveCharacterTextSplitter`

Chunking improves retrieval quality because LLMs cannot process very large documents efficiently.

---

# 3. Embedding Layer

Each document chunk is converted into a **vector embedding**.

Example concept:

```
"Total revenue was $23,823M"
```

becomes:

```
[0.34, -0.18, 0.77, ...]
```

These vectors represent **semantic meaning** rather than exact words.

Embeddings are generated using:

```
OpenAI Embeddings
```

---

# 4. Vector Database (ChromaDB)

Location:

```
storage/vector_db/
```

The vector database stores:

```
Document chunk
Embedding vector
Metadata
```

Example record:

```
Text:
"Total revenue for 2025 was $23,823M"

Embedding:
[0.21, -0.33, 0.77, ...]

Metadata:
source: Qantas_2025.pdf
page: 42
```

### Why a Vector Database?

Traditional databases search using keywords.

Vector databases search using **semantic similarity**.

Example query:

```
How much money did Qantas earn in 2025?
```

Even if the report uses the term **"total revenue"**, the vector database can still retrieve the correct section.

---

# 5. Retrieval Layer

Location:

```
src/retrieval/
```

The retriever performs **semantic search** against the vector database.

Workflow:

```
User question
      │
      ▼
Convert question → embedding
      │
      ▼
Vector similarity search
      │
      ▼
Top relevant document chunks returned
```

These chunks become **context for the LLM**.

---

# 6. Agent Layer

Location:

```
src/agents/
```

The financial agent orchestrates the system.

Responsibilities:

```
Retrieve relevant report sections
Extract financial numbers
Call financial tools
Generate explanations
```

The agent uses:

```
ChatOpenAI (GPT models)
```

The LLM focuses on **reasoning and explanation**, not deterministic calculations.

---

# 7. Financial Tool Layer

Location:

```
src/tools/
```

Financial tools provide deterministic calculations.

Example:

```
calculate_growth(current_value, previous_value)
```

Formula:

```
(current - previous) / previous × 100
```

Example calculation:

```
Revenue 2024 = 21,939
Revenue 2025 = 23,823

Growth = 8.59%
```

Using tools prevents **LLM math hallucinations**.

---

# 8. Utility Layer

Location:

```
src/utils/
```

Helper functions are stored here.

Example functionality:

```
Number extraction from financial text
Regex-based parsing of monetary values
```

Example extracted values:

```
21,939
23,823
1,884
```

These values are passed to financial tools.

---

# 9. Script Layer

Location:

```
scripts/
```

Scripts provide entry points for running the system.

### Ingestion Pipeline

```
run_ingestion.py
```

Builds the vector database from financial reports.

### Agent Execution

```
run_agent.py
```

Starts the financial analysis agent and allows users to ask questions.

---

# 10. Documentation Layer

Location:

```
docs/
```

Contains architecture and design documentation.

```
docs/architecture.md
```

This file explains the system design.

---

# Example End-to-End Query

Example question:

```
What is the revenue growth between 2024 and 2025?
```

System execution:

```
1. User asks question
2. Retriever searches ChromaDB
3. Relevant financial text retrieved
4. Numbers extracted from text
5. Financial tool calculates growth
6. LLM explains the result
```

Example result:

```
Revenue increased from $21,939M to $23,823M.

Using the formula:
(current - previous) / previous × 100

Revenue growth ≈ 8.59%.
```

---

# Current Capabilities

The system currently supports:

```
Document ingestion
Semantic search
Vector database retrieval
Financial KPI calculations
Grounded LLM explanations
```

---

# Future Improvements

Possible extensions include:

```
Segment revenue analysis
Profit margin calculations
Cash flow analysis
Structured table extraction
Multi-agent financial analysis
Automated data ingestion
Web dashboard
CI testing pipelines
```

---

# Summary

The system demonstrates how **agentic AI systems can combine LLM reasoning with deterministic financial tools** to produce trustworthy analysis.

Key architectural ideas:

```
Retrieval Augmented Generation (RAG)
Vector databases for semantic search
Deterministic tools for financial calculations
Modular architecture for scalability
```
