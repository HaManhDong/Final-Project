import requests
import os

url = "http://localhost:8000/pas/api/upload-image/"

files = [
    ('face1', open('faces/face_10.jpg', 'rb')),
    ('face2', open('faces/11.jpg', 'rb')),
]
r = requests.post(url, files=files)
# print(os.path.join('/home/donghm/git/final/Final-Project/', 'opencv/faces/'))
