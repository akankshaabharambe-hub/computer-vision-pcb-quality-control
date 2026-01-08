# System Architecture

This document describes the high-level architecture of the Computer Vision–Based PCB Quality Control system.
The focus is on how model inference is engineered and integrated into a production inspection pipeline,
rather than on model training or dataset construction.

---

## Design Goals

The system was designed with the following goals in mind:

- **Low-latency inference** suitable for manufacturing environments
- **Clear separation of concerns** between ML, systems, and integration layers
- **Modularity**, allowing model upgrades without rewriting downstream logic
- **Production readiness**, including validation, error handling, and structured outputs
- **Ease of integration** with existing quality-control and MES systems

---

## High-Level Architecture

![High-Level Architecture Diagram](https://github.com/user-attachments/assets/11004151-38b8-44a4-aa54-8b91a047f855)

---

## Component Breakdown

### 1. Image Ingestion & Validation

Responsible for:
- Validating incoming image formats and dimensions
- Ensuring consistency with model expectations
- Isolating malformed or corrupted inputs early

This layer prevents downstream failures and simplifies debugging in production environments.

---

### 2. Inference Engine

The inference engine encapsulates all interaction with the trained object detection model.

Key characteristics:
- Model loading is abstracted behind a clean interface
- Inference is treated as a stateless operation
- Designed to support future model replacements without impacting callers

The repository includes **inference orchestration logic only**.
Model weights and training artifacts are excluded.

---

### 3. Post-Processing & Validation

After raw detections are generated, post-processing applies:

- Confidence thresholding
- Bounding box normalization
- Domain-specific rules for resistor placement and validity

This layer converts raw ML output into **actionable inspection results**.

---

### 4. Output Serialization & Integration

Results are emitted in formats suitable for downstream consumption:

- Structured JSON for system integration
- Annotated images for visualization and debugging
- Clear success/failure indicators for quality control workflows

This design allows the system to plug into existing manufacturing or QC pipelines
without tight coupling.

---

## Modularity & Extensibility

The architecture intentionally separates:

- Model inference
- Business rules
- System integration

This enables:
- Independent scaling of inference workloads
- Safer model upgrades
- Easier testing and maintenance
- Clear ownership boundaries between ML and platform teams

---

## Scope & Constraints

This repository contains a **representative subset** of the overall system.

The following components are intentionally excluded due to confidentiality,
licensing, and size constraints:

- Model training pipelines
- Datasets and annotations
- Trained model weights
- Internal deployment and orchestration configurations

The included code and documentation focus on the **engineering of the inference layer**
and its integration into a real-world inspection system.

---

## Summary

This architecture reflects how computer vision systems are typically embedded
into production manufacturing environments—prioritizing robustness, clarity,
and maintainability over experimentation or rapid prototyping.
