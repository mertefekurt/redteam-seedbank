![Redteam Seedbank cover](assets/readme-cover.svg)

# Redteam Seedbank

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Generate compact red-team prompt seeds for AI app evaluations.

## Read this first

This is a compact tool, not a platform. The useful part is the repeatable check and the plain output, so the repository keeps setup and code paths short.

## First run

```bash
python -m pip install -e ".[dev]"
redteam-seedbank examples/sample.jsonl
```

## Maintenance

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m redteam_seedbank --help
```

## Repository map

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
