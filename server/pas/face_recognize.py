import cv2, os, sys

from server import settings

TMP_FOLDER = os.path.join(settings.BASE_DIR, 'tmp/')
EIGENFACES_FOLDER = os.path.join(settings.BASE_DIR, 'pas/eigenfaces/')
FACE_CASCADE_PATH = os.path.join(settings.BASE_DIR, 'pas/haarcascade_frontalface_default.xml')

width_resize = 100
height_resize = 100


def recognition(label):
    faceCascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
    model_path = os.path.join(EIGENFACES_FOLDER, str(label) + ".yml")
    recognizer = cv2.face.EigenFaceRecognizer_create()
    recognizer.read(model_path)


    for dirname, dirnames, filenames in os.walk(TMP_FOLDER):
        for filename in filenames:
            try:
                image_path = os.path.join(TMP_FOLDER, filename)
                image = cv2.imread(image_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(image)

                if len(faces) == 1:
                    for (x, y, w, h) in faces:
                        face_image = cv2.resize(image, (width_resize, height_resize))
                        label_predicted, conf = recognizer.predict(face_image)
                        print("{0} - {1} - {2}".format(filename, conf, label_predicted))
            except IOError:
                print("I/O error({0}): {1}")
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise


if __name__ == '__main__':
    recognition(11)
