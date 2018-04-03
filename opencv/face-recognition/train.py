#!/usr/bin/python

# Import the required modules
import cv2, os, sys
import numpy as np
from PIL import Image


width_resize = 300
height_resize = 300


def get_images_and_labels(path, faceCascade, sz=None):
    images = []
    labels = []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            print "*********", subject_path
            count = 0
            label = subject_path.split('/')[2]
            label = int(label)
            for filename in os.listdir(subject_path):
                print subject_path + "/" + filename
                try:
                    image_path = os.path.join(subject_path, filename)

                    image = cv2.imread(image_path)
                    cv2.imshow("Training on image...", image)
                    cv2.waitKey(100)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(image)

                    # pilImage = Image.open(image_path).convert('L')
                    # image = np.array(pilImage, 'uint8')
                    # faces = faceCascade.detectMultiScale(image)

                    if len(faces) == 1:
                        count += 1
                        print " has image"
                        images.append(cv2.resize(image, (width_resize, height_resize)))
                        labels.append(label)
                except IOError:
                    # print "I/O error({0}): {1}".format(errno, strerror)
                    print "I/O error({0}): {1}"
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            print "number image: ", count
    return images, labels


def train(path, recognizer, faceCascade, threshold):
    t = str(threshold).split('.')[0]
    images, labels = get_images_and_labels(path, faceCascade)
    recognizer.train(images, np.array(labels))
    recognizer.save('./train_2_' + t + '.yml')


if __name__ == '__main__':
    cascadePath = "../haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    threshold = 6
    path_train = './training-data'

    # recognizer = cv2.createEigenFaceRecognizer(10)
	# recognizer = cv2.createFisherFaceRecognizer()
	# recognizer = cv2.createLBPHFaceRecognizer()
    recognizer = cv2.createEigenFaceRecognizer(200, threshold)
    train(path_train, recognizer, faceCascade, threshold)


