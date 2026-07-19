# Milestone 3 — AI Assistant

> **Theme:** The model can now **do things**, not just **generate text**.

---

# Goal

Transform AI Workbench from an LLM-powered text generation API into an **AI Assistant** capable of reasoning, selecting tools, executing them, remembering conversations, and responding intelligently.

By the end of this milestone, the application should behave like a miniature ChatGPT with tool usage.

---

# Core Deliverable

```text
User

↓

Assistant API

↓

LLM

↓

Should I use a tool?

├── No
│     ↓
│  Respond
│
└── Yes
      ↓

Tool Registry

↓

Execute Tool

↓

Return Result

↓

LLM

↓

Final Response
```

---

# Engineering Goal

The biggest mental shift of this milestone:

```text
LLM decides

↓

Backend executes
```

The LLM never executes code.

It only decides **what should happen next**.

Your backend performs every action.

---

# New Concepts

## Function Calling

The model chooses which function should run.

Example:

* Calculator
* Current Time
* UUID Generator

---

## Tool Registry

Instead of checking

```python
if tool == ...
```

throughout the project,

create one place responsible for finding and executing tools.

---

## Conversation Memory

The assistant should remember previous messages instead of treating every request independently.

---

## Context Window

Understand that models have limited memory.

Learn how to:

* Store history
* Trim old messages
* Manage token budget

---

## Assistant Loop

Instead of

```text
Prompt

↓

LLM

↓

Response
```

we now have

```text
Prompt

↓

LLM

↓

Tool?

↓

Execute

↓

LLM

↓

Response
```

This becomes the foundation for RAG and Agents later.

---

# Architecture Evolution

Current

```text
app/

api/

core/

llm/

schemas/

services/
```

Target

```text
app/

api/

core/

llm/

memory/

schemas/

services/

tools/
```

---

# Folder Responsibilities

## tools/

Responsible for:

* Calculator
* Current Time
* UUID Generator
* Tool Registry
* Tool execution

Not responsible for:

* HTTP routes
* Prompt Engineering
* LLM communication

---

## memory/

Responsible for:

* Conversation history
* Token trimming
* Session state

Not responsible for:

* Tool execution
* Prompt templates

---

# Build Order

## Phase 3.1 — Tools

* [X] Create `tools/`
* [X] Create `calculator.py`
* [X] Create `current_time.py`
* [X] Create `uuid.py`
* [X] Create `registry.py`
* [X] Register all tools

Deliverable:

```text
Tool Name

↓

Registry

↓

Python Function
```

---

## Phase 3.2 — Function Calling

* [X] Learn Groq/OpenAI Function Calling API
* [X] Define tool schemas
* [X] Connect tool schemas to the model
* [X] Detect requested tool
* [X] Execute requested tool
* [X] Return tool output back to the model
* [X] Generate final response

Deliverable:

```text
User

↓

LLM

↓

Tool Call

↓

Backend

↓

Tool Result

↓

LLM

↓

Final Answer
```

---

## Phase 3.3 — Assistant Endpoint

* [X] Create `/assistant`
* [X] Create `AssistantRequest`
* [X] Create `AssistantResponse`
* [X] Create `assistant.py` service
* [X] Connect assistant with tool registry

Deliverable

```text
POST /assistant
```

---

## Phase 3.4 — Conversation Memory

* [ ] Create `memory/`
* [ ] Store conversation history
* [ ] Replay previous messages
* [ ] Keep latest context
* [ ] Trim old messages

Deliverable

Assistant remembers previous interactions.

---

Stretch Goal

```text
Thinking...

↓

Calling calculator...

↓

Done

↓

Answer...
```

---

## Phase 3.6 — Cleanup

* [ ] Refactor duplicated code
* [ ] Improve naming
* [ ] Update README
* [ ] Update tests
* [ ] Commit
* [ ] Tag release (`v0.3.0`)

---

# Suggested Folder Structure

```text
app/

├── api/
│   ├── assistant.py
│   ├── chat.py
│   ├── extract.py
│   └── summarize.py
│
├── core/
│
├── llm/
│
├── memory/
│   ├── history.py
│   └── manager.py
│
├── schemas/
│
├── services/
│   ├── assistant.py
│   ├── chat.py
│   ├── extractor.py
│   └── summarizer.py
│
├── tools/
│   ├── calculator.py
│   ├── current_time.py
│   ├── uuid.py
│   ├── registry.py
│   └── schemas.py
│
└── main.py
```

---

# Deliverables

By the end of Milestone 3:

* [X] Assistant endpoint
* [X] Tool registry
* [X] Calculator tool
* [X] Current time tool
* [X] UUID tool
* [X] Function calling
* [ ] Tests
* [ ] Documentation updated
* [ ] Conversation memory
* [ ] Context management

---

# Things We Are NOT Building

* [ ] LangChain
* [ ] LangGraph
* [ ] CrewAI
* [ ] AutoGen
* [ ] MCP
* [ ] Multi-agent systems
* [ ] RAG

Those concepts will be introduced after understanding the underlying primitives.

---

# Milestone Completion Criteria

You can ask questions like:

> What time is it?

> Calculate `(583 × 192) ÷ 7`

> Generate a UUID

The assistant should:

1. Decide whether a tool is needed.
2. Select the correct tool.
3. Execute it.
4. Feed the result back to the LLM.
5. Return a natural language response.

If all of those work while maintaining conversation history, Milestone 3 is complete and AI Workbench has evolved from an LLM API into a true AI Assistant.
