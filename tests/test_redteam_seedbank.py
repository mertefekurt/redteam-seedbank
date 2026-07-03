from __future__ import annotations

import json

import pytest

from redteam_seedbank.cli import main
from redteam_seedbank.core import categories, render_jsonl, render_markdown, select


def test_categories_are_sorted() -> None:
    assert categories() == sorted(categories())


def test_select_filters_category() -> None:
    assert select("tool-abuse", 5, 1)[0].category == "tool-abuse"


def test_select_is_deterministic() -> None:
    assert select(None, 2, 9) == select(None, 2, 9)


def test_unknown_category_raises() -> None:
    with pytest.raises(ValueError):
        select("missing", 1, 1)


def test_jsonl_render() -> None:
    assert json.loads(render_jsonl(select("tool-abuse", 1, 1)))["category"] == "tool-abuse"


def test_markdown_render() -> None:
    assert "# Red-team seeds" in render_markdown(select(None, 1, 1))


def test_cli_help(capsys) -> None:
    try:
        main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0
    assert "red-team" in capsys.readouterr().out
