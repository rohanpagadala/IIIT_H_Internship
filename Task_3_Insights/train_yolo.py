from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(
    data='african_wildlife/african_wildlife.yaml',  # relative path to yaml file
    epochs=15,
    imgsz=640,
    batch=16,
    name='african_wildlife_yolov8n'
)
