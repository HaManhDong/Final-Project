import os

from enum import IntEnum

from server import settings

TMP_FOLDER = os.path.join(settings.BASE_DIR, 'images/tmp/')
EIGENFACES_FOLDER = os.path.join(settings.BASE_DIR, 'pas/eigenfaces/')
FACE_TRAIN_FOLDER = os.path.join(settings.BASE_DIR, 'pas/member_images/')
FACE_CASCADE_PATH = os.path.join(settings.BASE_DIR, 'pas/haarcascade_frontalface_default.xml')

VIDEO_PATH = os.path.join(settings.BASE_DIR, 'images/video/')

TRAIN_FACES_FOLDER_NAME = 'train_faces'
TEST_FACES_FOLDER_NAME = 'test_faces'

NUMBER_COMPONENT = 200

MQTT_AUTH_TOPIC = "pas/mqtt/icse/auth"
MQTT_LATEST_USER_SCAN = 'pas/mqtt/server/latest_scan'


class MemberType(IntEnum):
    student = 1
    teacher = 2
