# -*- coding: utf-8 -*-
"""yolo_on_coco.ipynb

"""

# !pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="your api key")
project = rf.workspace("").project("my-first-project-vfy2c")
version = project.version(1)
dataset = version.download("yolov9")



# !pip install ultralytics

from ultralytics import YOLO

# Load YOLOv10 model (pre-trained)
model = YOLO("yolov10s.pt")

# Train the model
model.train(data="/content/My-First-Project-1/data.yaml", epochs=100, imgsz=640, batch=8)

print("✅ Training completed!")

