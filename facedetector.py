import cv2

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier(r"C:\Users\sean2\OneDrive\Desktop\Python Projects\haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(r"C:\Users\sean2\OneDrive\Desktop\Python Projects\haarcascade_fullbody.xml")

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read the frames from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the frame with the faces
    cv2.imshow('Face Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy the windows
cap.release()
cv2.destroyAllWindows()
