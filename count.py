import face_recognition
import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import random

def postFunc(data, optNum):
    num = 1
    while num != 140:
        if (optNum == 1):
            ref.child(str(num)).update({
                'lon': data['location'][num - 1].split(",")[0],
                'lat': data['location'][num - 1].split(",")[1],
                'weight': (data['value'][num - 1] + 1) * 40 + random.randrange(-1000, 1000) / 100
            })
        else:
            ref.child(str(num)).update({
                'weight': (data['value'][num - 1] + 1) * 40 + random.randrange(-1000, 1000) / 100
            })
        num+=1

#Initialize Dict and camera data
data = {'id': [], 'location': [], 'value':[]}
cameradata = pd.read_csv("Cameras_Data.csv")

#Initialize Video
videoName = "samplevideo.mp4"
video = cv2.VideoCapture(videoName)

#Get Certification
cred = credentials.Certificate('cert.json')

# Initialize the app with a custom auth variable
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://distancebetter.firebaseio.com/',
})

ref = db.reference('location')

# num = 1
# while num != 140:
#     ref.child(str(num)).set({
#         'long': data['location'][0].split(",")[0],
#         'lat': data['location'][0].split(",")[1],
#         'value': data['value'][0]
#     })
#     num+=1

#while True:
y = 1
while y != 99:
    x = 1
    while x!=140:
        video.set(cv2.CAP_PROP_POS_FRAMES, x * 100 - y)
        ret, frame = video.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        if (len(data['id']) < 140):
            data['id'].append(x)
            templat = cameradata['LATITUDE'][x]
            templong = cameradata['LONGITUDE'][x]
            data['location'].append(str(templat) + "," + str(templong))
            data['value'].append(len(face_locations))
        else:
            data['value'][x] = len(face_locations)
        x+=1
    postFunc(data, y)
    y+=1
