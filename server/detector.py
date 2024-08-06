import cv2
from utils.constants import *

"""
Author: Huanzhong Ma
Finished Time: 16-6-2024
Function: The detectors of body and face.
Notice: You need to download deep learning models for these detectors.
"""


def get_res(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    body_detect = cv2.CascadeClassifier(BODY_DETECTOR)
    body = body_detect.detectMultiScale(gray, 1.2, 35)
    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    faces_detect = cv2.CascadeClassifier(FACE_DETECTOR)
    face = faces_detect.detectMultiScale(gray, 1.05, 3)
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)



    # resized = cv2.resize(img, (int(img.shape[1] // 3), int(img.shape[0] // 3)))
    resized = img
    return resized