from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # You can change to 'yolov8s.pt', 'yolov8m.pt', etc.

# Define correct training parameters
train_params = {
    "data": "data.yaml",  # Path to dataset config file
    "epochs": 3,         # Number of training epochs
    "batch": 16,          # Batch size
    "imgsz": 640,         # Input image size
    "lr0": 0.01,          # Initial learning rate (corrected)
    "weight_decay": 0.0005,  # L2 regularization factor
    "momentum": 0.937,    # Momentum value
    "device": "cuda",     # Change to 'cpu' if not using GPU
    "workers": 2,         # Number of CPU workers
    "patience": 10,       # Early stopping patience
    "optimizer": "SGD",   # Optimizer type
}

# Train the model
results = model.train(**train_params)

# Save model after training (optional)
model.export(format="onnx")  # Save model in ONNX format if needed
#export_formats = ["onnx", "torchscript", "engine", "coreml", "tflite"]

#for fmt in export_formats:
#    try:
#        model.export(format=fmt)
#        print(f"Model successfully exported in {fmt} format.")
#    except Exception as e:
#        print(f"Error exporting model in {fmt} format: {e}")
