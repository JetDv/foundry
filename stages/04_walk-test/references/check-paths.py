#!/usr/bin/env python3
"""Resolve every relative path written in a workspace's contracts and entry files.

Usage: python3 check-paths.py [workspace_root]

Scope is deliberate. In contracts (`CONTEXT.md`) and entry files (`AGENTS.md`,
`CLAUDE.md`), a path is the interface and must resolve. In reference and
template files, paths are illustrative — `../01_research/output/research.md`
in an example is not a claim that the file exists. Checking those too produces
noise, and a checker that cries wolf is a checker nobody runs.

Exists because check 2 of the walk test is not verifiable by reading. A broken
input path is invisible until the run that needs it, and the run that needs it
is usually weeks later, in someone else's hands.
"""
import pathlib
import re
import sys

CHECKED = {"CONTEXT.md", "AGENTS.md", "CLAUDE.md"}

# Artifacts a run produces: absent before the first run, not a failure.
RUN_ARTIFACT = re.compile(
    r"(brief|blueprint|emit-manifest|walk-report)\.md$|/output/[^/]+\.md$"
)
BACKTICKED = re.compile(r"`([^`\n]+)`")


def is_path_claim(token: str) -> bool:
    """A token is a path claim only if it navigates: it contains a separator,
    carries no glob or placeholder, and is not prose with spaces."""
    if "*" in token or "{" in token or " " in token.strip():
        return False
    if token.startswith(("http", "#", "$")):
        return False
    # A bare `output/` or `references/` names a folder's role, not a location.
    if token.count("/") == 1 and token.endswith("/"):
        return False
    return "/" in token


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    broken, checked = [], 0
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts or md.name not in CHECKED:
            continue
        checked += 1
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for raw in BACKTICKED.findall(line):
                token = raw.strip()
                if not is_path_claim(token) or RUN_ARTIFACT.search(token):
                    continue
                if (md.parent / token).exists() or (root / token.lstrip("/")).exists():
                    continue
                broken.append(f"{md.relative_to(root)}:{lineno}  ->  {token}")

    if broken:
        print(f"BROKEN ({len(broken)} in {checked} contract/entry files):")
        print("\n".join("  " + b for b in broken))
        return 1
    print(f"all paths resolve — {checked} contract/entry files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
