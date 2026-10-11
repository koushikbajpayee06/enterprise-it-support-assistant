# Enterprise IT Support Assistant

Enterprise IT Support Assistant is a full-stack document intelligence application designed to retrieve reliable information from internal IT documentation and gradually evolve into an AI-powered support copilot.

The current system extracts content from uploaded documents, splits it into searchable chunks, generates vector embeddings, stores them in ChromaDB, and performs semantic searches with configurable relevance filtering. Grounded RAG answers and support workflows are planned but have not yet been implemented.

## Project Status

🚧 Currently under active development.

The following features are currently working:

- React frontend connected with FastAPI
- PDF, TXT, and Markdown document uploads
- File type and size validation
- Local document storage with UUID-based filenames
- Text extraction from supported documents
- Recursive document chunking
- OpenAI embedding generation
- Persistent ChromaDB vector storage
- Duplicate-safe document indexing
- Semantic similarity search API
- React semantic-search interface
- Raw vector-distance reporting
- Configurable filtering of low-relevance results
- Empty-result handling for irrelevant queries
- Automated unit tests for retrieval filtering

The next milestone is grounded RAG answer generation. Retrieved chunks and their source, page, and chunk metadata will be provided to the OpenAI chat model so that generated answers can include precise citations.

## Features

### Implemented

- Upload PDF, TXT, and Markdown documents
- Validate uploaded file type and size
- Store uploaded documents locally
- Extract readable text from documents
- Split documents into overlapping chunks
- Generate embeddings using OpenAI
- Persist embeddings in ChromaDB
- Prevent duplicate chunk indexing using deterministic IDs
- Perform semantic similarity searches
- Return raw vector distances with search results
- Filter low-relevance results using a configurable maximum distance
- Return an empty result set when no relevant chunk is found
- Display upload and processing results in React
- Display semantic-search results in React
- Test retrieval filtering and empty-query behavior with pytest
- Expose REST APIs using FastAPI
- Provide interactive API documentation through Swagger UI
- Preserve PDF page numbers through chunking and indexing
- Display page-aware search citations in React
- Test PDF page extraction and metadata preservation with pytest
- Generate grounded answers using retrieved document chunks
- Add inline citation IDs to generated answers
- Return source, page, chunk, content, and distance for cited evidence
- Filter citations that were not used in the generated answer
- Skip the chat-model call when no relevant context is found
- Provide a React question-answering interface with expandable citations
- Test RAG context building, generation, fallback, and citation filtering

### Planned

- Orchestrate support workflows with LangGraph
- Store document metadata and persistent state in PostgreSQL
- Store conversation history in PostgreSQL
- Resume previous conversations
- Manage indexed documents
- Add authentication and authorization
- Add ticket lookup and draft creation
- Require human approval before ticket submission
- Stream generated responses
- Store production documents in AWS S3
- Expand retrieval evaluation, API, and integration tests
- Containerize and deploy the application

## Technology Stack

### Frontend

- React
- Vite
- JavaScript
- CSS
- Fetch API

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- Pydantic Settings

### AI and Retrieval

- LangChain
- OpenAI
- ChromaDB
- Retrieval-Augmented Generation
- LangGraph (planned)
- Recursive Character Text Splitter

### Document Processing

- PyPDF
- Pathlib
- LangChain Documents

### Storage

- ChromaDB for vector embeddings
- Local filesystem during development
- PostgreSQL for planned metadata, conversation history, and workflow state
- AWS S3 for planned production document storage

### Development Tools

- uv
- npm
- Git
- GitHub
- Swagger UI
- pytest

## High-Level Architecture

```text
End User
    │
    ▼
React Frontend
    │
    ▼
FastAPI Backend
    ├── Document Validation
    ├── Local Document Storage
    ├── Document Processing
    ├── OpenAI Embedding Model
    ├── ChromaDB Vector Store
    └── OpenAI Chat Model (RAG milestone)
```

## Document Ingestion Flow

```text
Document Upload
      │
      ▼
React Frontend
      │
      ▼
FastAPI Upload API
      │
      ▼
File Validation
      │
      ▼
Local Document Storage
      │
      ▼
Text Extraction
      │
      ▼
Recursive Text Chunking
      │
      ▼
OpenAI Embedding Generation
      │
      ▼
ChromaDB Vector Store
```

## Semantic Search Flow

```text
Search Query
      │
      ▼
FastAPI Semantic Search API
      │
      ▼
OpenAI Query Embedding
      │
      ▼
ChromaDB Similarity Search
      │
      ▼
Raw Vector Distances
      │
      ▼
Maximum-Distance Filter
      │
      ▼
Relevant Chunks or Empty Result
      │
      ▼
JSON Response with Sources and Distances
```

