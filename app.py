import streamlit as st
import cv2
import numpy as np
import pandas as pd
from ultralytics import YOLO
from PIL import Image


# Load YOLO model
model = YOLO(r"best.pt")  # Ensure best.pt is in the same directory

# Class names (match your dataset)
class_names = ['Platelets', 'RBC', 'WBC']
colors = [(0, 0, 255), (0, 180, 0), (255, 0, 0)]  # Green, Blue, Red for classes

def draw_bounding_boxes(image, results):
    """Draw bounding boxes on the image based on YOLO results."""
    img_with_boxes = image.copy()
    cell_counts = {'RBC': 0, 'WBC': 0, 'Platelets': 0}
    
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])  # Class index
            conf = box.conf[0].item()  # Confidence score

            if conf >= 0.25:  # Only keep detections with confidence ≥ 25%
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                cv2.rectangle(img_with_boxes, (x1, y1), (x2, y2), colors[cls], 2)
                
                # 🔹 Bold font, reduced size, and thickness
                label = f"{class_names[cls]} {conf:.2f}"
                cv2.putText(img_with_boxes, label, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX  , 0.5, colors[cls], 1)
                
                # Increment the count for detected class
                cell_counts[class_names[cls]] += 1
    
    return img_with_boxes, cell_counts

# Streamlit App
st.title("🩸 Blood Cell Detection App 🔬")
st.write("Upload an image to detect RBC, WBC, and Platelets.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    image = np.array(image)  # Convert to NumPy array for OpenCV

    # Save the uploaded image temporarily
    image_path = "temp.jpg"
    cv2.imwrite(image_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    # Run inference
    results = model(image_path)

    # Draw bounding boxes
    img_with_boxes, cell_counts = draw_bounding_boxes(image, results)
    
    # Convert BGR to RGB for display
    # img_with_boxes = cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB)

    # Show only detected image
    st.image(img_with_boxes, caption="Detected Image", use_container_width=False)

    # Display counts in a table
    st.write("### 📊 **Detected Blood Cell Counts**")
    df = pd.DataFrame.from_dict(cell_counts, orient="index", columns=["Count"])
    df.index.name = "Cell Type"
    st.table(df)

    # Option to download the detected image
    cv2.imwrite("detected.jpg", cv2.cvtColor(img_with_boxes, cv2.COLOR_RGB2BGR))
    with open("detected.jpg", "rb") as file:
        st.download_button("Download Detected Image", file, file_name="detected.jpg", mime="image/jpeg")
