# AI Workbench

A production-oriented AI backend built from first principles.

The goal of this project is **not** to learn frameworks first. Instead, it focuses on understanding the primitives behind modern AI applications—LLMs, structured outputs, tool calling, RAG, agents, and production AI systems—by implementing everything step by step.

> **Rule:** Learn the engineering primitives first. Frameworks become implementation details later.

---

# Roadmap Progress

```text
████████████░░░░░░░░░░░░░░░░░░ 35%

Phase 1  ██████████  Complete
Phase 2  ██████████  Complete
Phase 3  ████░░░░░░  In Progress
Phase 4  ░░░░░░░░░░  Pending
Phase 5  ░░░░░░░░░░  Pending
Phase 6  ░░░░░░░░░░  Pending
```

---

# Architecture

```text
                Client

                   │

                   ▼

             FastAPI Router

                   │

                   ▼

              Service Layer

                   │

                   ▼

             LLM Orchestrator

                   │

        ┌──────────┴──────────┐

        ▼                     ▼

     LLM Provider         Tool Registry

                               │

                               ▼

                    Python Tool Functions

                               │

                               ▼

                        Final Response
```

---

# Current Project Structure

```text
phase-3/

├── app/
│
├── api/
│     assistant.py
│     chat.py
│     summarize.py
│     extract.py
│     code.py
│     sql.py
│
├── core/
│     config.py
│
├── llm/
│     client.py
│     prompts/
│
├── schemas/
│     requests.py
│     responses.py
│     tools.py
│
├── services/
│     assistant.py
│     chat.py
│     summarizer.py
│     extractor.py
│     code.py
│     sql.py
│
├── tools/
│     calculator.py
│     registry.py
│     current_time.py
│     uuid.py
│
├── tests/
│
└── main.py
```

---

# Milestone 1 — LLM Engineering

## Objectives

* Learn how to communicate with LLM providers.
* Build a reusable FastAPI backend.
* Understand streaming and provider abstraction.

## Completed

* [x] FastAPI setup
* [x] Groq/OpenAI integration
* [x] Chat endpoint
* [x] Streaming responses
* [x] Health endpoint
* [x] Environment configuration
* [x] Model configuration
* [x] Provider abstraction

---

# Milestone 2 — Structured AI APIs

## Objectives

Build reliable AI APIs that return structured, validated outputs instead of unpredictable text.

```text
Input

↓

LLM

↓

JSON Mode

↓

Pydantic Validation

↓

API Response
```

## Completed

* [x] Router-based architecture
* [x] Service layer
* [x] Prompt library
* [x] JSON Mode
* [x] Structured Outputs
* [x] Pydantic Request Models
* [x] Pydantic Response Models
* [x] Summarizer endpoint
* [x] Information extraction endpoint
* [x] Code explanation endpoint
* [x] SQL generation endpoint
* [x] Separation of concerns

---

# Milestone 3 — Local Tool Calling (Current)

## Objective

Allow the LLM to invoke Python functions whenever additional computation or external capabilities are required.

```text
User

↓

LLM

↓

Tool Call

↓

Tool Registry

↓

Python Function

↓

Tool Result

↓

LLM

↓

Final Response
```

## Completed

### Assistant

* [x] Assistant service
* [x] Assistant endpoint
* [x] Assistant request model
* [x] Assistant response model

### Tool Calling

* [x] Local Tool Calling
* [x] Tool Schema
* [x] Tool Registry
* [x] Tool Execution
* [x] Function Calling
* [x] Calculator Tool

### Metadata

Every assistant response now returns:

* [x] Response
* [x] Provider
* [x] Model
* [x] Tools Used
* [x] Latency
* [x] Finish Reason

Example

```json
{
  "response": "...",
  "provider": "groq",
  "model": "openai/gpt-oss-120b",
  "tools_used": [
    "calculate"
  ],
  "latency_ms": 423,
  "finish_reason": "stop"
}
```

---

# Remaining — Milestone 3

## More Tools

* [X] Current Time
* [X] UUID Generator

---

## Agent Improvements

* [ ] Multi-tool execution loop (`while`)
* [ ] Multiple tool calls in one conversation
* [ ] Tool execution retries
* [ ] Unknown tool handling
* [ ] Invalid arguments handling
* [ ] Better exception handling

---

## Engineering

* [ ] Structured logging
* [ ] Request IDs
* [ ] Unit tests
* [ ] Integration tests
* [ ] Configuration cleanup
* [ ] Registry refactoring (`execute(tool_call)` owns all parsing)

---

## Stretch Goal — Streaming Tool Execution

Instead of waiting for the complete workflow, progressively stream the assistant's execution.

```text
User

↓

Thinking...

↓

Calling calculator...

↓

Done

↓

Generating response...

↓

Answer
```

This introduces:

* [ ] Streaming tool execution
* [ ] Server-Sent Events (SSE)
* [ ] Progressive UI updates
* [ ] Better UX for long-running tool calls

---

# Future Milestones

## Milestone 4 — Context & Memory

* [ ] Conversation memory
* [ ] Token budgeting
* [ ] Context window management
* [ ] Prompt assembly
* [ ] Token counting
* [ ] Cost estimation

---

## Milestone 5 — Retrieval & RAG

* [ ] PDF ingestion
* [ ] Chunking
* [ ] Embeddings
* [ ] Vector search
* [ ] Retrieval pipeline
* [ ] Citation support
* [ ] RAG evaluation

---

## Milestone 6 — Production Engineering

* [ ] Provider switching
* [ ] Observability
* [ ] Logging
* [ ] Retry strategies
* [ ] Benchmarks
* [ ] Docker
* [ ] Deployment
* [ ] CI/CD
* [ ] Performance optimization
* [ ] Production-ready architecture

---

# Engineering Principles

Throughout this project:

* Build primitives before frameworks.
* Separate API, business logic, and infrastructure.
* Keep services focused on orchestration.
* Keep tools focused on computation.
* Validate all machine-consumed outputs.
* Return consistent API contracts.
* Refactor after features work.
* Prefer simple architecture that evolves incrementally.

---

# Builder Mode

The objective is **not** to build another chatbot.

The objective is to build a reusable AI backend that progressively evolves into a production-grade AI platform.

Every milestone should leave the project in a working, shippable state before introducing additional complexity.
