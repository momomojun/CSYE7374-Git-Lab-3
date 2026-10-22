"""Application orchestration for prompt selection and model inference."""

from collections.abc import Callable

from .model import generate_text
from .prompts import prompt_v1, prompt_v2, prompt_v3

PromptBuilder = Callable[[str], str]
PROMPT_BUILDERS: dict[str, PromptBuilder] = {
    "v1": prompt_v1,
    "v2": prompt_v2,
    "v3": prompt_v3,
}


def analyze_issue(issue: str, prompt_version: str) -> str:
    """Build the selected prompt for an issue and return the model response."""
    prompt_builder = PROMPT_BUILDERS.get(prompt_version)
    if prompt_builder is None:
        raise ValueError(f"unknown prompt version: {prompt_version!r}")
    return generate_text(prompt_builder(issue))
