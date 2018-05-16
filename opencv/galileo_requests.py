import requests
import os

url = "http://localhost:8000/pas/api/server-auth/"

files = [
    ('10.jpg', open('faces/10.jpg', 'rb')),
    ('11.jpg', open('faces/11.jpg', 'rb')),
    ('12.jpg', open('faces/12.jpg', 'rb')),
    ('13.jpg', open('faces/13.jpg', 'rb')),
]
context = {'card_id': '96 42 A9 AC'}
r = requests.post(url, files=files, data=context)
print r
# print(os.path.join('/home/donghm/git/final/Final-Project/', 'opencv/faces/'))
