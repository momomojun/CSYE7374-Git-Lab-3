import pytest

from src.prompts import prompt_v1, prompt_v2, prompt_v3

ISSUE = "The API returns HTTP 503 errors under heavy traffic."


def test_each_prompt_is_a_string_and_contains_issue():
    # TODO: STUDENT IMPLEMENT
    prompts = [prompt_v1(ISSUE), prompt_v2(ISSUE), prompt_v3(ISSUE)]

    assert all(isinstance(prompt, str) for prompt in prompts)
    assert all(ISSUE in prompt for prompt in prompts)


def test_prompt_versions_are_distinct():
    # TODO: STUDENT IMPLEMENT
    assert len({prompt_v1(ISSUE), prompt_v2(ISSUE), prompt_v3(ISSUE)}) == 3


def test_prompt_rejects_blank_issue():
    # TODO: STUDENT IMPLEMENT
    for prompt_builder in (prompt_v1, prompt_v2, prompt_v3):
        with pytest.raises(ValueError, match="non-empty"):
            prompt_builder("   ")
