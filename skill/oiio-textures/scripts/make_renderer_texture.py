from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _command import new_output, run


@skill_entry
def main(
    input_path: str,
    output_path: str,
    input_color_space: str | None = None,
    output_color_space: str | None = None,
    ocio_config: str | None = None,
    **_: Any,
) -> dict[str, Any]:
    try:
        source, target = new_output(input_path, output_path)
        args = ["maketx", str(source), "-o", str(target)]
        if input_color_space and output_color_space:
            args += ["--colorconvert", input_color_space, output_color_space]
        if ocio_config:
            args += ["--colorconfig", ocio_config]
        report = run(args)
        return skill_success("Renderer texture created", file=str(target), report=report)
    except Exception as exc:
        return skill_exception(exc, message="Renderer texture generation failed")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main
    run_main(main)

