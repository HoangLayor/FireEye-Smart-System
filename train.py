import wandb
import os
from ultralytics import YOLO

wandb.login(key=os.getenv("WANDB_API_KEY"))
model = YOLO("yolov10m.pt")

train_data_path = "data/data.yaml"
model.train(data=train_data_path, epochs=100, project='fire_smoke', name='yolov10m_v2_06') # connect to W&B
