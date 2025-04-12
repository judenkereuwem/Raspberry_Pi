
import cv2
import os

# Define the folder path
save_folder = "captured_images"

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)

img_count = 0  # To count and label saved images

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame to 224x224
    frame_resized = cv2.resize(frame, (224, 224))

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


