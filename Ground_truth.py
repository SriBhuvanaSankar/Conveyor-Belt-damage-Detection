import cv2
import numpy as np
import os
from pathlib import Path

def preprocess_for_groundtruth(image_path, output_dir):
    """Preprocess images and generate ground truth masks for damage detection"""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error loading {image_path}")
        return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 30, 100)

    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=2)
    morph = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    
    _, ground_truth = cv2.threshold(morph, 1, 255, cv2.THRESH_BINARY)
    
    ground_truth = cv2.erode(ground_truth, kernel, iterations=1)
    
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    damage_highlight = img.copy()
    damage_highlight[ground_truth == 255] = (0, 0, 255)  
    
    cv2.imwrite(f"{output_dir}/original/{base_name}.jpg", img)
    cv2.imwrite(f"{output_dir}/ground_truth/{base_name}_mask.png", ground_truth)
    cv2.imwrite(f"{output_dir}/highlighted/{base_name}_highlighted.jpg", damage_highlight)
    
    return ground_truth


input_folder = r"F:/Conveyor/Conveyor/damage cropped"
output_folder = r"F:/Conveyor/Conveyor/ground_truth_data"

Path(output_folder).mkdir(parents=True, exist_ok=True)
Path(f"{output_folder}/original").mkdir(exist_ok=True)
Path(f"{output_folder}/ground_truth").mkdir(exist_ok=True)
Path(f"{output_folder}/highlighted").mkdir(exist_ok=True)

for img_file in os.listdir(input_folder):
    if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        print(f"Processing {img_file}...")
        img_path = os.path.join(input_folder, img_file)
        preprocess_for_groundtruth(img_path, output_folder)

print("Ground truth generation complete! Files saved to:", output_folder)
