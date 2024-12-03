import numpy as np
import cv2 as cv

# Open video capture
cap = cv.VideoCapture('asim.mp4')

# Read the first frame
ret, frame = cap.read()

# Define the initial position of the tracking window
x, y, height, width = 400, 440, 150, 150
track_window = (x, y, width, height)

# Define the region of interest (ROI)
roi = frame[y:y + height, x:x + width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# Create a mask for the ROI
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# Set termination criteria for the tracking algorithm
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 15, 2)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv.resize(frame, (720, 720), fx=0, fy=0, interpolation=cv.INTER_CUBIC)
    
    # Show original frame
    cv.imshow('Original', frame)

    # Apply thresholding to the frame
    ret1, frame1 = cv.threshold(frame, 180, 155, cv.THRESH_TOZERO_INV)

    # Convert the frame to HSV color space
    hsv = cv.cvtColor(frame1, cv.COLOR_BGR2HSV)

    # Calculate the back projection of the frame using the histogram of the ROI
    dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # Apply CamShift algorithm
    ret2, track_window = cv.CamShift(dst, track_window, term_crit)

    # Get the points of the rotated rectangle and draw it on the frame
    pts = cv.boxPoints(ret2)
    pts = np.int0(pts)
    result = cv.polylines(frame, [pts], True, (0, 255, 255), 2)

    # Show the result
    cv.imshow('Camshift', result)

    # Wait for the ESC key to break the loop
    k = cv.waitKey(30) & 0xFF
    if k == 27:  # ESC key
        break

# Release the video capture and close windows
cap.release()
cv.destroyAllWindows()
