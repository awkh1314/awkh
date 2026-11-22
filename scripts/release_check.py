#!/usr/bin/env python3
"""Fail-closed checks for the public AWKH experience repository."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(r"\b(?:ghp_|gho_|ghu_|ghs_|ghr_|github_pat_)[A-Za-z0-9_]{20,}\b"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "url_credentials": re.compile(r"https?://[^/\s:@]+:[^/\s@]+@"),
}
PRIVATE_HOST_PATTERNS = [
    re.compile(r"agent\.qa\.awkh\.site", re.I),
    re.compile(r"agent\.awkh\.site", re.I),
    re.compile(r"dev\.awkh\.site", re.I),
]
FORBIDDEN_PATH_PARTS = {
    "private", "platform", "customer-data", "runtime-state",
}
FORBIDDEN_SUFFIXES = {
    ".pem", ".key", ".p12", ".pfx", ".db", ".sqlite", ".sqlite3",
    ".exe", ".dll", ".so", ".zip", ".gz", ".zst",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def git_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True,
        stdout=subprocess.PIPE,
    )
    return [p for p in result.stdout.decode().split("\0") if p]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="")
    args = parser.parse_args()

    version_file = ROOT / "VERSION"
    if not version_file.is_file():
        fail("VERSION file is missing.")
    version = version_file.read_text(encoding="utf-8").strip()
    if not VERSION_RE.fullmatch(version):
        fail(f"VERSION is not valid SemVer: {version!r}")
    if args.version and args.version != version:
        fail(f"Requested version {args.version!r} does not match VERSION {version!r}.")

    if os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch":
        if os.environ.get("GITHUB_REF") != "refs/heads/main":
            fail("Release workflow must be dispatched from main.")

    required = [
        "README.md",
        "RELEASES.md",
        "CHANGELOG.md",
        "docs/quick-start.md",
        "docs/experience.md",
        "docs/privacy-and-safety.md",
        "docs/release-policy.md",
        f"releases/v{version}.md",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"Required public release file is missing: {relative}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    quick_start = (ROOT / "docs/quick-start.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    release_notes = (ROOT / f"releases/v{version}.md").read_text(encoding="utf-8")

    public_endpoint = "https://mcp.awkh.art/connect/mcp"
    if public_endpoint not in readme or public_endpoint not in quick_start or public_endpoint not in release_notes:
        fail("Official public MCP endpoint must be present in README, quick start, and release notes.")
    if f"## [{version}]" not in changelog:
        fail(f"CHANGELOG.md has no entry for {version}.")
    if f"v{version}" not in (ROOT / "RELEASES.md").read_text(encoding="utf-8"):
        fail(f"RELEASES.md does not list v{version}.")
    if "RELEASES.md" not in readme or "CHANGELOG.md" not in readme:
        fail("README must link to RELEASES.md and CHANGELOG.md.")

    tracked = git_files()
    if not tracked:
        fail("Git returned no tracked files.")
    findings: list[str] = []
    for relative in tracked:
        path = Path(relative)
        lowered_parts = {part.lower() for part in path.parts}
        if lowered_parts & FORBIDDEN_PATH_PARTS:
            findings.append(f"forbidden path: {relative}")
            continue
        if any(part == ".env" or (part.startswith(".env.") and part != ".env.example") for part in lowered_parts):
            findings.append(f"environment file not allowed in public experience repo: {relative}")
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(f"private key, database, binary, or package file not allowed: {relative}")
            continue
        full_path = ROOT / path
        try:
            raw = full_path.read_bytes()
            if b"\0" in raw or len(raw) > 2_000_000:
                continue
            content = raw.decode("utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                findings.append(f"{name} pattern in {relative}")
        for pattern in PRIVATE_HOST_PATTERNS:
            if pattern.search(content):
                findings.append(f"private QA hostname in {relative}")

    if findings:
        fail("Public-boundary/security scan failed:\n- " + "\n- ".join(findings))

    diff_check = subprocess.run(
        ["git", "diff", "--check"], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    if diff_check.returncode:
        fail("git diff --check failed:\n" + diff_check.stdout)

    print(f"PASS: public experience {version}")
    print(f"PASS: {len(required)} required release files present")
    print(f"PASS: {len(tracked)} tracked files scanned")
    print("PASS: public MCP endpoint, release metadata, and public/private boundary")
    print("PASS: no detected credential patterns or private QA hostnames")


if __name__ == "__main__":
    main()
