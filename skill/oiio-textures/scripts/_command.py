from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Sequence


def existing_file(path: str) -> Path:
    value = Path(path).expanduser().resolve()
    if not value.is_file():
        raise FileNotFoundError(value)
    return value


def new_output(input_path: str, output_path: str) -> tuple[Path, Path]:
    source = existing_file(input_path)
    target = Path(output_path).expanduser().resolve()
    if source == target:
        raise ValueError("output_path must differ from input_path")
    target.parent.mkdir(parents=True, exist_ok=True)
    return source, target


def run(args: Sequence[str]) -> str:
    completed = subprocess.run(list(args), check=True, capture_output=True, text=True)
    return completed.stdout.strip()

