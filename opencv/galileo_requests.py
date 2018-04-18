import requests
import os

url = "http://localhost:8000/pas/api/server-auth/"

files = [
    ('16.jpg', open('faces/16.jpg', 'rb')),
    ('17.jpg', open('faces/17.jpg', 'rb')),
    ('18.jpg', open('faces/18.jpg', 'rb')),
]
context = {'card_id': '5D 3F FE E9'}
r = requests.post(url, files=files, data=context)
print r
# print(os.path.join('/home/donghm/git/final/Final-Project/', 'opencv/faces/'))
