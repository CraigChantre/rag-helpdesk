# RAG Helpdesk Assistant

A container-ready Retrieval-Augmented Generation (RAG) system that answers IT helpdesk questions using a local LLM, document retrieval, and a FastAPI backend.

---

## Overview

This project simulates an internal IT helpdesk assistant that can answer common technical issues (e.g., VPN failures, password resets) by retrieving relevant documentation and generating grounded responses through passing in context during runtime. 

The system uses:
- TF-IDF-based document retrieval
- A locally hosted LLM via Ollama
- A FastAPI backend for serving requests

---

## Architecture
User Query → FastAPI (/query) → Retriever (TF-IDF) → Context → LLM (Ollama) → Answer + Sources


## Features

- Retrieval-Augmented Generation (RAG)
- Local LLM inference (no external API required)
- FastAPI backend with auto-generated docs
- Relevance filtering (removes low-score results)
- Source attribution for answers
- Clean modular architecture (retrieval, generation, services)

---

## Example

### Input

```json
{
  "query": "vpn not working"
}
```
### Output

```json
{
  "query": "vpn not working",
  "answer": "1. Check that your internet connection is working.\n2. Verify your username and password...\n...",
  "sources": ["VPN Troubleshooting"]
}
```

## Features
- Retrieval-Augmented Generation (RAG)
- Local LLM inference (no external API required)
- FastAPI backend with interactive API docs
- Relevance filtering to remove low-confidence results
- Source attribution for generated answers
- Modular architecture (retrieval, generation, services)


## Setup

### 1. Clone the repository

```bash
git clone https://github.com/CraigChantre/rag-helpdesk.git
cd rag-helpdesk
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Download from https://ollama.com/download

Then run:
```bash
ollama run llama3.1:8b
```

Replace model with whatever is suitable for your hardware. 


### 5. Start the backend API
```bash
uvicorn app.main:app --reload
```

### 6. Test the API 

Open http://127.0.0.1:8000/docs

and use the /query endpoint to send requests 


## Future Improvements

- Document chunking for more precise retrieval
- Embedding-based vector search (FAISS / Chroma)
- Docker-based deployment
- Streaming responses from the LLM
- Frontend UI for chat interaction


## Author

Craig Chantre-Rivera  
UC San Diego — Cognitive Science (Machine Learning)