## Planned RAG Flow

```text
User Question
      │
      ▼
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
Load Conversation History
      │
      ▼
Semantic Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build RAG Prompt
      │
      ▼
OpenAI Chat Model
      │
      ▼
Answer with Sources
      │
      ▼
Save Conversation
      │
      ▼
React Frontend
```

## Project Structure

```text
enterprise-it-support-assistant/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       ├── documents.py
│   │   │       ├── health.py
│   │   │       └── search.py
│   │   │
│   │   ├── models/
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── document.py
│   │   │   └── search.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── document_service.py
│   │   │   ├── llm_service.py
│   │   │   ├── storage_service.py
│   │   │   └── vector_store.py
│   │   │
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_vector_store.py
│   ├── uploads/
│   │   └── .gitkeep
│   ├── vector_db/
│   │   └── .gitkeep
│   ├── .env.example
│   ├── .python-version
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── uv.lock
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── DocumentUpload.jsx
│   │   │   └── SemanticSearch.jsx
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── .env.example
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── docs/
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Make sure the following tools are installed:

- Python 3.10 or later
- uv
- Node.js
- npm
- Git

## Clone the Repository

Using HTTPS:

```bash
git clone https://github.com/koushikbajpayee06/enterprise-it-support-assistant.git
cd enterprise-it-support-assistant
```

Using SSH:

```bash
git clone git@github.com:koushikbajpayee06/enterprise-it-support-assistant.git
cd enterprise-it-support-assistant
```

## Backend Setup

### 1. Navigate to the Backend

```bash
cd backend
```

### 2. Install Dependencies

Using `uv`:

```bash
uv sync
```

Alternatively, create a standard Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Backend Environment Variables

Create `backend/.env` using `backend/.env.example` as a reference:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_TEMPERATURE=0

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_BUCKET_NAME=
AWS_REGION=ap-south-1

FRONTEND_URL=http://localhost:5173

UPLOAD_DIR=uploads
MAX_UPLOAD_SIZE_MB=10

CHROMA_PERSIST_DIR=vector_db
CHROMA_COLLECTION_NAME=documind_documents
MAX_SEARCH_DISTANCE=1.25
```

Never commit the `.env` file or expose real credentials publicly.

AWS configuration is optional during local development and will be required when S3 integration is implemented. PostgreSQL configuration will be added with the persistent-state milestone.

### 4. Start the FastAPI Server

From the `backend` directory:

```bash
uv run uvicorn app.main:app --reload
```

Backend links:

- API: http://127.0.0.1:8000
- Health check: http://127.0.0.1:8000/api/health
- Swagger UI: http://127.0.0.1:8000/docs

A successful health check returns HTTP `200` with a `healthy` status and an API availability message.

## Frontend Setup

### 1. Navigate to the Frontend

Open another terminal from the project root:

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Frontend Environment Variables

Create `frontend/.env` using `frontend/.env.example` as a reference:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### 4. Start the React Development Server

