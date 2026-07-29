# Changelog

All notable changes to AI Workbench are documented here.
This project follows [Semantic Versioning](https://semver.org/).

## [0.3.0] — 2026-07-28

### Added
- Tool registry with dynamic tool registration and execution
- Function calling integration with Groq LLM
- Calculator, current time, and UUID tools
- Assistant endpoint (`POST /assistant`) with tool-calling loop
- Prompt management system (`app/prompts/`) with markdown templates
- Code explanation endpoint (`POST /code/explain`)
- SQL generation endpoint (`POST /sql/generate`)

### Changed
- Repository restructured: flattened from `phase-3/` to root
- Prompts promoted from `app/llm/prompts/` to `app/prompts/`
- Tests moved to top-level `tests/` directory
- Documentation formalized under `docs/`

## [0.2.0]

### Added
- Chat endpoint with streaming support
- Summarization endpoint with structured JSON output
- Entity extraction endpoint
- Provider abstraction with Groq
- Pydantic request/response schemas

## [0.1.0]

### Added
- Initial FastAPI scaffolding
- Health check endpoint
- Project configuration with pydantic-settings
