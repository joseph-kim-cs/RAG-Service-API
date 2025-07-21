# RAG Service API

A modular Retrieval-Augmented Generation (RAG) service powered by Milvus, watsonx.ai, and embedding-based pipelines. This API supports intelligent question answering and insight generation using structured and unstructured data.

## Project Structure

```
app/
├── .env                      # Environment variables (watsonx.ai keys, Milvus credentials, memory cache configs)
├── Dockerfile                # Docker container setup
├── requirements.txt          # Python package dependencies
├── README.md                 # Project overview and instructions
├── test/                     # Unit and integration tests
├── route/                    # API endpoints, error logging, environment validation
│   ├── ingest/               # Ingestion endpoint
│   └── query/                # Query endpoint (retrieval, reranking, rewriting)
|   └── root/                 # fastapi HTML response
├── src/
│   ├── model/                # Data models for ingestion, querying, errors, evaluation
│   └── services/             # Core pipeline services
│       ├── COSService        # Cloud Object Storage integration
│       ├── IngestionService  # Vector DB ingestion, collection schema
│       ├── QueryService      # Prompting, retrieval, LLM integration
│       └── EvaluationService # PII, relevance, governance SDK scoring
```

## Core Features

### Current Features
- Ingestion Pipeline with chunking & merging
- Embedding & Vector Store (Milvus)
- Retrieval
- Generation with prompt templates
- Prompt guardrails
- Evaluation metrics (e.g. relevance, PII)

### New Features (Planned)
- Multi-turn Q&A (Zep or custom cache layer)
- Memory layer integration (MemVerge or Redis)
- Question rewriting/enhancement
- Reranking (e.g., cross-encoder reranker)
- Hybrid vs Dense embeddings toggle
- Error logging with structured messages
- Offline environment support (optional LLM/embedding flexibility)

### Customization Options
- Swap or update embedding/LLM models
- Extend ingestion logic (chunking strategy, metadata schema)
- Prompt controls & rewrite templates
- Tune retrieval parameters (top-k, similarity metrics)
- Modular governance SDK support (watsonx-only or optional plugin)

## Setup Instructions

1. Clone the repository
   ```bash
   git clone <repo-url>
   cd rag-service-api
   ```

2. Set environment variables
   Create a `.env` file:
   ```
   WATSONX_API_KEY=your_key_here
   MILVUS_HOST=localhost
   MILVUS_PORT=19530
   USE_MEMORY_LAYER=True
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the service (locally)
   ```bash
   uvicorn app.main:app --reload
   ```

## Testing

Run tests using:
```bash
pytest test/
```
