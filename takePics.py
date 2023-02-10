#This is a super simple Python script that opens the webcam and takes 5 pictures of the user
#I'm using the gathered images to train a model that will eventually be able to recognise the user 
#Here's how it should work:
#-webcam launches
#-detects faces in frame
#-labels "Seán (me)" or "Soph (housemate)" or "Unknown"
#-allow "Unknown" to be added to database if wanted


import cv2
import os

# Open the webcam
cap = cv2.VideoCapture(0)

# Create a folder to save the images
folder = "user_images"
if not os.path.exists(folder):
    os.makedirs(folder)

# Loop over the number of images to capture
for i in range(5):
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Show the frame on the screen
    cv2.imshow("Webcam", frame)

    # Ask the user to enter a label for the image
    label = input(f"Enter label for image {i}: ")

    # Save the frame as an image with the label as the filename
    filename = f"{folder}/{label}_{i}.jpg"
    cv2.imwrite(filename, frame)

    # Wait for a key press
    cv2.waitKey(500)

# Release the webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()

