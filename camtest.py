import cv2
import numpy as np

def calculate_exposure(frame):
    # Convert the frame to grayscale for simplicity
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the average pixel intensity
    average_intensity = np.mean(gray_frame)

    # You might want to further process this value based on your specific needs

    return average_intensity

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    exposure = calculate_exposure(frame)

    cv2.putText(frame, f'Exposure: {exposure}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
