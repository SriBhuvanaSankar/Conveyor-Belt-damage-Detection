# Conveyor-Belt-damage-Detection
<h3>Using YOLOV8 to detect and segment the damage in the conveyor belt. with preprocessing</h3>

We have worked on a confidential dataset from NLC, so the dataset cannot be added in this project

<b>Step-1:</b>
First to avoid external disturbance in the image we cropped conveyor belt from the rest of the image using Cropping_belt.py
by setting the color range of our dataset

<b>Step-2:</b>
For further annotation purpose we applied Canny edge Detection and Morphological Dilation to get a Ground truth,, which help in identify the damage. Here we used Ground_truth.py

<b>Step-3:</b>
We manually annotated the Damage using Makesense.ai and Exported annotation in yolo supported format

<b>Step-4:</b> 
Created Data.yaml for model training

<b>Step-5:</b>
Train the model usinf Train.py
