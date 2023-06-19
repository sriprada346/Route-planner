import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64

# Read the image
img = cv2.imread('image.jpeg')
img = cv2.resize(img, (640, 480))

# Define the points
points = [(150, 50),(150,200,),(190,200),(150, 200), (200, 150), (850, 350)]

# Draw a line through all the points
color = (0, 0, 255)  # BGR color format
thickness = 5
for i in range(len(points)-1):
    pt1 = points[i]
    pt2 = points[i+1]
    cv2.line(img, pt1, pt2, color, thickness)

# Convert the image to PNG format and encode it as base64
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB format
pil_img = Image.fromarray(img)
buffer = BytesIO()
pil_img.save(buffer, format='JPEG')
img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

# Embed the base64-encoded image in an HTML page
html = f"<img src='data:image/jpeg;base64,{img_str}'>"
with open('output.html', 'w') as f:
    f.write(html)
