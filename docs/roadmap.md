# Roadmap

## v0.3.0 — Tool Runtime (Current)
Tool registry, function calling, assistant endpoint, prompt management.

- Dynamic tool registration system with JSON schema auto-generation.
- Native function calling integration using Groq API (`llama-3.3-70b-versatile`).
- Built-in utility tools: arithmetic calculator, ISO timestamp retrieval, and UUID v4 generator.
- Multi-turn assistant API endpoint (`POST /assistant`) supporting automatic tool invocation loops.
- File-based prompt management system (`app/prompts/`) supporting Markdown templates with variable substitution.

## v0.4.0 — Agent Runtime
ReAct loop, multi-step reasoning, conversation memory, context window management.

- Explicit ReAct (Reasoning + Acting) execution loop with intermediate step inspection.
- Multi-step tool orchestration with configurable maximum step limits and termination rules.
- In-memory conversation state tracking across message turns and tool calls.
- Context window management including truncation and sliding-window strategies.
- Structured response schemas emitting reasoning thoughts, tool execution logs, and final answers.

## v0.5.0 — Memory & State
Persistent conversation memory (Redis), session management, token budget optimization.

- Redis backend integration for persistent session and conversation history storage.
- Session lifecycle management API (creation, retrieval, expiration, and deletion).
- Token usage tracking and accounting per request, session, and client.
- Automated conversation history summarization for long-context compression.
- Token budget enforcement and sliding window strategies to constrain API cost.

## v0.6.0 — Knowledge (RAG)
Vector database integration, document ingestion, retrieval-augmented generation.

- Vector database integration (ChromaDB / Qdrant) with embedding generation pipeline.
- Document ingestion pipeline supporting Markdown, PDF, and text file chunking.
- Semantic search and hybrid keyword retrieval engine with similarity scoring.
- RAG query pipeline (`POST /rag/query`) combining contextual retrieval with synthesis.
- Citation tracking and source provenance attribution in generated responses.

## v0.7.0 — Framework Integrations
LangChain, LangGraph, LlamaIndex, PydanticAI implementations for comparison.

- Reference implementations in `frameworks/` comparing third-party agent frameworks.
- LangChain and LangGraph stateful agent and DAG workflow implementations.
- LlamaIndex query engine and document indexing integration.
- PydanticAI type-safe agent and structured output implementation.
- Architectural benchmark comparing execution latency, memory footprint, and framework overhead.

## v0.8.0 — Evaluation
LLM output evaluation, test harness, benchmarking.

- Automated test harness for evaluating model outputs against ground truth datasets.
- LLM-as-a-judge evaluation pipelines with customized scoring rubrics.
- Metrics pipeline covering exact match, semantic similarity, and factual consistency.
- Regression testing suite for prompt updates and tool invocation safety.
- Benchmark reporting tool generating performance and accuracy metrics.

## v0.9.0 — Portfolio Apps
Document chat, research assistant, resume reviewer, SQL agent — all reusing the same backend.

- Standalone applications in `apps/` demonstrating backend architecture reuse.
- Document Chat application utilizing RAG context retrieval and file processing.
- Research Assistant application orchestrating web search, tool use, and report synthesis.
- Resume Reviewer application utilizing structured JSON output and targeted feedback.
- SQL Agent application featuring database schema inspection and safe query execution.

## v1.0.0 — Production
Observability, structured logging, deployment, monitoring, rate limiting.

- OpenTelemetry tracing and structured JSON logging across application pipelines.
- Prometheus metrics exporter for latency, token counts, error rates, and active sessions.
- Token bucket rate limiting and client API key throttling middleware.
- Containerized deployment configuration with multi-stage Dockerfiles and deployment manifests.
- Security controls including input sanitization, secret management, and CORS policy enforcement.
