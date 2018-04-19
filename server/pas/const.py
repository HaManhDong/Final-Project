import os
from server import settings

TMP_FOLDER = os.path.join(settings.BASE_DIR, 'images/tmp/')
EIGENFACES_FOLDER = os.path.join(settings.BASE_DIR, 'pas/eigenfaces/')
FACE_TRAIN_FOLDER = os.path.join(settings.BASE_DIR, 'pas/faces_train/')
FACE_CASCADE_PATH = os.path.join(settings.BASE_DIR, 'pas/haarcascade_frontalface_default.xml')


NORMAL_FACES_FOLDER_NAME = 'normal_faces'
SMILE_FACES_FOLDER_NAME = 'smile_faces'
CLOSED_EYE_FACES_FOLDER_NAME = 'closed_eye_faces'
NO_GLASS_FACES_FOLDER_NAME = 'no_glass_faces'
TEST_FACES_FOLDER_NAME = 'test_faces'

NUMBER_COMPONENT = 200
