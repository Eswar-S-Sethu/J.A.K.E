import cv2
import numpy as np
from PIL import Image
import os


def load_known_faces(known_faces_dir):
    known_faces = []
    known_names = []

    for file in os.listdir(known_faces_dir):
        if file.endswith(".jpg") or file.endswith(".png"):
            image_path = os.path.join(known_faces_dir, file)
            known_image = cv2.imread(image_path)
            known_image = cv2.resize(known_image, (96, 96))  # Resize for FaceNet
            known_faces.append(known_image)
            # Use the filename (without extension) as the person's name
            known_names.append(os.path.splitext(file)[0])

    return known_faces, known_names


def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (96, 96))  # Resize for FaceNet
    image = image.astype("float32") / 255.0
    return image


def get_face_embedding(model, face):
    face = preprocess_image(face)
    face = np.expand_dims(face, axis=0)  # Add batch dimension
    embedding = model.predict(face)  # Get the face embedding
    return embedding


# Load the DNN model (ensure you have the model file in the correct path)
model = cv2.dnn.readNetFromTorch('C:\\Users\\Eswar\\PycharmProjects\\J.A.K.E\\nn4.small2.v1.t7')  # Adjust the path if needed

# Load the known faces
known_faces_dir = "known_faces"  # Directory where known faces are stored
known_faces, known_names = load_known_faces(known_faces_dir)

# Load the input image
inputImage = input('Enter image name with extension:')
image = Image.open(inputImage)
filename, fileExtension = os.path.splitext(inputImage)
new_image = image.resize((600, 420))
new_image.save('test{et}'.format(et=fileExtension))
pixels = cv2.imread('test{et}'.format(et=fileExtension))

# Detect faces using Haar Cascade
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
bboxes = classifier.detectMultiScale(pixels)

for box in bboxes:
    x, y, width, height = box
    face = pixels[y:y + height, x:x + width]

    # Get the face embedding
    face_embedding = get_face_embedding(model, face)

    # Compare with known faces
    min_dist = float("inf")
    name = "Unknown"

    for known_face, known_name in zip(known_faces, known_names):
        known_face_embedding = get_face_embedding(model, known_face)
        dist = np.linalg.norm(face_embedding - known_face_embedding)  # Calculate Euclidean distance

        if dist < min_dist:
            min_dist = dist
            name = known_name

    # Draw a box around the face and label it
    cv2.rectangle(pixels, (x, y), (x + width, y + height), (0, 0, 255), 2)
    cv2.putText(pixels, name, (x + 6, y + height - 6), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255), 1)

# Display the result
cv2.imshow('Face Detection & Recognition', pixels)
print("Completed successfully!")
cv2.waitKey(0)
cv2.destroyAllWindows()
