import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Load the faces dataset
faces = datasets.fetch_olivetti_faces()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(faces.data, faces.target, test_size=0.25, stratify=faces.target)

# Train the support vector machine classifier
clf = SVC(kernel='linear', C=1, random_state=0)
clf.fit(X_train, y_train)

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Launch your webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Crop the face and resize it to 64x64
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (64, 64))

        # Predict the gender of the face
        y_pred = clf.predict(face.reshape(1, -1))[0]

        # Add a text label to the frame indicating the predicted gender
        if y_pred == 0:
            gender = "Woman"
        else:
            gender = "Man"
        cv2.putText(frame, gender, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the frame with the predicted gender
    cv2.imshow("Webcam", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
