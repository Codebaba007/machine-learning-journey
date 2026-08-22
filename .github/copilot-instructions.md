# Copilot instructions for machine-learning-journey

Purpose

- Short: a learning-first machine learning repository arranged as progressive modules (01_python_for_ml → 10_projects) with reusable library code under `src/`, interactive content in `notebooks/`, datasets in `datasets/`, and documentation via MkDocs.

Build, test, and lint commands

- Create & activate a virtual environment (recommended):
  - Windows (cmd.exe):
    .venv\Scripts\activate
  - PowerShell:
    .venv\Scripts\Activate.ps1

- Install dependencies (from project root):
  - pip install -r requirements.txt
  - or use pyproject tooling for formatters (black/isort/ruff are configured in pyproject.toml).

- Start JupyterLab (local):
  - jupyter lab

- Docker (dev image, JupyterLab):
  - docker build -t ml-journey .
  - docker run -it --rm -v "$(pwd):/app" -p 8888:8888 ml-journey

- Docker Compose (recommended development setup):
  - docker-compose up             # starts jupyter by default
  - docker-compose up api         # starts FastAPI service (profile: api)
  - docker-compose up --profile mlops mlflow   # start mlflow service
  - docker-compose down

- FastAPI (local dev):
  - uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
    - NOTE: docker-compose references `src.api:app` — confirm the FastAPI entrypoint path if the API module is added/renamed.

Lint/format (same commands used by CI):
- Black (format check):
  - black --check --diff .
  - To apply: black .
- isort (import sorting):
  - isort --check-only --diff .
  - To apply: isort .
- Ruff (lint):
  - ruff check .

Tests (pytest)
- Run all tests (CI uses):
  - pytest tests/ -v --tb=short
- Run tests as configured by pyproject.toml (includes coverage by default via addopts):
  - pytest
- Run a single test function or file (examples):
  - pytest tests/test_models.py::test_regressor_fit -q
  - pytest tests/test_models.py -q
  - pytest -k "pattern" -q   # run tests matching `pattern`

CI
- GitHub Actions workflow: .github/workflows/python-check.yml
  - Installs black, ruff, isort, pytest, and runs:
    - black --check --diff .
    - isort --check-only --diff .
    - ruff check .
    - pytest tests/ -v --tb=short

High-level architecture

- Learning-module layout
  - Top-level numbered modules (01_python_for_ml, 02_numpy, …). Each module is self-contained with its own README, notes, exercises, and mini projects. Use module README files for day-by-day journals and exercises.

- Library code (src/)
  - `src/` contains reusable utility and library code intended to be imported by notebooks and small projects. Key subpackages present today:
    - `src.data` — data loading & preprocessing helpers
    - `src.features` — feature engineering helpers
    - `src.models` — simple ML models wrappers (classifiers/regressors)
    - `src.training` — training/experiment helper (Trainer)
    - `src.evaluation` — metrics & evaluation utilities
    - `src.utils` — logging/helpers
    - `src.visualization` — plotting helpers
  - Packaging note: pyproject.toml sets `known_first_party = ["src"]`, use `src`-first layout when importing or packaging.

- Interactive & docs
  - `notebooks/` — step-by-step interactive notebooks for learning and examples.
  - `docs/` + `mkdocs.yml` — static docs site built with MkDocs Material (site config and cheatsheets listed in mkdocs.yml).

- Experiment & infra
  - `docker-compose.yml` defines three services used in development:
    - `jupyter` — JupyterLab; mounts project and dataset volume
    - `api` — uvicorn-based FastAPI (profile: api)
    - `mlflow` — MLflow server backing store (profile: mlops)
  - Dockerfile builds a lightweight dev image with JupyterLab default CMD.

- Tests & CI
  - Tests live under `tests/` and follow `test_*.py` naming; pytest configuration lives in pyproject.toml and includes coverage collection for `src/`.
  - GitHub Actions (`.github/workflows/python-check.yml`) enforces formatting, import sorting, linting, and runs the test suite on push/PR to main.

Key conventions (repo-specific)

- src-first layout: code intended for importable modules lives under `src/`. pyproject.toml uses this as the first-party package root.

- Module folders are numbered and considered the canonical learning unit. Each module contains its own README and local artifacts (notes, exercises, mini_projects). When adding content for a stage, follow the same numbered folder convention.

- Testing conventions:
  - test file names: `tests/test_*.py`
  - test function names: `test_*`
  - pytest markers configured in pyproject.toml:
    - `slow` (can be deselected with `-m "not slow"`)
    - `integration`
  - pytest addopts include coverage collection: running `pytest` will include coverage by default.

- Formatting & linting rules (authoritative configs in pyproject.toml):
  - Black: line-length 88, target py310–py312
  - isort: profile = black
  - Ruff: selected rules + pydocstyle using Google convention; certain pydoc/annotation rules ignored (see pyproject.toml)
  - Follow these configs for any automated formatting/linting changes in PRs — CI enforces `--check` modes.

- Docker-compose profiles: `api` and `mlops` control extra services. By default `docker-compose up` starts JupyterLab only.

- Notebook usage: notebooks assume you run from project root so relative dataset paths (e.g., `datasets/`) resolve correctly. When running inside Docker, the compose mounts `.` to `/app` and datasets to `/app/datasets`.

- Experiment tracking placeholder: docker-compose binds MLflow to a local sqlite backend inside a named volume (`mlflow-data`). Keep this pattern if you add MLflow experiments to avoid committing large artifacts.

AI assistant / other assistant configs

- No existing Copilot instructions file was present prior to this addition.
- No CLAUDE.md, AGENTS.md, .cursorrules, or similar AI-assistant files were detected. If you maintain other assistant rule files, place repository-specific guidance there and reference it here.

Notes for Copilot sessions

- Prefer reading module README.md and the relevant `src/` package before suggesting code changes or running experiments — module READMEs contain the daily progress and constraints for that stage.
- When proposing code edits, run or suggest the same lint/format commands that CI uses (black, isort, ruff) and ensure tests under `tests/` pass locally. Use minimal, surgical edits scoped to the relevant module or `src/` package.
- For new features that introduce runtime dependencies, update `requirements.txt` and include a short note in the module README describing how to run the new code (venv, docker-compose, or direct python invocation).

What was added

- This file: `.github/copilot-instructions.md` capturing build/test/lint commands, high-level architecture, and repo-specific conventions for Copilot sessions.

If you'd like changes

- Ask to: expand the file with examples for specific modules, include commands to run particular notebooks, or add explicit step-by-step instructions for contributing new module content.

