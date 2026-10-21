"""Application orchestration for prompt selection and model inference."""

from collections.abc import Callable

from .model import generate_text  # noqa: F401
from .prompts import prompt_v1, prompt_v2, prompt_v3

PromptBuilder = Callable[[str], str]
PROMPT_BUILDERS: dict[str, PromptBuilder] = {
    "v1": prompt_v1,
    "v2": prompt_v2,
    "v3": prompt_v3,
}


def analyze_issue(issue: str, prompt_version: str) -> str:
    # TODO: STUDENT IMPLEMENT
    pass
