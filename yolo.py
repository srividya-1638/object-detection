from ultralytics import YOLO
print("YOLOv10 ready")

model = YOLO("yolov10n.pt")

# Image detection
results = model("dog.jpg", conf=0.4)
results[0].show()

# Video detection
results = model("video.mp4", conf=0.4)
results[0].show()