import os

image_dir = r"E:\Conveyor final\Conveyor\cleaning\damage cropped - Copy"
label_dir = r"E:\Conveyor final\Conveyor\cleaning\yolo_damage_label"

# Rename annotation files
for filename in os.listdir(label_dir):
    if filename.endswith("_mask.txt"):
        new_filename = filename.replace("_mask", "")
        os.rename(os.path.join(label_dir, filename), os.path.join(label_dir, new_filename))

# Remove images without corresponding annotations
image_files = set([f.split(".")[0] for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
label_files = set([f.split(".")[0] for f in os.listdir(label_dir) if f.endswith(".txt")])

images_to_remove = image_files - label_files

for image_name in images_to_remove:
    for image_file in os.listdir(image_dir):
        if image_file.startswith(image_name):
            os.remove(os.path.join(image_dir, image_file))
            print(f"Removed image: {image_file}")

print("File renaming and image cleanup complete.")
