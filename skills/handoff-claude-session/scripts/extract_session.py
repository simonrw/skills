#!/usr/bin/env python3
"""Extract a readable transcript from a Claude Code session JSONL log."""

from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from pathlib import Path
from typing import Any, TextIO


def default_claude_dir() -> Path:
    configured_dir = os.environ.get("CLAUDE_CONFIG_DIR")
    if configured_dir:
        return Path(configured_dir).expanduser()
    return Path.home() / ".claude"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract a Claude Code session without invoking Claude."
    )
    parser.add_argument("session_id", help="Claude Code session UUID")
    parser.add_argument(
        "--claude-dir",
        type=Path,
        default=default_claude_dir(),
        help="Claude data directory (default: $CLAUDE_CONFIG_DIR or ~/.claude)",
    )
    parser.add_argument("--output", type=Path, help="Write Markdown to this path")
    return parser.parse_args()


def normalize_session_id(value: str) -> str:
    try:
        return str(uuid.UUID(value))
    except ValueError as error:
        raise ValueError(f"invalid Claude session ID: {value!r}") from error


def find_log(claude_dir: Path, session_id: str) -> Path:
    projects_dir = claude_dir.expanduser() / "projects"
    matches = sorted(projects_dir.glob(f"*/{session_id}.jsonl"))
    if not matches:
        raise FileNotFoundError(
            f"no session log for {session_id} under {projects_dir}"
        )
    if len(matches) > 1:
        paths = "\n".join(f"  {path}" for path in matches)
        raise RuntimeError(f"multiple session logs found:\n{paths}")
    return matches[0]


def load_records(path: Path, session_id: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                print(
                    f"warning: skipped malformed JSON at {path}:{line_number}: {error}",
                    file=sys.stderr,
                )
                continue
            if record.get("sessionId") == session_id and not record.get("isSidechain"):
                records.append(record)
    if not records:
        raise RuntimeError(f"session log contains no main-chain records for {session_id}")
    return records


def json_block(value: Any) -> str:
    return "```json\n" + json.dumps(value, indent=2, ensure_ascii=False) + "\n```"


def render_content(content: Any) -> list[str]:
    if isinstance(content, str):
        return [content] if content.strip() else []
    if not isinstance(content, list):
        return []

    rendered: list[str] = []
    for block in content:
        if isinstance(block, str):
            if block.strip():
                rendered.append(block)
            continue
        if not isinstance(block, dict):
            continue

        block_type = block.get("type")
        if block_type == "text" and block.get("text", "").strip():
            rendered.append(block["text"])
        elif block_type == "tool_use":
            name = block.get("name", "unknown")
            rendered.append(f"Tool call: `{name}`\n\n{json_block(block.get('input'))}")
        elif block_type == "tool_result":
            result = block.get("content", "")
            label = "Tool result"
            if block.get("is_error"):
                label += " (error)"
            result_parts = render_content(result)
            if not result_parts and result != "" and result is not None:
                result_parts = [json_block(result)]
            rendered.append(f"{label}:\n\n" + "\n\n".join(result_parts))
    return rendered


def first_value(records: list[dict[str, Any]], key: str) -> str:
    return next((str(record[key]) for record in records if record.get(key)), "unknown")


def write_transcript(
    destination: TextIO,
    log_path: Path,
    session_id: str,
    records: list[dict[str, Any]],
) -> None:
    timestamps = [record["timestamp"] for record in records if record.get("timestamp")]
    print("# Claude session transcript", file=destination)
    print(file=destination)
    print(f"- Session: `{session_id}`", file=destination)
    print(f"- Log: `{log_path}`", file=destination)
    print(f"- Working directory: `{first_value(records, 'cwd')}`", file=destination)
    print(f"- Git branch: `{first_value(records, 'gitBranch')}`", file=destination)
    if timestamps:
        print(f"- First event: `{timestamps[0]}`", file=destination)
        print(f"- Last event: `{timestamps[-1]}`", file=destination)

    for record in records:
        record_type = record.get("type")
        if record_type not in {"user", "assistant"}:
            continue
        content = record.get("message", {}).get("content")
        parts = render_content(content)
        if not parts:
            continue
        is_tool_result = isinstance(content, list) and any(
            isinstance(block, dict) and block.get("type") == "tool_result"
            for block in content
        )
        role = "Tool" if is_tool_result else record_type.title()
        timestamp = record.get("timestamp", "unknown time")
        print(file=destination)
        print(f"## {role} - {timestamp}", file=destination)
        print(file=destination)
        print("\n\n".join(parts), file=destination)


def main() -> int:
    args = parse_args()
    try:
        session_id = normalize_session_id(args.session_id)
        log_path = find_log(args.claude_dir, session_id)
        records = load_records(log_path, session_id)
        if args.output:
            output_path = args.output.expanduser()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with output_path.open("w", encoding="utf-8") as destination:
                write_transcript(destination, log_path, session_id, records)
        else:
            write_transcript(sys.stdout, log_path, session_id, records)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
