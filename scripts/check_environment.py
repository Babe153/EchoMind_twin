"""Check the day-one learning environment without contacting external services."""

import asyncio
import importlib
from importlib.metadata import version
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
DEPENDENCIES = (
    ("anthropic", "anthropic"),
    ("fastapi", "fastapi"),
    ("uvicorn", "uvicorn"),
    ("pydantic", "pydantic"),
    ("python-multipart", "multipart"),
    ("redis", "redis"),
    ("chromadb", "chromadb"),
    ("prometheus-client", "prometheus_client"),
    ("httpx", "httpx"),
    ("python-dotenv", "dotenv"),
    ("pytest", "pytest"),
)


def main():
    failures = []
    print(f"Python: {sys.version.split()[0]}")
    print(f"Interpreter: {sys.executable}")
    expected_venv = REPO_ROOT / ".venv"
    in_repo_venv = (
        sys.prefix != sys.base_prefix
        and Path(sys.prefix).resolve() == expected_venv.resolve()
    )
    if not in_repo_venv:
        failures.append("Run this script with the repository's .venv Python.")
    else:
        print("PASS repository virtual environment")

    for distribution, module in DEPENDENCIES:
        try:
            importlib.import_module(module)
            print(f"PASS {distribution}=={version(distribution)}")
        except Exception as exc:
            failures.append(f"{distribution}: {type(exc).__name__}: {exc}")

    required_dirs = (
        "core", "agents", "mcp", "memory", "skills", "monitor",
        "evaluation", "api", "tests", "exercises", "docs/learning-notes",
        "evaluation_cases", "evaluation_results", "config", "frontend",
    )
    missing_dirs = [name for name in required_dirs if not (REPO_ROOT / name).is_dir()]
    if missing_dirs:
        failures.append(f"Missing directories: {', '.join(missing_dirs)}")
    else:
        print("PASS learning directory layout")

    if not (REPO_ROOT / ".env.example").is_file():
        failures.append("Missing .env.example")
    else:
        print("PASS environment template exists")

    # Only a synthetic key is used; constructing the client makes no API request.
    client = None
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key="day01-local-check", base_url="https://example.invalid")
        print("PASS Anthropic client construction (no API call)")
    except Exception as exc:
        failures.append(f"Anthropic client: {type(exc).__name__}: {exc}")
    finally:
        if client is not None:
            client.close()

    async def check_async_client():
        from anthropic import AsyncAnthropic
        async with AsyncAnthropic(
            api_key="day01-local-check", base_url="https://example.invalid"
        ):
            pass

    try:
        asyncio.run(check_async_client())
        print("PASS async Anthropic client construction (no API call)")
    except Exception as exc:
        failures.append(f"Async Anthropic client: {type(exc).__name__}: {exc}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    print("PASS day-one environment checks; external services are not verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
