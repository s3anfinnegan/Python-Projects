import cv2

# Create a VideoCapture object to access the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error opening webcam")
    exit()

# Continuously capture and display frames from the webcam
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame")
        break
    
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
