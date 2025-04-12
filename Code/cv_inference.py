import numpy as np
import tflite_runtime.interpreter as tflite
import cv2
from picamera2 import Picamera2
import time

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path="model_unquant.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Model input dimensions
frame_width, frame_height = input_details[0]['shape'][1], input_details[0]['shape'][2]

def preprocess_frame(frame):
    # Resize and normalize the frame to match model input size
    img = cv2.resize(frame, (frame_width, frame_height))
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img.astype(np.float32) / 255.0  # Normalize to range [0,1]
    return img

def predict_from_picamera2():
    # Initialize Picamera2
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (640, 480)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.configure("preview")
    picam2.start()
    
    time.sleep(2)  # Allow camera to warm up
    print("Press 'q' to quit.")
    
    while True:
        # Capture frame-by-frame
        frame = picam2.capture_array()
        
        # Preprocess the frame
        img = preprocess_frame(frame)
        
        # Set the tensor to the input image
        interpreter.set_tensor(input_details[0]['index'], img)
        
        # Run inference
        interpreter.invoke()
        
        # Get the output prediction
        output_data = interpreter.get_tensor(output_details[0]['index'])
        predicted_class = np.argmax(output_data)
        
        # Display the prediction on the frame
        cv2.putText(frame, f"Predicted class: {predicted_class}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Show the frame with prediction
        cv2.imshow("Camera Inference", frame)
        
        # Quit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    picam2.stop()
    cv2.destroyAllWindows()

# Run the inference
predict_from_picamera2()
