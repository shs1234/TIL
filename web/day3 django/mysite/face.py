from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import matplotlib.pyplot as plt
import face_recognition
import os
from imutils import paths
import pickle

data = pickle.loads(open("known.bin", "rb").read())

def faceverification(fimename):
    image = cv2.imread(fimename)

    boxes = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, boxes)

#     names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = ""
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {} 
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1  #get : 있으면 값을 반환하여 +1 하고, 없으면(최초) 0+1
            name = max(counts, key=counts.get)
#         names.append(name)                             
#     for ((top, right, bottom, left), name) in zip(boxes, names):
#         cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
#         y = top - 15 if top - 15 > 15 else top + 15
#         cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,  0.75, (0, 255, 0), 2)

    return name