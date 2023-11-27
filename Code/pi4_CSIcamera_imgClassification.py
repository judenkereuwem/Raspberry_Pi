
#!/usr/bin/python3

import cv2
import cvzone
from cvzone.ClassificationModule import Classifier
from picamera2 import Picamera2
import time

# Initialize variables for frame rate calculation
start_time = time.time()
frame_count = 0

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()


myClassifier = Classifier('MyModel/keras_model.h5','MyModel/labels.txt')
#fpsReader = cvzone.FPS()

while True:

    img = picam2.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    prediction = myClassifier.getPrediction(img)
    print(prediction[1])
    
    
    # Increment frame count
    frame_count += 1

    # Calculate frame rate every second
    if time.time() - start_time >= 1:
        fps = frame_count / (time.time() - start_time)
        print(f"FPS: {fps:.2f}")
        start_time = time.time()
        frame_count = 0
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
                

