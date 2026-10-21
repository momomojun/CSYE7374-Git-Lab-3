import pytest

from src import app

ISSUE = "The service returns HTTP 503 errors."


def test_analyze_issue_selects_prompt_and_returns_model_response(monkeypatch):
    # TODO: STUDENT IMPLEMENT
    seen = {}

    def fake_generate(prompt):
        seen["prompt"] = prompt
        return "diagnosis"

    monkeypatch.setattr(app, "generate_text", fake_generate)

    assert app.analyze_issue(ISSUE, "v2") == "diagnosis"
    assert ISSUE in seen["prompt"]


def test_analyze_issue_rejects_unknown_prompt_version():
    # TODO: STUDENT IMPLEMENT
    with pytest.raises(ValueError, match="unknown prompt version"):
        app.analyze_issue(ISSUE, "v9")
