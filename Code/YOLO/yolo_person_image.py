from ultralytics import YOLO
import cv2


# Load the YOLO model (replace with custom model if needed)
model = YOLO("yolo11n.pt")  

# Load image
image_path = "Images/1.png"  # Change to your image file path
image = cv2.imread(image_path)

# Run YOLO inference
results = model(image)

for result in results:
    for box in result.boxes:
        cls = int(box.cls[0])  # Class ID
        conf = float(box.conf[0])  # Confidence score
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates

        # Filter only "person" class (COCO class 0)
        if cls == 0:
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f"Person {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show output image
cv2.imshow("YOLO11 Person Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output image
cv2.imwrite("output.jpg", image)  # Saves the detected image
