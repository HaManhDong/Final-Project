#!/usr/bin/env python
import cv2
import time

if __name__ == "__main__":
    # find the webcam
    capture = cv2.VideoCapture(0)

    # video recorder
    fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
    videoOut = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

    start_time = time.time()
    seconds = 15

    # record video
    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            videoOut.write(frame)
            # cv2.imshow('Video Stream', frame)

        else:
            break

        current_time = time.time()
        if (current_time - start_time) >= seconds:
            break

        # Tiny Pause
        key = cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    videoOut.release()
    # cv2.destroyAllWindows()