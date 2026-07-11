# AI Workbench - Phase 1

A FastAPI-based backend application that integrates with LLM providers (OpenAI/Groq) to power a chat interface.

## Project Structure

```
ai-workbench/
├── app/
│   └── main.py
├── .env
├── pyproject.toml
└── README.md
```

## Getting Started

### Phase 1: Project Setup
- [X] Create project folder structure
- [X] Create Python virtual environment
- [X] Install FastAPI framework
- [X] Install OpenAI SDK
- [X] Install uvicorn (ASGI server)
- [X] Create `.env` configuration file
- [X] Add LLM provider API key to `.env`
- [X] Start FastAPI development server

### Phase 2: Backend Implementation
- [X] Create `/chat` POST endpoint
- [X] Implement JSON body parsing
- [X] Extract `message` field from request
- [X] Call LLM provider (OpenAI or Groq)
- [X] Return model response to client
- [X] Test endpoint in Swagger UI (`/docs`)
- [X] Test endpoint using Postman or Bruno REST client

### Phase 3: Verification & Understanding
Answer these questions without external references:
- [X] Explain what the backend service does
- [X] Explain what the LLM provider role is
- [X] Explain why the API key is required
- [X] Identify where the actual LLM computation happens
- [X] Trace the complete flow from user sending a message to receiving a response

### Phase 4: Stretch Goals (Optional)
Implement these features if you complete the core tasks early:
- [X] Add `/health` endpoint for service status checks
- [X] Include model name in the API response
- [X] Make LLM model selection configurable via `.env` (instead of hardcoding)

## Key Concepts to Understand

- **FastAPI**: Modern Python web framework for building APIs
- **LLM Provider**: External service (OpenAI/Groq) that processes natural language
- **API Key**: Authentication credential for accessing the LLM provider's services
- **ASGI**: Asynchronous Server Gateway Interface for handling requests
- **Endpoint**: A specific URL path that performs a particular action
