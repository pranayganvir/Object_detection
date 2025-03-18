# 🩸 Blood Cell Detection App 🔬

## 📌 Overview
The **Blood Cell Detection App** is a Streamlit-based application that allows users to upload an image and detect different types of blood cells (🟥 RBCs, 🔵 WBCs, and 🟡 Platelets) using a YOLO model. The detected image is displayed with bounding boxes and a table showing the count of each cell type. 

The model was trained on the BCCD dataset, with annotations converted to TXT format using Roboflow for YOLO compatibility. The app processes images, draws bounding boxes around detected cells, and displays a count table, providing an efficient tool for blood cell analysis. 🚀.

## ✨ Features
✅ Upload an image for blood cell detection  
✅ Draw bounding boxes around detected 🟥 RBCs, 🔵 WBCs, and 🟡 Platelets  
✅ Display a count table of detected cells  
✅ Option to download the processed image  

## ⚙️ Installation
To run the app locally, follow these steps:

### 1️⃣ Clone the Repository
```sh
https://github.com/pranayganvir/blood-cell-detection-BCCD.git
cd blood-cell-detection-BCCD
```

### 2️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required packages:
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```sh
streamlit run app.py
```

## 📌 Requirements
- 🐍 Python 3.7+
- 🌐 Streamlit
- 📷 OpenCV
- 🔢 NumPy
- 📊 Pandas
- 🖼️ PIL (Pillow)
- 🏆 ultralytics (for YOLO model)

## 🚀 Usage
1️⃣ Upload an image containing blood cells.  
2️⃣ The model processes the image and detects 🟥 RBCs, 🔵 WBCs, and 🟡 Platelets.  
3️⃣ The detected image is displayed with bounding boxes.  
4️⃣ A table shows the count of each type of blood cell.  
5️⃣ Optionally, download the processed image.  

## 📦 Model Details
The application uses a YOLO model (`best.pt`) trained on the **YOLO v10p** framework with the **BCCD dataset**. Ensure the model file is available in the project directory.

- 🔗 **Dataset:** [BCCD Dataset](https://github.com/Shenggan/BCCD_Dataset)
- 📝 **Annotations Converted:** Annotations were converted into the TXT format using [Roboflow](https://roboflow.com/) for compatibility with YOLO.

## 🙌 Acknowledgments
- 📚 Dataset: BCCD Dataset
- 🤖 Model: YOLO v10p
- 🖥️ Framework: Streamlit
- 🛠️ Annotation Conversion: Roboflow

## 📜 License
This project is open-source and available under the MIT License.


## Front UI Interface

![UI Interface](https://github.com/pranayganvir/blood-cell-detection-BCCF/blob/main/Screenshot/Screenshot%202025-03-18%20151342.png)

## Result

![Result !](https://github.com/pranayganvir/blood-cell-detection-BCCF/blob/main/Screenshot/Screenshot%202025-03-18%20151455.png)


## Count Table

![Count Table](https://github.com/pranayganvir/blood-cell-detection-BCCF/blob/main/Screenshot/Screenshot%202025-03-18%20151517.png)

## Downloaded Image

![App Screenshot](https://github.com/pranayganvir/blood-cell-detection-BCCF/blob/main/Screenshot/detected%20(3).jpg)
