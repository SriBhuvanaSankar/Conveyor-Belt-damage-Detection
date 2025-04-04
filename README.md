# Conveyor-Belt-Damage-Detection

## Overview
This project focuses on detecting and segmenting damage in conveyor belts using YOLOv8. The system preprocesses images to remove external disturbances and enhances detection through edge-based ground truth generation.

## Dataset
We have used a confidential dataset from NLC; therefore, the dataset cannot be included in this repository.

## Sample Images

![No Damage](https://github.com/SriBhuvanaSankar/Conveyor-Belt-damage-Detection/blob/main/no_damage.jpeg)
![Damage](https://github.com/SriBhuvanaSankar/Conveyor-Belt-damage-Detection/blob/main/damage.jpeg)

## Methodology

### Step 1: Preprocessing
To remove external disturbances, we cropped the conveyor belt region using `Cropping_belt.py` by defining the color range of the dataset.

### Step 2: Ground Truth Generation
For annotation purposes, we applied Canny edge detection and morphological dilation using `Ground_truth.py`. This helped in identifying the damaged areas in the conveyor belt.

### Step 3: Manual Annotation
We manually annotated the damage using [Makesense.ai](https://www.makesense.ai/) and exported the annotations in a YOLO-supported format.

### Step 4: Data Preparation
A `data.yaml` file was created to configure the dataset for YOLOv8 model training.

### Step 5: Model Training
The YOLOv8 model was trained using `Train.py`, leveraging the prepared dataset and annotations.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/SriBhuvanaSankar/Conveyor-Belt-damage-Detection.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run preprocessing:
   ```bash
   python Cropping_belt.py
   ```
4. Generate ground truth:
   ```bash
   python Ground_truth.py
   ```
5. Train the model:
   ```bash
   python Train.py
   ```

## Results
The trained model successfully detects and segments damaged areas on the conveyor belt. Future work includes real-time deployment and further improvements in segmentation accuracy.

---

This README has been updated with the content from the report.

