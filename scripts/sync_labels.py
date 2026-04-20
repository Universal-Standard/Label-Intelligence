#!/usr/bin/env python3
"""Synchronize label index with live labels from a GitHub repository."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path


def slugify(label: str) -> str:
    value = label.strip().lower()
    value = value.replace("/", "-")
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"[^a-z0-9-]", "", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "label"


def github_get(url: str, token: str) -> list[dict]:
    request = urllib.request.Request(url)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        request.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def list_labels(repo: str, token: str) -> list[dict]:
    owner, name = repo.split("/", 1)
    query = urllib.parse.urlencode({"per_page": 100, "page": 1})
    url = f"https://api.github.com/repos/{owner}/{name}/labels?{query}"
    labels = github_get(url, token)
    if not isinstance(labels, list):
        raise ValueError("Unexpected GitHub API response for labels")
    return sorted(labels, key=lambda item: item["name"].lower())


def read_labels_from_file(path: str) -> list[dict]:
    labels = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(labels, list):
        raise ValueError("labels-json must contain a JSON array")
    return sorted(labels, key=lambda item: item["name"].lower())


def build_index(labels: list[dict]) -> str:
    lines = [
        "# Label Catalog",
        "",
        "This index is synchronized with the GitHub label inventory.",
        "",
        "## Labels",
    ]
    for label in labels:
        name = label["name"]
        slug = slugify(name)
        desc = (label.get("description") or "No description configured in GitHub.").strip()
        lines.append(f"- [`{name}`](./{slug}.md) — {desc}")
    lines.append("")
    return "\n".join(lines)


def ensure_label_doc(path: Path, name: str, description: str) -> None:
    if path.exists():
        return

    content = f"""# Label: `{name}`

## Purpose
{description or 'Use this label to classify work matching the documented operational scope.'}

## When to Use
- Apply this label when issue or PR scope directly matches the purpose above.
- Pair this label with size and domain labels for better routing.

## When Not to Use
- Do not apply this label when the work can be represented more precisely by another existing label.
- Do not use this label without adding triage notes when context is ambiguous.

## Related Labels
- `question`
- `documentation`

## Automation Expectations
- No automation behavior is enforced by default for this label.
- Update this section in the same PR when workflow or bot behavior is introduced.

## Last Updated
{date.today().isoformat()}
"""
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="owner/repo")
    parser.add_argument("--docs-dir", required=True, help="Path to docs/labels directory")
    parser.add_argument("--index", required=True, help="Path to labels index markdown file")
    parser.add_argument(
        "--labels-json",
        help="Optional path to a JSON array of labels for offline sync testing",
    )
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN", "")

    if args.labels_json:
        try:
            labels = read_labels_from_file(args.labels_json)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"Failed to read labels from file: {exc}", file=sys.stderr)
            return 1
    else:
        try:
            labels = list_labels(args.repo, token)
        except (urllib.error.URLError, ValueError) as exc:
            print(f"Failed to fetch labels: {exc}", file=sys.stderr)
            return 1

    docs_dir = Path(args.docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    for label in labels:
        name = label["name"]
        description = (label.get("description") or "").strip()
        doc_path = docs_dir / f"{slugify(name)}.md"
        ensure_label_doc(doc_path, name, description)

    index_path = Path(args.index)
    index_path.write_text(build_index(labels), encoding="utf-8")
    print(f"Synchronized {len(labels)} labels from {args.repo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
