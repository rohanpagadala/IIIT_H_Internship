import os
import shutil
from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')
input_dir = "video_frames"
output_dir = "segmented_frames"
os.makedirs(output_dir, exist_ok=True)

image_files = sorted([
    f for f in os.listdir(input_dir)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

for image_file in image_files:
    image_path = os.path.join(input_dir, image_file)
    results = model(image_path, save=True, save_txt=False)
    saved_dir = results[0].save_dir

    for file in os.listdir(saved_dir):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            src_file = os.path.join(saved_dir, file)
            dst_file = os.path.join(output_dir, file)
            shutil.copy2(src_file, dst_file)

shutil.rmtree("runs", ignore_errors=True)
print(f"✅ Segmented images saved to: {output_dir}")
