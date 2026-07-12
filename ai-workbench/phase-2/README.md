# AI Workbench

> Build production-grade LLM applications from first principles.
>
> **No LangChain. No LlamaIndex. No AI frameworks.**
>
> The goal isn't to learn a framework—it's to understand how modern AI applications are engineered.

---

# Vision

AI Workbench is a progressive backend project that evolves from a simple LLM API into a production-style AI platform.

Instead of building ten unrelated demo projects, the same codebase grows milestone by milestone, introducing new engineering concepts only when the project naturally requires them.

Every abstraction must be **earned**, not copied from tutorials.

---

# Learning Philosophy

This repository follows one principle.

```text
Understand

↓

Design

↓

Sketch

↓

Build

↓

Test

↓

Refactor

↓

Commit
```

The objective is to think like an engineer.

Every milestone answers three questions:

* **Why are we building this?**
* **What engineering problem does it solve?**
* **Why does the architecture need to evolve?**

---

# Current Progress

## ✅ Milestone 1 — Talk to an LLM

### Deliverables

* Chat endpoint
* Streaming endpoint
* Health endpoint
* Configuration management
* Provider abstraction (basic)
* Swagger integration

### Concepts Learned

* FastAPI
* REST APIs
* LLM Providers
* API Keys
* Streaming
* Request lifecycle
* Basic project structure

---

## 🚧 Milestone 2 — Reliable AI Responses

Current milestone.

Goal:

Transform the backend from "text generation" into a reliable AI service.

New endpoints:

```text
POST /summarize

POST /extract-json

POST /code-explain

POST /generate-sql
```

Every endpoint should return predictable, validated JSON.

Concepts introduced:

* Structured Outputs
* JSON Mode
* Prompt Engineering
* Prompt Library
* Pydantic Response Models
* Output Validation
* Error Handling

---

# Engineering Roadmap

```text
Milestone 1

Talk to an LLM
        │
        ▼
Milestone 2

Reliable AI Responses
        │
        ▼
Milestone 3

AI Assistant
(Function Calling + Memory)
        │
        ▼
Milestone 4

Practical AI Utilities
(Resume Review, SQL, Code Review)
        │
        ▼
Milestone 5

LLM Engineering Toolkit
(Token Counting, Cost, Benchmarking)
        │
        ▼
Milestone 6

Production Backend
(Docker, CI, Testing, Deployment, Monitoring)
        │
        ▼
Stage 2

RAG

        │
        ▼
Stage 3

Agents
```

---

# Current Architecture

```text
                Client

                   │

            HTTP Request

                   │

               FastAPI

                   │

               API Router

                   │

           Business Logic

                   │

             LLM Provider

                   │

          Structured Response

                   │

             HTTP Response
```

The architecture should evolve only when the project earns new abstractions.

---

# Architecture Evolution

## Milestone 1

```text
app/

main.py

chat.py

schemas.py

config.py
```

Reason:

One feature.

One endpoint.

No unnecessary abstractions.

---

## Milestone 2 (Target)

```text
app/

├── api/

├── llm/

├── schemas/

├── main.py
```

Reason:

The application now exposes multiple AI capabilities.

Responsibilities become clearer.

### api/

Responsible for:

* HTTP routes
* Request validation
* Calling business logic

Not responsible for:

* Prompt engineering
* LLM communication
* Business rules

---

### llm/

Responsible for:

* Provider initialization
* Shared client configuration
* Provider switching

Not responsible for:

* Prompt construction
* Feature-specific logic

---

### schemas/

Responsible for:

* Request models
* Response models
* API contracts

Not responsible for:

* Business logic

---

## Future Evolution

The following folders are intentionally **not** created yet.

```text
services/

prompts/

uploads/

memory/

tools/

providers/
```

These will only be introduced when the codebase naturally demands them.

No abstraction is created before there's a real engineering reason.

---

# Folder Evolution Philosophy

A new folder must answer three questions.

```text
What problem exists?

↓

Why can't the current structure handle it?

↓

How does this folder solve it?
```

If these questions cannot be answered, the folder should not exist.

---

# Development Workflow

Every new feature follows the same engineering process.

```text
Feature Idea

↓

Understand the problem

↓

Draw the architecture

↓

Design request flow

↓

Implement

↓

Test

↓

Refactor

↓

Commit
```

---

# Definition of Done (Milestone 2)

* [ ] Introduce `api/` using `APIRouter`
* [ ] Move provider initialization into `llm/`
* [ ] Implement `/summarize`
* [ ] Implement `/extract-json`
* [ ] Implement `/code-explain`
* [ ] Implement `/generate-sql`
* [ ] Return validated Pydantic responses
* [ ] Create initial prompt library
* [ ] Improve error handling
* [ ] Update tests
* [ ] Refactor only when duplication appears

---

# Engineering Rules

* Build first. Abstract later.
* Every folder must have one responsibility.
* Never introduce architecture because a tutorial does.
* Prefer duplication over premature abstraction.
* Refactor only after patterns become obvious.
* Keep `main.py` as the application's entry point—not its brain.
* Every commit should leave the project in a working state.

---

# Tech Stack

* Python 3.12+
* FastAPI
* Pydantic
* Groq SDK
* OpenAI SDK
* httpx
* uv
* python-dotenv
* tiktoken (Milestone 5)

---

# Long-Term Goal

By the end of this repository, you'll understand the engineering primitives behind modern AI systems:

* LLM APIs
* Structured Outputs
* Function Calling
* Streaming
* Context Windows
* Prompt Engineering
* Provider Abstractions
* Production Backend Design
* RAG
* Agentic Systems

The objective is not to become a LangChain developer.

The objective is to become the kind of engineer who could build the abstractions that frameworks provide.

