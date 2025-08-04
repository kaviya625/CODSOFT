# Face Detection in Google Colab (CodSoft AI Internship - Task 3)

# Step 1: Install and import required packages
!pip install opencv-python

import cv2
import numpy as np
from PIL import Image
import io
from google.colab.patches import cv2_imshow
from google.colab import files

# Step 2: Upload an image
uploaded = files.upload()

# Step 3: Load and convert image
for filename in uploaded.keys():
    image_stream = io.BytesIO(uploaded[filename])
    img = Image.open(image_stream).convert('RGB')
    img_np = np.array(img)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

# Step 4: Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Step 5: Convert image to grayscale and detect faces
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

# Step 6: Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img_cv, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Step 7: Show the result
cv2_imshow(img_cv)
print(f"✅ Detected {len(faces)} face(s) in the image.")
