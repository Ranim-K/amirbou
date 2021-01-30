#code by amirbou
import cv2 #OpenCV
import pyautogui
import numpy as np


codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Recorded.avi", codec , 60, (1366, 768)) #Here screen resolution is 1366 x 768, you can change it depending upon your need
cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270) #Here we are resizing the window to 480x270 so that the program doesn't run in full screen in the beginning



while True:
    img = pyautogui.screenshot() #capturing screenshot
    frame = np.array(img) #converting the image into numpy array representation 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting the BGR image into RGB image
    out.write(frame) #writing the RBG image to file
    cv2.imshow('Recording', frame) #display screen/frame being recorded
    if cv2.waitKey(1) == ord('q'): #Wait for the user to press 'q' key to stop the recording
        break

out.release() #closing the video file
cv2.destroyAllWindows() #destroying the recording window