import cv2
import numpy as np

# Load the video
video = cv2.VideoCapture("traffic.mp4")

# Define the background subtractor object
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Read the first frame
_, first_frame = video.read()

# Convert the first frame to grayscale
gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# Define the region of interest (ROI)
roi = cv2.selectROI(first_frame)

# Define the number of frames to process
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize an array to store the sum of pixel intensities in the ROI
intensity_sum = np.zeros(num_frames)

# Process each frame
for i in range(num_frames):
    # Read the next frame
    _, frame = video.read()

    # Apply the background subtractor to the frame
    foreground_mask = background_subtractor.apply(frame)

    # Convert the foreground mask to grayscale
    foreground_mask = cv2.cvtColor(foreground_mask, cv2.COLOR_GRAY2BGR)

    # Extract the ROI from the foreground mask
    roi_mask = foreground_mask[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    # Convert the ROI to grayscale
    roi_mask = cv2.cvtColor(roi_mask, cv2.COLOR_BGR2GRAY)

    # Sum the pixel intensities in the ROI
    intensity_sum[i] = np.sum(roi_mask)

# Find the frame with the maximum intensity sum
max_intensity_frame = np.argmax(intensity_sum)

# Print the result
print("The heaviest traffic is in frame", max_intensity_frame)
