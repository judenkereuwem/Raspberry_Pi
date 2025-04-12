from ultralytics import YOLO
from picamera2 import Picamera2
import cv2

# Load YOLOv8 model (replace 'best.pt' with your custom model)
model = YOLO("best.pt")

# Initialize Pi Camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

# Start live detection
while True:
    # Capture frame from Pi Camera
    frame = picam2.capture_array()

    # Run inference
    results = model(frame)

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Display result using OpenCV
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
