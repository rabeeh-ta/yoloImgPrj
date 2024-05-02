import os
# from ultralytics.models.yolo.model import YOLO
from ultralytics import YOLO


# Load YOLO model
model_path = os.path.join('.', 'models','last.pt')
model = YOLO(model_path)

result = model.predict(source="0", show=True)