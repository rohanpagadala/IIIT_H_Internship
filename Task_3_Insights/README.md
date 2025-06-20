
# African Wildlife Detection using YOLOv8

## Task Description

This project involves training a YOLOv8 object detection model on the **African Wildlife** dataset and interpreting the results from the training process. The dataset includes four common African animals and is used to build a detection model that can identify them accurately.

##  (a) Dataset and Training

**Dataset Link**: [Kaggle - African Wildlife](https://www.kaggle.com/datasets/ultralytics/african-wildlife)  
**YAML File Guide**: [Ultralytics Dataset YAML Guide](https://docs.ultralytics.com/datasets/detect/african-wildlife/#datasetyaml)

This is a **four-class** object detection dataset, containing:
- Buffalo  
- Elephant  
- Rhino  
- Zebra

I stored the training and validation images in **separate folders**, using the YOLO directory structure:

```
datasets/
└── african-wildlife/
    ├── images/
    │   ├── train/
    │   └── val/
    └── labels/
        ├── train/
        └── val/
```

###  Training Setup

I trained the model using **YOLOv8** for **15 epochs** with the following Python code:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Use yolov8s.pt for better accuracy
model.train(data="african-wildlife.yaml", epochs=15, imgsz=640)
```

After training, all results were saved in `runs/detect/train/` (or a folder like `runs/detect/exp/`).

## (b) Interpretation of Graphs and Output

### Confusion Matrix

- **Rows = actual classes**, **Columns = predicted classes**
- Darker cells on the **diagonal** indicate better prediction accuracy
- *Example*: 2 **zebras** were misclassified as **impalas**, which may be due to similar appearance or background

## Box Loss

- Measures accuracy of bounding box prediction
- *Example*: Box loss decreased from **0.09** to **0.03**, showing improved localization of objects

### Class Loss

- Measures the model’s ability to classify correctly
- *Example*: Class loss remained stable around **0.01**, indicating consistent classification confidence
  
### mAP (mean Average Precision)

- Reflects the overall detection accuracy across IoU thresholds
- *Example*: Final **mAP@0.5 = 0.72**, which suggests good detection performance across all four classes

---

## Output Artifacts

After training, the following files were generated inside `runs/detect/train/`:

- `results.png` – Training and validation curves (loss, precision, recall, mAP)
- `confusion_matrix.png` – Visual representation of true vs. predicted labels
- `F1_curve.png`, `P_curve.png`, `R_curve.png` – F1-score, Precision, and Recall over epochs
- `best.pt` – Best-performing weights saved after training

## Summary

- Used **YOLOv8** on a 4-class African wildlife dataset
- Trained for **15 epochs** using properly structured train and val folders
- Interpreted key metrics including **confusion matrix**, **box/class loss**, and **mAP**
