#!/usr/bin/env python3
"""Minimal offline lint for a handoff note. No network, no file writes, no secret output.

This does NOT verify code/test/permission claims. The Red Team must inspect evidence.
"""
from pathlib import Path
import re
import sys

FIELDS = (
    "목표·요구 ID", "승인 범위·제외·추가 승인", "환경·위치·진입점",
    "버전·작업 상태", "완료/진행/남은 일", "변경 파일·주요 흐름",
    "테스트 증거", "인간·AI 의사결정", "위험·차단·금지", "다음 첫 작업",
)
SECRET = (
    ("private-key", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ("github-token", r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{12,}\b"),
    ("aws-access-key", r"\bAKIA[0-9A-Z]{16}\b"),
    ("openai-key", r"\bsk-[A-Za-z0-9_-]{20,}\b"),
)
DANGEROUS = (
    ("destructive-cmd", r"\brm\s+-rf\b|\bgit\s+reset\s+--hard\b"),
    ("force-push", r"\bgit\s+push\b[^\n]*\s--force\b"),
    ("script-pipe", r"\b(?:curl|wget)\b[^\n]*\|\s*(?:bash|sh)\b"),
)


def lint(content):
    errors, warnings = [], []
    for f in FIELDS:
        if not re.search(r"(?m)^[ \t]*[-*]?[ \t]*"+re.escape(f)+r"[ \t]*:[ \t]*[^\s]", content):
            errors.append("missing-or-blank: " + f)
    for name, pat in SECRET:
        if re.search(pat, content, flags=re.I):
            errors.append("sensitive-value-pattern: " + name)
    for name, pat in DANGEROUS:
        if re.search(pat, content, flags=re.I):
            warnings.append("needs-manual-command-review: " + name)
    if re.search(r"(?i)ignore (?:all )?(?:previous|prior) instructions|이전 지시(?:를)? 무시", content):
        warnings.append("prompt-injection-candidate")
    if len(content) > 15000:
        warnings.append("excessive-length: review for unnecessary copied logs")
    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("usage: handoff_lint.py docs/handoff.md", file=sys.stderr)
        return 2
    p = Path(sys.argv[1])
    if not p.is_file():
        print("FAIL: handoff file absent")
        return 2
    errors, warnings = lint(p.read_text(encoding="utf-8"))
    for item in errors:
        print("FAIL:", item)
    for item in warnings:
        print("WARN:", item)
    if not errors and not warnings:
        print("PASS: structure and limited pattern checks only; verify code/tests separately")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
