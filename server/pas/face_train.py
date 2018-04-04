#!/usr/bin/python

# Import the required modules
import cv2, os, sys
import numpy as np

from server import settings

FACE_CASCADE_PATH = os.path.join(settings.BASE_DIR, 'pas/haarcascade_frontalface_default.xml')
FACE_TRAIN_FOLDER = os.path.join(settings.BASE_DIR, 'pas/faces_train/')
EIGENFACES_FOLDER = os.path.join(settings.BASE_DIR, 'pas/eigenfaces/')

NUMBER_COMPONENT = 200

width_resize = 100
height_resize = 100


def get_images_and_labels(label, faceCascade):
    path_faces = os.path.join(FACE_TRAIN_FOLDER, str(label))
    images = []
    labels = []
    count = 0
    for dirname, dirnames, filenames in os.walk(path_faces):
        for filename in filenames:
            try:
                image_path = os.path.join(path_faces, filename)
                image = cv2.imread(image_path)
                # cv2.imshow("Training on image...", image)
                # cv2.waitKey(100)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # faces = faceCascade.detectMultiScale(image)
                #
                # if len(faces) == 1:
                #     count += 1
                #     images.append(cv2.resize(image, (width_resize, height_resize)))
                #     labels.append(label)
                count += 1
                images.append(cv2.resize(image, (width_resize, height_resize)))
                labels.append(label)
            except IOError:
                print("I/O error({0}): {1}")
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise
        print("number image: ", count)
    return images, labels


def train(label):
    faceCascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
    images, labels = get_images_and_labels(label, faceCascade)

    recognizer = cv2.face.EigenFaceRecognizer_create(NUMBER_COMPONENT)
    recognizer.train(images, np.array(labels))
    recognizer.save(os.path.join(EIGENFACES_FOLDER, str(label) + ".yml"))


if __name__ == '__main__':
    path_train = 11

    train(path_train)
