import cv2
import time

# Global variables to calculate FPS
fps = 0
frame_count = 0
start_time = time.time()

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    # Calculate the time taken for this frame
    frame_count += 1
    elapsed_time = time.time() - start_time
    
    success, img = cap.read()

    # Calculate the FPS every second
    if elapsed_time > 1:
        fps = frame_count / elapsed_time
        frame_count = 0
        start_time = time.time()

    # Show the FPS
    cv2.putText(img, f"FPS: {fps:.2f}", (24, 50), cv2.FONT_HERSHEY_DUPLEX,
                1, (0, 255, 0), 1, cv2.LINE_AA)
                
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
