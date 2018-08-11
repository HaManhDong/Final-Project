import requests
import os

url = "http://192.168.60.238:9090/"

# files = [
#     ('10.jpg', open('faces/10.jpg', 'rb')),
#     ('11.jpg', open('faces/11.jpg', 'rb')),
#     ('12.jpg', open('faces/12.jpg', 'rb')),
#     ('13.jpg', open('faces/13.jpg', 'rb')),
# ]
r = requests.get(url)
print r
# print(os.path.join('/home/donghm/git/final/Final-Project/', 'opencv/faces/'))
