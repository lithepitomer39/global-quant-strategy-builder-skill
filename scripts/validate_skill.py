#!/usr/bin/env python3
"""Validate the publishable Global Quant Strategy Builder repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "global-quant-strategy-builder"
SKILL_DIR = ROOT / "skills" / SKILL_NAME

REQUIRED_FILES = (
    ROOT / "README.md",
    ROOT / "README_EN.md",
    ROOT / "LICENSE",
    ROOT / "AGENTS.md",
    ROOT / "examples" / "prompt-gallery.md",
    ROOT / ".github" / "workflows" / "validate-skill.yml",
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "global-markets.md",
    SKILL_DIR / "references" / "us-equities-etfs.md",
    SKILL_DIR / "references" / "hong-kong-equities.md",
    SKILL_DIR / "references" / "listed-options.md",
    SKILL_DIR / "references" / "futures-fx-crypto.md",
    SKILL_DIR / "references" / "frameworks.md",
    SKILL_DIR / "references" / "validation.md",
)

_TODO = "TO" + "DO"
_TBD = "T" + "BD"
_USER_REPO_PLACEHOLDER = "YOUR" + r"[_ -]?" + "GITHUB"
PLACEHOLDER_PATTERNS = (
    re.compile(rf"\b{_TODO}\b", re.IGNORECASE),
    re.compile(rf"\b{_TBD}\b", re.IGNORECASE),
    re.compile(_USER_REPO_PLACEHOLDER, re.IGNORECASE),
    re.compile(rf"\[{_TODO}[^\]]*\]", re.IGNORECASE),
)

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")

    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    values: Dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in values:
            raise ValueError(f"duplicate frontmatter key: {key}")
        values[key] = value
    return values, "\n".join(lines[end + 1 :])


def find_local_markdown_links(path: Path, text: str) -> Iterable[Tuple[str, Path]]:
    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        yield match.group(1), (path.parent / target).resolve()


def validate_openai_yaml(path: Path, errors: List[str]) -> None:
    text = read_text(path)
    required_values = {
        "display_name": "Global Quant Strategy Builder",
        "short_description": "Build testable global, US, and Hong Kong strategies",
    }
    for key, expected in required_values.items():
        pattern = re.compile(rf"^\s*{re.escape(key)}:\s*[\"']([^\"']+)[\"']\s*$", re.MULTILINE)
        match = pattern.search(text)
        if not match:
            errors.append(f"{path.relative_to(ROOT)}: missing quoted {key}")
        elif match.group(1) != expected:
            errors.append(f"{path.relative_to(ROOT)}: unexpected {key}")

    short_match = re.search(r"^\s*short_description:\s*[\"']([^\"']+)[\"']\s*$", text, re.MULTILINE)
    if short_match and not 25 <= len(short_match.group(1)) <= 64:
        errors.append(f"{path.relative_to(ROOT)}: short_description must be 25-64 characters")

    prompt_match = re.search(r"^\s*default_prompt:\s*[\"']([^\"']+)[\"']\s*$", text, re.MULTILINE)
    if not prompt_match:
        errors.append(f"{path.relative_to(ROOT)}: missing quoted default_prompt")
    elif f"${SKILL_NAME}" not in prompt_match.group(1):
        errors.append(f"{path.relative_to(ROOT)}: default_prompt must mention ${SKILL_NAME}")


def main() -> int:
    errors: List[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    skill_path = SKILL_DIR / "SKILL.md"
    try:
        frontmatter, body = parse_frontmatter(read_text(skill_path))
    except ValueError as exc:
        errors.append(str(exc))
        frontmatter, body = {}, ""

    if set(frontmatter) != {"name", "description"}:
        errors.append("SKILL.md frontmatter must contain exactly name and description")
    if frontmatter.get("name") != SKILL_NAME:
        errors.append("SKILL.md name must match its directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", frontmatter.get("name", "")):
        errors.append("SKILL.md name must use lowercase hyphen-case")
    if len(frontmatter.get("name", "")) > 63:
        errors.append("SKILL.md name must be shorter than 64 characters")
    if len(frontmatter.get("description", "")) < 80:
        errors.append("SKILL.md description is too short to explain triggers and scope")
    if len(body.splitlines()) >= 500:
        errors.append("SKILL.md body must stay under 500 lines")

    skill_text = read_text(skill_path)
    for reference in sorted((SKILL_DIR / "references").glob("*.md")):
        relative_target = f"references/{reference.name}"
        if f"]({relative_target})" not in skill_text:
            errors.append(f"SKILL.md does not link {relative_target}")

    validate_openai_yaml(SKILL_DIR / "agents" / "openai.yaml", errors)

    checked_text_files = list(ROOT.rglob("*.md")) + [
        ROOT / ".github" / "workflows" / "validate-skill.yml",
        ROOT / "scripts" / "validate_skill.py",
    ]
    for path in checked_text_files:
        text = read_text(path)
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: unresolved placeholder matching {pattern.pattern!r}")
        if path.suffix == ".md":
            for target_text, resolved in find_local_markdown_links(path, text):
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    errors.append(f"{path.relative_to(ROOT)}: local link escapes repository: {target_text}")
                    continue
                if not resolved.exists():
                    errors.append(f"{path.relative_to(ROOT)}: broken local link: {target_text}")

    if errors:
        for error in sorted(set(errors)):
            print(f"[ERROR] {error}")
        return 1

    print(f"[OK] Validated {SKILL_NAME}")
    print(f"[OK] Checked {len(REQUIRED_FILES)} required files")
    print(f"[OK] Checked {len(list(ROOT.rglob('*.md')))} Markdown files and their local links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
