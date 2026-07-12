from pathlib import Path

PROMPT_DIR = Path(__file__).parent
prompts = {}

for prompt_file in PROMPT_DIR.glob("*.md"):
    prompt_name = prompt_file.stem
    prompts[prompt_name] = prompt_file.read_text(encoding="utf-8")


def loader(promptFile: str):
    return prompts.get(promptFile)
