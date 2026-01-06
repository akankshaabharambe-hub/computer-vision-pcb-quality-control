## Source Code

This directory contains lightweight, production-oriented scripts that demonstrate
how model inference and post-processing would be integrated into a PCB inspection system.

The focus here is not on model training, but on **engineering the inference layer**
of an ML pipeline, including:

- Input validation and error handling
- Inference orchestration and model interface boundaries
- Structured outputs for downstream consumption (JSON + annotated images)
- Clear separation between code, configuration, and data

The implementation is intentionally modular and minimal to reflect how
computer vision components are typically embedded into larger manufacturing
or quality-control systems.

Training pipelines, datasets, and model weights are not included due to
size, licensing, and reproducibility constraints.
