from ultralytics import YOLO
import cv2

model = YOLO("YOLOv11_weights/yolo11n.pt") 
results = model("Videos/cars.mp4")
results[0].show()
#cv2.waitKey(0)
