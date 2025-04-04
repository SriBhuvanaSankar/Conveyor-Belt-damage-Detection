import cv2
import numpy as np
import os
from pathlib import Path

input_folder = r"F:\Conveyor\Conveyor\no damage"
output_folder = r"F:\Conveyor\Conveyor\no damage cropped"

Path(output_folder).mkdir(parents=True, exist_ok=True)

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

kernel = np.ones((5, 5), np.uint8)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):

        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Could not read image: {image_path}")
            continue
        

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if not contours:
            print(f"No blue regions found in: {filename}")
            continue
        

        largest_contour = max(contours, key=cv2.contourArea)
        
        x, y, w, h = cv2.boundingRect(largest_contour)
        cropped = image[y:y+h, x:x+w]
        
        output_path = os.path.join(output_folder, f"cropped_{filename}")
        cv2.imwrite(output_path, cropped)
        print(f"Processed and saved: {output_path}")

print("Processing complete!")
