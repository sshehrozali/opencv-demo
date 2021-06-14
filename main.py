# OpenCV based program to use PC/Laptop web cam

import cv2      # Import OpenCV Library

video = cv2.VideoCapture(0)     # Open default Webcam

while True:
    ret, img = video.read()     # Read video
    cv2.imshow("Frame", img)    # Show video frame
    
    key = cv2.waitKey(1)        # Breaks the loop if 'q' is pressed
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()