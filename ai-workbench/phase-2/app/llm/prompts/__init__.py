from pathlib import Path

_prompt_path = Path(__file__).parent / "summary.md"
try:
    summary = _prompt_path.read_text(encoding="utf-8")
except Exception:
    summary = "You are a precise summarization assistant. Summarize the following text."
