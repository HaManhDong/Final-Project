import cv2, os, sys
import numpy as np
from PIL import Image

width_resize = 300
height_resize = 300

image_path = 'test-data/1.jpg'
label = 1


def test_recognition(faceCascade, image_path, label):
    try:
        image = cv2.imread(image_path)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_image = cv2.resize(image[y:y + h, x:x + w], (width_resize, height_resize))
            label_predicted, conf = recognizer.predict(face_image)
            print label_predicted
            print conf

        cv2.imshow("Training on image...", image)
        cv2.waitKey(0)

    except IOError:  # print "I/O error({0}): {1}".format(errno, strerror)
        print "I/O error!"
    except:
        print "Unexpected error:", sys.exc_info()[0]

if __name__ == '__main__':
    cascadePath = "../haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    model_path = 'train_2_6.yml'
    recognizer = cv2.createEigenFaceRecognizer()
    recognizer.load(model_path)

    test_recognition(faceCascade, image_path, label)
