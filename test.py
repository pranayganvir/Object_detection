from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np
 


model = YOLO(r'best.pt')


image_path = r'BloodImage_00000.jpg'

results = model(image_path)

#Show Result
for result in results:
    img = result.plot()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# img = plt.imread(image_path)
# plt.imshow(img)
# plt.axis('off')
# plt.show()