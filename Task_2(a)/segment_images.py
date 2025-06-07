import os
from ultralytics import YOLO

def segment_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Load YOLOv8 segmentation model
    model = YOLO('yolov8n-seg.pt')  # pretrained segmentation model

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_dir, filename)

            # Run segmentation
            results = model(img_path)

            # Save the segmented image
            result_filename = f"seg_{filename}"
            results[0].save(os.path.join(output_dir, result_filename))

            print(f"Segmented and saved: {result_filename}")

if __name__ == "__main__":
    input_dir = '/Users/rohanpagadala/Desktop/Project/Task_2(a)/images'
    output_dir = '/Users/rohanpagadala/Desktop/Project/Task_2(a)/outputs'

    segment_images(input_dir, output_dir)
