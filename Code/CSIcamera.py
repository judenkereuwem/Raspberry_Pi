
#!/usr/bin/python3
#sudo apt install -y libcamera-dev


import cv2
from picamera2 import Picamera2
import time

# Global variables to calculate FPS
fps = 0
frame_count = 0
start_time = time.time()

cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

while True:
    im = picam2.capture_array()
    image=cv2.resize(im,(640,480))

    #image = cv2.flip(image, -1)

    # Calculate the time taken for this frame
    frame_count += 1
    elapsed_time = time.time() - start_time
    
    # Calculate the FPS every second
    if elapsed_time > 1:
        fps = frame_count / elapsed_time
        frame_count = 0
        start_time = time.time()

    # Show the FPS
    cv2.putText(image, f"FPS: {fps:.2f}", (24, 50), cv2.FONT_HERSHEY_DUPLEX,
                1, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow("Camera", image)
    cv2.waitKey(1)
