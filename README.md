# LLMOps Assignment 1: PromptOps

A small PromptOps application that loads a lightweight Hugging Face causal language model, generates software-issue prompts, and compares three prompt styles.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The default model is `sshleifer/tiny-gpt2`, configured in `src/model.py`. Model files are downloaded by Hugging Face on the first real inference run. Loading is lazy so tests and prompt development do not require a download.

## Run Tests

```bash
make test
```

## Required Workflow

From the repository root, run:

```bash
make install
make lint
make test
make check
```

The expected workflow is:

```bash
make install
make check
```

Run `make check` before submitting. All tests and Ruff linting checks must pass.

Some source and test functions intentionally contain `# TODO: STUDENT IMPLEMENT`.
The related tests are active and should fail until students complete the TODOs.
The model tests use mocked components, so unit tests do not download or execute
the Hugging Face model.

## Run an Analysis

```bash
python -c 'from src.app import analyze_issue; print(analyze_issue("The application returns HTTP 503 errors under heavy traffic.", "v2"))'
```

The same application can be started with:

```bash
make run
```

Run the examples with `v1`, `v2`, and `v3` to compare the generated responses.

## Prompt Evaluation

Prompt V1:
Observation: The direct instruction is concise and gives the model broad freedom, so the response is often quick but may omit investigation detail.

Prompt V2:
Observation: Adding an engineering role and requested diagnostic context encourages discussion of causes, checks, and a safer fix.

Prompt V3:
Observation: The explicit section structure produces the most scannable and useful response for comparing incidents because it separates diagnosis from action.

Prompt V3 produced the most useful responses overall because its required sections make the result easier to review and apply. The exact quality still depends on the small model and the issue supplied.
