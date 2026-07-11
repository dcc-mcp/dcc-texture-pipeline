from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _command import file_path, output_paths, run


@skill_entry
def main(
    input_path: str,
    output_path: str,
    from_space: str,
    to_space: str,
    config_path: str | None = None,
    **_: Any,
) -> dict[str, Any]:
    try:
        source, target = output_paths(input_path, output_path)
        args = ["oiiotool"]
        if config_path:
            args += ["--colorconfig", str(file_path(config_path))]
        args += [str(source), "--colorconvert", from_space, to_space, "-o", str(target)]
        report = run(args)
        return skill_success("Image color converted", file=str(target), report=report)
    except Exception as exc:
        return skill_exception(exc, message="Image color conversion failed")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main
    run_main(main)

