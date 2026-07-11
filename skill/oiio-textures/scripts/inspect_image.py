from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _command import existing_file, run


@skill_entry
def main(input_path: str, verbose: bool = True, **_: Any) -> dict[str, Any]:
    try:
        source = existing_file(input_path)
        args = ["iinfo"] + (["-v"] if verbose else []) + [str(source)]
        return skill_success("Image inspected", file=str(source), report=run(args))
    except Exception as exc:
        return skill_exception(exc, message="Image inspection failed")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main
    run_main(main)

