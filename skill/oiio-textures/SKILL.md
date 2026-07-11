---
name: oiio-textures
description: Infrastructure skill for inspecting images and producing tiled mipmapped renderer textures with OpenImageIO. Use before DCC material binding. Not for creative image generation.
license: MIT
compatibility: "dcc-mcp-core 0.19+, OpenImageIO 2.5+"
metadata:
  dcc-mcp:
    dcc: python
    layer: infrastructure
    stage: pipeline
    version: "0.1.0"
    tags: [openimageio, texture, tx, mipmap, image, pipeline]
    search-hint: "inspect texture metadata, make tx texture, tiled mipmaps, OpenImageIO, renderer texture"
    tools: tools.yaml
    runtimes: runtimes.yaml
---

# OpenImageIO Textures

Use deterministic OpenImageIO commands for image inspection and renderer-ready
texture generation. Outputs are new files; source files are never overwritten.

