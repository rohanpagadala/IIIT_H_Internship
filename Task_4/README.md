YOLOv8 Custom Object Detection (Cup Detection)
This project involves training a YOLOv8 model to detect cups using a custom dataset from Roboflow. The dataset was downloaded in YOLOv8 format and split into training, validation, and test sets.

Training was performed on the yolov8m.pt model for 20 epochs at a resolution of 640×640. After training, the model was evaluated using standard metrics and visual tools.

Methodology

Roboflow was used to download a pre-annotated object detection dataset.
The model was trained using YOLOv8 with default settings on Google Colab.
Evaluation included validation runs, confusion matrix analysis, and prediction testing on new images.

Results

Confusion Matrix: Showed high accuracy and minimal misclassifications for the cup class.
Training Curves: mAP, precision, recall, and loss curves indicated stable convergence by epoch 20.
Prediction Samples: The trained model successfully detected cups in test images with high confidence.
