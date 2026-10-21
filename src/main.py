"""Command-line entry point for the PromptOps assignment."""

from .app import analyze_issue


def main() -> None:
    issue = input("Software issue: ").strip()
    prompt_version = input("Prompt version (v1, v2, or v3): ").strip()
    print(analyze_issue(issue, prompt_version))


if __name__ == "__main__":
    main()