import face_recognition
import cv2
import numpy as np
import random

data = {'id': [], 'location': [], 'value':[]}

videoName = "samplevideo.mp4"

video = cv2.VideoCapture(videoName)
x = 1
y = 1
while y != 99:
    while x!=140:
        video.set(cv2.CAP_PROP_POS_FRAMES, x*100-y)
        ret, frame = video.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        if (y == 1):
            data['id'].append(x)
            templat = random.randrange(4365, 4392)/100
            templong = random.randrange(-8000, -7925)/100
            data['location'].append(str(templat) + "," + str(templong))
            data['value'].append(len(face_locations))
        else:
            data['value'][x] = len(face_locations)
        x+=1
    print(data)
    y+=1
