from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _command import file_path, run


@skill_entry
def main(config_path: str, **_: Any) -> dict[str, Any]:
    try:
        config = file_path(config_path)
        return skill_success("OCIO config is valid", file=str(config), report=run(["ociocheck", "--iconfig", str(config)]))
    except Exception as exc:
        return skill_exception(exc, message="OCIO config validation failed")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main
    run_main(main)

