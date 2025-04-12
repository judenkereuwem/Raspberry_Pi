from ultralytics import YOLO
import cv2
from picamera2 import Picamera2
import time

# Global variables to calculate FPS
fps = 0
frame_count = 0
start_time = time.time()

# Load YOLOv8 model (you can also use 'yolov8n.pt' for a smaller model)
model = YOLO("YOLOv11_weights/yolo11n.pt")  

# Define the classes you want to detect (Example: Person & Car)
target_classes = {0, 2} #0 = person, 2 = Car

# Open webcam or use a video file
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

#while cap.isOpened():
while True:
    # Calculate the time taken for this frame
    frame_count += 1
    elapsed_time = time.time() - start_time
    
    img = picam2.capture_array()
    #frame=cv2.resize(im,(640,480))
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # ret, frame = cap.read()
    # if not ret:
        # break
        
    # Run YOLO inference
    results = model(frame)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0]) # Class ID
            conf = float(box.conf[0])  # Confidence score
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box

            # Filter only "person" class (COCO class 0)
            if cls in target_classes:
                label = f"{model.names.get(cls, 'unkown')} {conf:.2f}"                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Calculate the FPS every second
    if elapsed_time > 1:
        fps = frame_count / elapsed_time
        frame_count = 0
        start_time = time.time()

    # Show the FPS
    cv2.putText(frame, f"FPS: {fps:.2f}", (24, 50), cv2.FONT_HERSHEY_DUPLEX,
                1, (0, 255, 0), 1, cv2.LINE_AA)

    # Show frame
    cv2.imshow("YOLOv11 Person Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


                
cap.release()
cv2.destroyAllWindows()
