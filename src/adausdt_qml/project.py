# notebooks/project.py
from __future__ import annotations

import os
from pathlib import Path


def find_project_root(start: Path | None = None) -> Path:
    """Walk up from `start` until a project marker is found."""
    start = (start or Path.cwd()).resolve()
    for p in (start, *start.parents):
        if (p / "pyproject.toml").exists() or (p / ".git").exists() or (p / "src").exists():
            return p
    raise RuntimeError("Project root not found (expected pyproject.toml/.git/src).")


def setup() -> Path:
    """
    Set CWD to project root so relative paths like 'cache/' work.
    Returns the project root Path.
    """
    root = find_project_root()
    os.chdir(root)
    return root