# Architectural Decisions

## ADR-001: Why FastAPI?

### Context
Building a modern AI backend requires asynchronous execution for high-concurrency LLM response streaming, strict schema validation for structured outputs and function calling payloads, and automated standards-compliant API documentation.

### Decision
Use FastAPI as the primary web framework for the application.

### Consequences
- Native `async`/`await` support enables non-blocking response streaming and concurrent IO operations.
- Deep integration with Pydantic handles request validation and automatic JSON schema generation for tool parameters.
- Automatic OpenAPI documentation (`/docs` and `/redoc`) simplifies API contract inspection and integration testing.
- High compatibility with the broader Python AI/ML ecosystem.

---

## ADR-002: Why Provider Abstraction?

### Context
The LLM provider ecosystem changes rapidly. Direct coupling of vendor-specific SDK calls within application routes creates tight coupling, complicates testing, and hinders provider swapping or fallback routing.

### Decision
Isolate all LLM provider interactions behind a client interface layer (`app/llm/client.py`).

### Consequences
- Application service logic depends on a unified internal interface rather than vendor-specific SDKs.
- Groq is configured as the initial primary provider, but substituting or adding OpenAI, Anthropic, or local endpoints requires zero changes to business logic or route handlers.
- Mocking model responses for unit and integration tests is streamlined and independent of live network connections.

---

## ADR-003: Why a Tool Registry?

### Context
As an AI agent expands its capabilities, managing available tools using procedural `if/else` control flow or hardcoded dispatch routines becomes unmaintainable and resistant to dynamic execution.

### Decision
Implement a central `ToolRegistry` that explicitly registers tool functions, parameter schemas, and metadata by name.

### Consequences
- Decouples tool definition and execution from the assistant orchestration loop.
- Automatically generates tool JSON schemas required for LLM function calling.
- Enables dynamic runtime tool discovery, parameter validation, and execution by tool name.
- Modular tool addition without modifying core API endpoints or assistant execution logic.

---

## ADR-004: Why First-Principles Before Frameworks?

### Context
High-level AI frameworks abstract key operational mechanics—such as prompt formatting, tool invocation parsing, state management, context window constraints, and retry loops—behind opaque abstractions.

### Decision
Build core backend capabilities (LLM client, prompt templates, tool registry, function calling loops) manually using standard Python primitives before integrating external orchestration frameworks.

### Consequences
- Establishes a complete, low-level understanding of fundamental agent and LLM mechanics.
- Prevents opaque framework behavior, unexpected state mutations, and unhandled library failures.
- Provides a clear baseline for measuring performance, latency, and resource overhead.

---

## ADR-005: Why LangGraph Later?

### Context
Stateful agent workflows, graph execution loops, and durable state management introduce structural complexity. Adopting framework graph mechanisms before establishing basic loop mechanics obscures fundamental runtime behavior.

### Decision
Defer LangGraph integration until v0.7+, introducing it after a custom manual ReAct loop and state management primitives exist in the codebase.

### Consequences
- Allows direct architectural and performance comparison between custom implementations and framework implementations.
- Provides concrete, empirical understanding of LangGraph trade-offs including execution overhead, state graph semantics, and code complexity.
- Keeps early versions (v0.1–v0.6) focused on fundamental AI engineering concepts.

---

## ADR-006: Why Not LangChain First?

### Context
LangChain provides high-level abstractions for chains, memory, tools, and prompts. However, relying on LangChain initially obscures low-level mechanics like raw message payload formatting, manual function call parsing, and context window pruning.

### Decision
Avoid using LangChain in initial application releases (v0.1–v0.6) and implement all core components from scratch.

### Consequences
- Eliminates dependency bloat, dynamic class magic, and breaking API changes during foundational development.
- Forces direct interaction with raw LLM responses, structured Pydantic models, and JSON function calling specifications.
- Enables clear positioning of framework implementations in `frameworks/` for comparative benchmarking in v0.7+.

---

## ADR-007: Why ReAct?

### Context
Autonomous AI agents require an execution framework that interleaves explicit reasoning (thought formulation) with external action (tool execution and observation ingestion) to solve complex multi-step tasks.

### Decision
Adopt the ReAct (Reason + Act) pattern as the core architecture for agent execution.

### Consequences
- Provides a structured, deterministic execution flow: Thought → Action → Observation → Final Answer.
- Enhances system observability and debuggability by exposing intermediate reasoning steps.
- Building the ReAct loop manually guarantees total control over execution step limits, loop termination conditions, and error handling.

---

## ADR-008: Why Prompts as First-Class Citizens?

### Context
Hardcoding system prompts as inline strings across Python service modules scatters prompt logic, complicates prompt iteration, and obscures system instructions from version control tracking.

### Decision
Manage system prompts as standalone Markdown files within `app/prompts/`, loading and rendering them at runtime.

### Consequences
- Decouples prompt engineering and instruction design from application code.
- Supports clean variable substitution into Markdown templates without modifying Python logic.
- Enables version-controlled prompt management, visual diffing across commits, and structured prompt iteration.