```bash
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

When both servers are running, the frontend displays the backend health status above the upload and search interfaces.

## Document Upload

Users can upload documents from the React interface.

Supported formats:

- PDF
- TXT
- Markdown

Maximum file size:

```text
10 MB
```

### Upload Endpoint

```http
POST /api/documents/upload
```

The request must use `multipart/form-data` with a field named `file`.

Example successful response:

```json
{
  "message": "Document uploaded, processed, and indexed successfully",
  "original_filename": "example.pdf",
  "stored_filename": "generated-uuid.pdf",
  "content_type": "application/pdf",
  "size_bytes": 587379,
  "character_count": 110399,
  "chunk_count": 138
}
```

During document upload, the backend:

1. Validates the file type and size.
2. Assigns a UUID-based stored filename.
3. Saves the document inside `backend/uploads/`.
4. Extracts readable text from the document.
5. Divides the text into overlapping chunks.
6. Generates embeddings for each chunk.
7. Stores the chunks and embeddings in ChromaDB.

## Semantic Search

The semantic search endpoint retrieves document chunks that are conceptually related to the provided query.

### Search Endpoint

```http
POST /api/search/semantic
```

Example request:

```json
{
  "query": "What are the benefits of APIs?",
  "number_of_results": 3
}
```

Example response:

```json
{
  "query": "What are the benefits of APIs?",
  "results": [
    {
      "content": "APIs enable different systems and applications to communicate...",
      "metadata": {
        "source": "Complete Notes.pdf",
        "chunk_index": 1,
        "document_id": "generated-deterministic-id"
      },
      "distance": 0.82
    }
  ]
}
```

The search endpoint returns chunks whose raw vector distance is less than or equal to the configured `MAX_SEARCH_DISTANCE`. A smaller distance indicates a closer semantic match. If no result passes the threshold, the endpoint returns an empty `results` list.

Answer generation using the retrieved context will be added in the RAG milestone.

## Duplicate-Safe Indexing

Enterprise IT Support Assistant generates deterministic identifiers for document chunks using their source, chunk index, and content.

This prevents the same chunk from being stored repeatedly when an identical document is uploaded more than once.

## Current Development Status

The application currently supports local document upload, document parsing and chunking, OpenAI embedding generation, persistent ChromaDB indexing, and semantic search through both FastAPI and React.

Search results include source, chunk, and raw vector-distance information. A configurable distance threshold removes low-relevance results, and automated unit tests verify the filtering behavior.

Page-level citations, generated RAG answers, LangGraph workflows, PostgreSQL persistence, authentication, ticket operations, human approval, streaming, and production deployment have not yet been implemented.

Generated RAG answers, LangGraph workflows, PostgreSQL persistence, authentication, ticket operations, human approval, streaming, and production deployment have not yet been implemented.

## Current Development Status

The application currently supports document upload, page-aware PDF ingestion, recursive chunking, OpenAI embeddings, persistent ChromaDB indexing, semantic retrieval, and grounded RAG answers through FastAPI and React.

Generated answers use retrieved document chunks as context and include inline citation IDs. Each cited source includes its filename, PDF page number when available, chunk index, supporting content, and vector distance. If no relevant context passes the retrieval threshold, the application returns a safe fallback response without calling the chat model.

Conversation history, LangGraph workflows, PostgreSQL persistence, authentication, ticket operations, human approval, streaming, and production deployment have not yet been implemented.

## Development Roadmap

- [x] Initialize Git repository
- [x] Set up Python environment with `uv`
- [x] Configure backend dependencies
- [x] Add environment configuration templates
- [x] Define the initial project architecture
- [x] Configure OpenAI chat and embedding models
- [x] Create the FastAPI application and health endpoint
- [x] Initialize the React frontend
- [x] Configure CORS
- [x] Connect React with FastAPI
- [x] Implement the document upload API
- [x] Build the React document-upload interface
- [x] Add file type and size validation
- [x] Add PDF, TXT, and Markdown parsing
- [x] Implement recursive document chunking
- [x] Generate document embeddings
- [x] Integrate persistent ChromaDB storage
- [x] Add duplicate-safe chunk indexing
- [x] Implement the semantic similarity search API
- [x] Build the React semantic-search interface
- [x] Return raw vector distances with search results
- [x] Add configurable retrieval-distance filtering
- [x] Handle searches with no relevant results
- [x] Add automated unit tests for retrieval filtering
- [x] Preserve PDF page numbers during ingestion
- [x] Preserve source and page metadata through chunking
- [x] Build the grounded RAG answer pipeline
- [x] Return generated answers with source and page citations
- [x] Skip the chat model when no relevant context is found
- [x] Filter unused citations from generated responses
- [x] Build the React RAG question-answering interface
- [x] Add automated tests for RAG services
- [ ] Build a history-aware RAG pipeline
- [ ] Add retrieval and RAG evaluation datasets and metrics
- [ ] Build a LangGraph support workflow
- [ ] Add PostgreSQL metadata, conversation history, and workflow state
- [ ] Add conversation resume functionality
- [ ] Add indexed-document management
- [ ] Add authentication and authorization
- [ ] Add ticket lookup and draft creation
- [ ] Require human approval before ticket submission
- [ ] Add streaming responses
- [ ] Integrate AWS S3
- [ ] Expand API and integration tests
- [ ] Improve error handling and structured logging
- [ ] Containerize the application with Docker
- [ ] Deploy the application to AWS

## Security

- Secrets are stored using environment variables.
- Sensitive values are handled using Pydantic `SecretStr`.
- Backend and frontend `.env` files are excluded from Git.
- Uploaded documents and local vector data are excluded from version control.
- Uploaded files are validated by extension and size.
- UUID-based stored filenames help prevent filename collisions.
- Production AWS credentials should use restricted IAM permissions.
- Raw documents and sensitive information should not be written to application logs.
- OpenAI and AWS credentials must never be committed to Git.

## Author

**Koushik Bajpayee**

- GitHub: [koushikbajpayee06](https://github.com/koushikbajpayee06)

## License

This project is currently intended for learning and portfolio purposes.
