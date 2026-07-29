I think this is the **last major structural refactor** you should do before you spend months building features.

After this, I would avoid moving folders around unless you're extracting a module. From this point onward, your effort should go into adding capabilities (ReAct, memory, RAG, frameworks), not reorganizing the repository.

## Guiding principle

The repository should answer three questions immediately:

1. **What is this?** → Root `README.md`
2. **How does it work?** → `docs/architecture.md` + the architecture image
3. **What version is this?** → Git tags + changelog

Everything else should support those.

---

# Final repository layout (the one I'd keep to v1.0)

```text
ai-workbench/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── llm/
│   ├── services/
│   ├── tools/
│   ├── memory/
│   │
│   ├── agents/            # v0.4+
│   ├── orchestration/     # v0.4+
│   ├── rag/               # v0.6+
│   ├── evaluation/        # v0.8+
│   ├── observability/     # v1.0
│   │
│   ├── schemas/
│   └── main.py
│
├── frameworks/
│   ├── langchain/
│   ├── langgraph/
│   ├── llamaindex/
│   └── pydanticai/
│
├── apps/
│   ├── document-chat/
│   ├── research-assistant/
│   ├── resume-reviewer/
│   └── sql-agent/
│
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── changelog.md
│   ├── decisions.md
│   └── images/
│       └── architecture-final.png
│
├── tests/
│
├── README.md
├── pyproject.toml
└── uv.lock
```

Notice something important:

There are **no `phase-*` folders**.

There are also **no `v0.3` folders**.

Versions belong in **Git**, not in the filesystem.

---

# Source of truth

You should have exactly one authoritative README.

```
README.md
```

This is what people see first.

It should contain:

* project overview
* architecture image
* key features
* version roadmap
* getting started
* links to documentation

Nothing else.

---

# Where the architecture image lives

I would store your final Excalidraw image here:

```
docs/

    images/

        architecture-final.png
```

Then in README:

```md
# Architecture

![Architecture](docs/images/architecture-final.png)
```

This becomes the first thing recruiters and contributors see.

---

# Documentation structure

Instead of `Plan.md`, `summary.md`, random notes, I'd formalize everything.

## README.md

External documentation.

Think:

> "What should someone understand in 3 minutes?"

---

## docs/architecture.md

Explain the architecture in depth.

Example sections:

```
Overview

Request Lifecycle

LLM Orchestrator

Tool Runtime

ReAct Loop

Memory

RAG

Observability

Deployment
```

---

## docs/roadmap.md

Future versions.

```
v0.3

v0.4

v0.5

...

v1.0
```

---

## docs/changelog.md

Human-readable releases.

```
v0.3

Added

Changed

Fixed
```

Much nicer than digging through commits.

---

## docs/decisions.md

This one is underrated.

Every important architectural decision goes here.

For example:

```
Why FastAPI?

Why Provider Abstraction?

Why Tool Registry?

Why LangGraph later?

Why not LangChain first?

Why ReAct?
```

Six months from now, you'll be glad you documented these choices.

---

# Where prompts go

I would eventually move them out of `llm/` into their own module.

```
app/

    prompts/

        system.md

        summarize.md

        extraction.md

        sql.md

        agent.md
```

Prompts become a first-class part of the system.

---

# Where framework implementations go

One of my favorite ideas for this repository is this:

```
frameworks/

    langchain/

        tool-calling/

        rag/

        memory/

    langgraph/

        react/

        planner/

    llamaindex/

        rag/

    pydanticai/

        agents/
```

Each directory answers:

> "How would I build the same capability with this framework?"

This keeps your first-principles implementation intact while showing practical ecosystem knowledge.

---

# Apps

This is what turns the project into a portfolio.

All of these should reuse the same backend:

```
apps/

    resume-reviewer

    document-chat

    sql-agent

    research-assistant
```

You're not building four AI systems.

You're proving your backend supports four different products.

---

# Versioning

Never create folders like

```
phase-4

phase-5
```

Instead:

```
v0.3.0

Tool Runtime

↓

v0.4.0

Agent Runtime

↓

v0.5.0

Memory

↓

v0.6.0

Knowledge

↓

v0.7.0

Framework Integrations

↓

v1.0.0

Production
```

Git tracks versions.

The filesystem tracks architecture.

---

# Repository philosophy

I would add a short section like this to the README:

> AI Workbench is developed using a **first-principles, versioned approach**. Core AI concepts are implemented manually before introducing framework integrations. Each release adds a new capability to the runtime while preserving previous implementations for educational comparison and architectural clarity.

That single paragraph explains why the repository contains both `app/` and `frameworks/`.

---

# The architecture image

The image you shared is **much closer to the right direction** than the earlier sketch because it shows the system as a platform rather than a collection of APIs.

For the final Excalidraw version, I'd make **one refinement**: treat it as a **layered engineering diagram**, not a component catalog.

The visual flow should read top to bottom:

```text
Clients
    │
    ▼
API Gateway (FastAPI)
    │
    ▼
Feature Layer
(Chat • Assistant • Structured APIs • RAG)
    │
    ▼
AI Runtime
(LLM Orchestrator • ReAct • Planning • Context Builder)
    │
    ├──────────────┬──────────────┬──────────────┐
    ▼              ▼              ▼              ▼
Providers      Tool Runtime     Memory      Knowledge
(OpenAI...)    (Registry)       (Redis)     (Vector DB)
    │              │              │              │
    └──────────────┴──────────────┴──────────────┘
                   ▼
        Observability & Deployment
```

Then use numbered callouts around it to explain concepts like:

1. Request lifecycle
2. Why multiple LLM providers?
3. What does the orchestrator do?
4. Why ReAct?
5. Why a tool registry?
6. How memory and RAG differ
7. Where frameworks fit
8. How the system becomes production-ready

That gives you a single "source of truth" diagram you can use in your README, presentations, interviews, and documentation without needing to redraw it as the project evolves.
