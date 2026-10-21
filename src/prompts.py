"""Prompt templates used by the issue-analysis application."""


def _validate_issue(issue: str) -> str:
    if not isinstance(issue, str) or not issue.strip():
        raise ValueError("issue must be a non-empty string")
    return issue.strip()


def prompt_v1(issue: str) -> str:
    # TODO: STUDENT IMPLEMENT
    pass


def prompt_v2(issue: str) -> str:
    """Build an issue-analysis prompt with engineering context."""
    issue = _validate_issue(issue)
    return (
        "You are a senior software engineer helping diagnose a production issue. "
        "Explain likely causes, checks to run, and a safe fix.\n\n"
        f"Issue: {issue}"
    )


def prompt_v3(issue: str) -> str:
    """Build an issue-analysis prompt requesting a structured response."""
    issue = _validate_issue(issue)
    return (
        "Analyze the software issue below. Return exactly these sections: "
        "Summary, Likely Causes, Investigation Steps, and Recommended Fix.\n\n"
        f"Software issue: {issue}"
    )
