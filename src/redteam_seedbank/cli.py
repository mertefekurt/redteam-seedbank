from __future__ import annotations

import argparse

from redteam_seedbank.core import categories, render_jsonl, render_markdown, select


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate deterministic AI red-team prompt seeds.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="list categories")
    sample = sub.add_parser("sample", help="sample seeds")
    sample.add_argument("--category")
    sample.add_argument("--count", type=int, default=3)
    sample.add_argument("--seed", type=int, default=1)
    sample.add_argument("--format", choices=("jsonl", "markdown"), default="markdown")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "list":
        print("\n".join(categories()))
        return 0
    seeds = select(args.category, args.count, args.seed)
    print(render_jsonl(seeds) if args.format == "jsonl" else render_markdown(seeds), end="")
    return 0
