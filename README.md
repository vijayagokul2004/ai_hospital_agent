# Hospital AI Agent

An AI-powered hospital assistant designed to handle patient queries and assist with common hospital-related tasks using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), vector databases, and tool calling.

## Problem Statement

Hospital receptionists handle many repetitive tasks such as answering patient queries, providing hospital information, checking doctor availability, and assisting with appointment-related requests.

The goal of this project is to build an AI agent that can automate these interactions and provide users with relevant information from hospital-specific documents while also supporting action-based tasks through tools.

## Objectives

* Answer hospital-related user queries using trusted information.
* Retrieve relevant information from hospital documents.
* Reduce dependency on manual receptionist interactions for repetitive queries.
* Support task-based interactions such as appointment-related operations.
* Build an extensible AI agent architecture that can integrate additional tools in the future.

## Key Features

* Hospital-specific question answering
* Retrieval-Augmented Generation (RAG)
* Document ingestion and chunking
* Text embeddings
* Vector database-based semantic search
* Top-K relevant document retrieval
* LLM-based response generation
* Agent routing
* Tool calling for action-based requests
* FastAPI backend

## System Architecture

```text
User
  |
  v
AI Agent
  |
  v
Intent / Agent Router
  |
  +------------------------+
  |                        |
  v                        v
Information Query       Action Request
  |                        |
  v                        v
RAG Pipeline            Tool Calling
  |                        |
  v                        v
Embedding Model        Hospital Tools
  |                        |
  v                        v
Vector Database        Action / Operation
  |
  v
Top-K Relevant Chunks
  |
  v
LLM
  |
  v
Final Response
```

## RAG Pipeline

The RAG pipeline follows these steps:

1. Hospital documents are collected and loaded into the system.
2. Documents are split into smaller, meaningful chunks.
3. An embedding model converts each chunk into a numerical vector.
4. The embeddings are stored in a vector database.
5. When a user asks a question, the query is converted into an embedding.
6. The query embedding is compared with stored document embeddings using semantic similarity search.
7. The system retrieves the Top-K relevant chunks.
8. The retrieved chunks are provided to the LLM as context.
9. The LLM generates the final response based on the retrieved context.

## Agent and Tool Calling

The AI agent can distinguish between information-based queries and action-based requests.

For example:

### Information Query

```text
User:
"What time is Dr. Kumar available?"

        ↓

Agent Router

        ↓

RAG Retrieval

        ↓

Relevant Hospital Document

        ↓

LLM

        ↓

Response
```

### Action Request

```text
User:
"I want to book an appointment with Dr. Kumar."

        ↓

Agent Router

        ↓

Appointment Tool

        ↓

Appointment Operation

        ↓

Response to User
```

## Technology Stack

### Programming

* Python

### AI / ML

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Embedding Models
* Semantic Search

### Frameworks

* LangChain
* FastAPI

### Data / Retrieval

* Vector Database
* Document Processing
* Top-K Retrieval

### Development Tools

* VS Code
* Git
* GitHub
* Jupyter / Google Colab

## Project Structure

```text
ai_project_hospital/
│
├── app/
│   ├── agent/
│   │   ├── agent.py
│   │   ├── tools.py
│   │   └── prompts.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   ├── retriever.py
│   │   └── reranker.py
│   │
│   └── ...
│
├── scripts/
│   └── ingest.py
│
├── data/
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
```

## Example Queries

The system is designed to handle queries such as:

```text
"What time is Dr. Kumar available?"

"What services does the hospital provide?"

"What are the hospital visiting hours?"

"I want to book an appointment with Dr. Kumar."

"How can I contact the hospital?"
```

## Evaluation

The retrieval component can be evaluated using metrics such as:

* Recall@K
* Mean Reciprocal Rank (MRR)
* Context Relevance

The evaluation section will be updated with actual experimental results as the system is tested with a dedicated evaluation dataset.

## Future Improvements

* Hybrid retrieval using BM25 and vector search
* Reranking for improved retrieval quality
* RAG evaluation using a larger test dataset
* Improved agent routing
* Additional hospital tools
* Conversation memory
* Authentication and user management
* Production deployment
* Monitoring and logging
* Hallucination and response-quality evaluation

## Limitations

* The quality of responses depends on the quality and freshness of the provided hospital documents.
* The system should not be treated as a replacement for qualified medical professionals.
* Real-world deployment requires appropriate security, authentication, privacy, and validation mechanisms.
* Appointment and hospital operations require integration with actual hospital systems.

## Project Goal

The main goal of this project is to demonstrate how RAG, LLMs, vector databases, agent routing, and tool calling can be combined to build a practical AI assistant for hospital-related interactions.
