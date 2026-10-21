"""Hugging Face model loading and text generation helpers."""

from functools import lru_cache
from typing import Any

DEFAULT_MODEL_NAME = "sshleifer/tiny-gpt2"


@lru_cache(maxsize=2)
def load_tokenizer(model_name: str = DEFAULT_MODEL_NAME) -> Any:
    """Load and cache a tokenizer from Hugging Face."""
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained(model_name)


@lru_cache(maxsize=2)
def load_model(model_name: str = DEFAULT_MODEL_NAME) -> Any:
    """Load and cache a causal language model from Hugging Face."""
    from transformers import AutoModelForCausalLM

    return AutoModelForCausalLM.from_pretrained(model_name)


def generate_text(
    prompt: str,
    model_name: str = DEFAULT_MODEL_NAME,
    max_new_tokens: int = 80,
) -> str:
    """Generate text for a prompt using the configured Hugging Face model."""
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("prompt must be a non-empty string")
    if max_new_tokens <= 0:
        raise ValueError("max_new_tokens must be positive")

    tokenizer = load_tokenizer(model_name)
    model = load_model(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    output_ids = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
