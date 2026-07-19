# dcc-texture-pipeline

<p align="center">
  <img src="docs/assets/dcc-texture-pipeline.svg" alt="DCC-MCP · TEXTURE-PIPELINE" width="600">
</p>

## Agent workflow

AI agents should use installed package skills through the shared gateway. IDE
users may continue to use the MCP endpoint.

### Install or update the CLI

`dcc-mcp-cli` is the preferred control path for every shell-capable agent. If
it is missing, ask the user before installing the latest official release:

```bash
# Linux/macOS
curl -fsSL https://raw.githubusercontent.com/dcc-mcp/dcc-mcp-core/main/scripts/install-cli.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/dcc-mcp/dcc-mcp-core/main/scripts/install-cli.ps1 | iex"
```

Keep an official build current through the release manifest:

```bash
dcc-mcp-cli update check
dcc-mcp-cli update apply
```

`update apply` downloads and stages the latest CLI for the next launch. It
does not update a running `dcc-mcp-server`; update that server in its own
environment.

```bash
dcc-mcp-cli dcc-types
dcc-mcp-cli list
dcc-mcp-cli search --query "<task>" --dcc-type <host>
dcc-mcp-cli describe <tool-slug>
dcc-mcp-cli call <tool-slug> --json '{"key":"value"}'
```

If the package skill is not active, call
`dcc-mcp-cli load-skill <skill-name> --dcc-type <host>`. After the task,
query `dcc-mcp-cli stats --range 24h --session-id <task-id>` and pass only
bounded evidence to the `review_skill_improvement` prompt from
`dcc-mcp-skills-creator`.


Deterministic, DCC-neutral texture processing built on OpenImageIO and
OpenColorIO. Use it between generated/downloaded source images and host
material binding.

![Texture maps moving through color conversion and mip generation toward a DCC asset](docs/images/dcc-texture-pipeline-showcase.webp)

## Included skills

- `oiio-textures`: inspect images and build tiled, mipmapped renderer textures.
- `ocio-color`: validate OCIO configs and convert pixels between named spaces.

```mermaid
flowchart LR
    S[Source texture] --> I[OIIO inspection]
    I --> C[OCIO conversion]
    C --> T[TX and MIP generation]
    T --> D[Maya Blender Houdini 3ds Max Unreal]
```

Install OpenImageIO and OpenColorIO command-line tools, then add both `skill/*`
directories to the DCC-MCP skill path.

