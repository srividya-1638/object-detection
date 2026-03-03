# YOLOv10 Object Detection using Python
This project implements real-time object detection using the YOLOv10 (You Only Look Once) model from the Ultralytics library. 
The system is capable of detecting and classifying objects in both images and videos with high accuracy and speed.
The model automatically identifies multiple objects in a frame and draws bounding boxes with confidence scores.
## Features
- Object detection on images
- Object detection on video files
- Confidence threshold control
- Automatic model download
- Fast and accurate predictions
## Tech Stack
- Python
- Ultralytics YOLOv10
- OpenCV
- PyTorch
## How It Works
- Load YOLOv10 pretrained model
- Provide input image or video
- Model processes frame
- Displays detected objects with labels and confidence
## How to Run
- pip install ultralytics
- python yolo.py
## Sample Output
The model detects objects such as:
Person
Dog
Car
Bicycle
and more (COCO dataset classes)
## Future Improvements
- Real-time webcam detection
- Custom trained model
- Web app deployment
- Object counting system
