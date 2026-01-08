"""
infer.py

Minimal inference orchestration for PCB resistor detection.

This script demonstrates how a trained object detection model (e.g. YOLO)
would be integrated into a manufacturing inspection pipeline.

The focus is on:
- input validation
- model interface boundaries
- structured outputs
"""

import argparse
import json
import os
from typing import Dict, List


def validate_inputs(image_path: str) -> None:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Input image not found: {image_path}")

    if not image_path.lower().endswith((".jpg", ".jpeg", ".png")):
        raise ValueError("Input must be an image file (.jpg, .jpeg, .png)")


def load_model(model_dir: str) -> None:
    """
    Placeholder for model loading.

    In a full implementation, this would load:
    - YOLO configuration
    - trained weights
    - class labels
    """
    if not os.path.exists(model_dir):
        raise FileNotFoundError(
            f"Model directory not found: {model_dir}"
        )


def run_inference(image_path: str) -> List[Dict]:
    """
    Placeholder inference routine.

    Returns a list of detection results with the expected schema.
    """
    # Example output structure
    return [
        {
            "component": "resistor",
            "confidence": 0.87,
            "bbox": {"x": 120, "y": 80, "w": 45, "h": 18},
        }
    ]


def save_results(results: List[Dict], output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run inference on a PCB image."
    )
    parser.add_argument("--image", required=True, help="Path to input PCB image")
    parser.add_argument(
        "--model_dir",
        default="models/",
        help="Directory containing model artifacts",
    )
    parser.add_argument(
        "--output",
        default="outputs/detections.json",
        help="Path to write inference results",
    )

    args = parser.parse_args()

    validate_inputs(args.image)
    load_model(args.model_dir)

    detections = run_inference(args.image)
    save_results(detections, args.output)

    print(f"Inference complete. Detections written to {args.output}")


if __name__ == "__main__":
    main()
