# Computer Vision–Based PCB Quality Control

An affordable computer vision system for automated inspection of resistor placement and values in PCB manufacturing using YOLOv3.

---

## Problem

In small and mid-scale PCB manufacturing, quality inspection is often performed manually due to the high cost of traditional Automated Optical Inspection (AOI) systems. Manual inspection is time-consuming, error-prone, and difficult to scale with increasing production volumes.

This project explores a low-cost, software-driven alternative for detecting incorrect resistor placement and validating resistor values on printed circuit boards using computer vision techniques.

---

## System Overview

The system processes PCB images captured from a manufacturing setup and performs the following steps:

1. Detects resistors on the PCB using a custom-trained YOLOv3 object detection model  
2. Extracts and aligns detected resistor regions  
3. Analyzes resistor color bands to compute resistance values  
4. Compares computed values against expected specifications to generate a pass/fail result  

---

## Pipeline

- **Input:** Static PCB image  
- **Detection:** YOLOv3 trained on a custom PCB component dataset  
- **Post-processing:**
  - Bounding box extraction
  - Image alignment for consistent color-band detection  
- **Resistor Value Computation:**
  - Pixel-level color analysis
  - Mapping detected color bands to resistance values  
- **Output:**
  - Calculated resistance value
  - Inspection result (pass/fail)  

---

## Model & Data

- **Model:** YOLOv3 (custom trained)  
- **Training data:**
  - Manually curated images of PCBs and discrete components
  - Dataset focused primarily on resistor detection  
- **Training environment:**
  - Google Colab with GPU support  

---

## Results

- Resistor detection accuracy of approximately **87%**
- Successfully detected resistor placement and computed resistance values for 4-band resistors
- Performance was sensitive to:
  - Lighting conditions
  - Component orientation and alignment
  - Image quality  

---

## Limitations

- Processes static images only (not real-time)
- Supports only 4-band resistors
- Dataset size was limited due to manual labeling
- Accuracy degrades under inconsistent lighting conditions

---

## Future Improvements

- Extend detection to additional PCB components (capacitors, inductors, ICs)
- Improve robustness using larger and more diverse datasets
- Optimize the pipeline for real-time inference on edge devices
- Integrate results into a cloud-based or edge-based inspection dashboard

---

## Project Context

This project was completed as part of an industry-sponsored B.Tech capstone project focused on applying computer vision techniques to manufacturing quality control.
