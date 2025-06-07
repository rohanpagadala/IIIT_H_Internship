
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

image_url = 'https://ultralytics.com/images/bus.jpg'

results = model(image_url)

results[0].show()
results[0].save(filename='bus_output.jpg')
