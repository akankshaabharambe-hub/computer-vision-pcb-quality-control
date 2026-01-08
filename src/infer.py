"""
infer.py

Minimal inference orchestration for PCB resistor detection.

This script demonstrates how a trained object detection model (e.g., YOLO)
would be integrated into a manufacturing inspection pipeline.

Scope:
- Input validation
- Model artifact checks + interface boundaries
- Structured outputs (JSON)
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import List, Optional


SUPPORTED_EXTS = (".jpg", ".jpeg", ".png")


@dataclass(frozen=True)
class BBox:
    x: int
    y: int
    w: int
    h: int


@dataclass(frozen=True)
class Detection:
    component: str
    confidence: float
    bbox: BBox


@dataclass(frozen=True)
class InferenceResult:
    image: str
    created_at_utc: str
    detections: List[Detection]
    notes: Optional[str] = None


def validate_inputs(image_path: str) -> None:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Input image not found: {image_path}")
    if not image_path.lower().endswith(SUPPORTED_EXTS):
        raise ValueError(f"Input must be an image file: {', '.join(SUPPORTED_EXTS)}")


def ensure_parent_dir(path: str) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def load_model_artifacts(model_dir: str) -> None:
    """
    Validates presence of model artifacts.

    In a full implementation, this would load:
    - model configuration
    - trained weights
    - class labels
    """
    if not os.path.isdir(model_dir):
        raise FileNotFoundError(f"Model directory not found: {model_dir}")

    # These filenames are illustrative conventions (not included in repo).
    expected = ["model.cfg", "model.weights", "classes.names"]
    missing = [f for f in expected if not os.path.exists(os.path.join(model_dir, f))]
    if missing:
        raise FileNotFoundError(
            "Model artifacts missing from model_dir. Expected: "
            + ", ".join(expected)
            + f". Missing: {', '.join(missing)}"
        )


def run_inference(image_path: str, *, dry_run: bool) -> List[Detection]:
    """
    Runs inference and returns structured detections.

    dry_run=True enables a pipeline smoke-test without requiring model artifacts.
    """
    if dry_run:
        return []

    # Intentionally not implemented here to avoid bundling weights/dataset.
    # In a full implementation, this would call the model backend and post-process outputs.
    raise NotImplementedError(
        "Inference backend is not included in this repository. "
        "Run with --dry_run for a pipeline smoke-test."
    )


def save_results(result: InferenceResult, output_path: str) -> None:
    ensure_parent_dir(output_path)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(asdict(result), f, indent=2)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run inference on a PCB image.")
    parser.add_argument("--image", required=True, help="Path to input PCB image")
    parser.add_argument("--model_dir", default="models/", help="Directory containing model artifacts")
    parser.add_argument("--output", default="outputs/detections.json", help="Path to write inference results")
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Smoke-test the pipeline without model artifacts (writes empty detections).",
    )
    args = parser.parse_args()

    validate_inputs(args.image)

    notes = None
    if args.dry_run:
        notes = "dry_run enabled; inference backend and model artifacts are not required."
    else:
        load_model_artifacts(args.model_dir)

    detections = run_inference(args.image, dry_run=args.dry_run)

    result = InferenceResult(
        image=os.path.basename(args.image),
        created_at_utc=utc_now_iso(),
        detections=detections,
        notes=notes,
    )
    save_results(result, args.output)

    print(f"OK: wrote results to {args.output} (detections={len(detections)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
