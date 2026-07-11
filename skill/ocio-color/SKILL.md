---
name: ocio-color
description: Infrastructure skill for validating OpenColorIO configs and converting image pixels between named color spaces. Use for consistent film, animation, and game color pipelines.
license: MIT
compatibility: "dcc-mcp-core 0.19+, OpenColorIO 2.3+, OpenImageIO 2.5+"
metadata:
  dcc-mcp:
    dcc: python
    layer: infrastructure
    stage: pipeline
    version: "0.1.0"
    tags: [opencolorio, ocio, aces, color, image, pipeline]
    search-hint: "validate OCIO config, ACEScg conversion, convert color space, color pipeline audit"
    tools: tools.yaml
    runtimes: runtimes.yaml
---

# OpenColorIO Color

Validate the studio configuration before conversion. Pixel conversion writes a
new output file and delegates color math to OpenImageIO compiled with OCIO.

