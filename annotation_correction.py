import os
import cv2

def convert_bbox_to_polygon(label_dir, image_dir):
    """
    Converts bounding box annotations in YOLO format to polygon annotations.

    Args:
        label_dir (str): Path to the directory containing YOLO bounding box annotations.
        image_dir (str): Path to the directory containing the corresponding images.
    """

    for filename in os.listdir(label_dir):
        if filename.endswith(".txt"):
            label_path = os.path.join(label_dir, filename)
            image_path = os.path.join(image_dir, filename.replace(".txt", ".jpg"))  # Assuming .jpg images

            if not os.path.exists(image_path):
                image_path = os.path.join(image_dir, filename.replace(".txt", ".png")) # try png
                if not os.path.exists(image_path):
                    print(f"Warning: Image not found for {filename}")
                    continue

            image = cv2.imread(image_path)
            if image is None:
                print(f"Warning: Could not read image {image_path}")
                continue

            height, width, _ = image.shape

            with open(label_path, "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:  # Bounding box format: class x_center y_center width height
                    class_id = parts[0]
                    x_center = float(parts[1]) * width
                    y_center = float(parts[2]) * height
                    bbox_width = float(parts[3]) * width
                    bbox_height = float(parts[4]) * height

                    x_min = int(x_center - bbox_width / 2)
                    y_min = int(y_center - bbox_height / 2)
                    x_max = int(x_center + bbox_width / 2)
                    y_max = int(y_center + bbox_height / 2)

                    # Create a simple polygon (rectangle) from the bounding box
                    polygon_points = [
                        x_min / width, y_min / height,
                        x_max / width, y_min / height,
                        x_max / width, y_max / height,
                        x_min / width, y_max / height,
                    ]

                    new_line = f"{class_id} " + " ".join(map(str, polygon_points)) + "\n"
                    new_lines.append(new_line)
                else:
                    print(f"Warning: Line '{line.strip()}' in {filename} is not in bounding box format. Skipping.")
                    continue

            with open(label_path, "w") as f:
                f.writelines(new_lines)
            print(f"Converted {filename}")

# Example usage:
label_directory = r"D:\CV_damageD\NEW_yolo\datasets\labels\damage"  # Replace with your label directory
image_directory = r"D:\CV_damageD\NEW_yolo\datasets\images\damage" # Replace with your image directory

convert_bbox_to_polygon(label_directory, image_directory)