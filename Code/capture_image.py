
import cv2
import os
from picamera2 import Picamera2
import time

# Define the folder path
save_folder = "captured_images"

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Initialize video capture
#cap = cv2.VideoCapture(0)
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

img_count = 0  # To count and label saved images

while True:
    im = picam2.capture_array()
    frame_resized = cv2.resize(im,(224,224))

    # Display the resized frame
    cv2.imshow("Resized Frame", frame_resized)

    # Save the resized frame on pressing 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        img_name = f"{save_folder}/image_{img_count}.jpg"
        cv2.imwrite(img_name, frame_resized)
        print(f"Saved {img_name}")
        img_count += 1

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


