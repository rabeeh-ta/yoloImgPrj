import os
import cv2
from ultralytics.models.yolo.model import YOLO
import io
import contextlib


# Create a string buffer
buffer = io.StringIO()

# Load YOLO model
model_path = os.path.join('.', 'models','last.pt')
model = YOLO(model_path)

# Redirect stdout to the buffer
with contextlib.redirect_stdout(buffer):
    result = model.predict(source="0", show=True)


# Get the output
output = buffer.getvalue()
print("from variable", output)
