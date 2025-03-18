from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np
 


model = YOLO(r'best.pt')


image_path = r'BloodImage_00000.jpg'
# Class names from your dataset (Make sure these match your training data)
class_names = ['Platelets', 'RBC', 'WBC']
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)] 

results = model(image_path)
img = cv2.imread(image_path)
#Show Result
for result in results:
    # print(result)
    # break
    # Loop through detected objects
    for box in result.boxes:
        cls = int(box.cls[0])  # Class index
        conf = box.conf[0].item()  # Confidence score

        # Only draw boxes for detections with confidence ≥ 50%
        if conf >= 0.5:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates

            # Draw bounding box with class-specific color
            cv2.rectangle(img, (x1, y1), (x2, y2), colors[cls], 2)
            label = f"{class_names[cls]} {conf:.2f}"
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[cls], 2)
   # Convert BGR to RGB for displaying
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

# img = plt.imread(image_path)
# plt.imshow(img)
# plt.axis('off')
# plt.show()