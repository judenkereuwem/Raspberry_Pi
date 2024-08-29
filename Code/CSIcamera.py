
#!/usr/bin/python3

import cv2
from picamera2 import Picamera2
from cvzone.FPS import FPS


cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
##picam2.preview_configuration.main.size = (640,480)
##picam2.preview_configuration.main.format = "RGB888"
##picam2.preview_configuration.controls.FrameRate=40
##picam2.preview_configuration.align()
##picam2.configure("preview")
picam2.start()

while True:
    im = picam2.capture_array()
    image=cv2.resize(im,(640,480))

    image = cv2.flip(image, -1)

    

    fps = fpsReader.update()

    print(fps)

    cv2.imshow("Camera", im)
    cv2.waitKey(1)
