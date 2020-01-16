from flask import Flask, escape, request
import pickle, os
import math
import urllib.request
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

app = Flask(__name__)

# set FLASK_APP=main.py
# flask run

@app.route('/', methods=['post'])
def hi():
    return '안녕~'



@app.route('/namecard', methods=['post'])
def namecard():
    body = request.json

    url = body['action']['detailParams']['asd']['origin']
    print (url)

    urllib.request.urlretrieve(url, 'namecard.png')

    img = cv2.imread('namecard.png')
    img_copy = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(gray, (9,9), 0)
    _, binary = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)

    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=7)

    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #RETR_EXTERNAL:외곽만

    # print(len(contours))

    length = cv2.arcLength(contours[0], True)  #도형 윤곽 길이, 폐곡선 여부 True
    approx = cv2.approxPolyDP(contours[0], 0.02 * length, True) #얼마나 꺾이는지 확인, 꼭지점 위치
    cv2.drawContours(img_copy, [approx], -1, (0,255,0),5)

    # imshow('', img_blur)
    # imshow('', binary)
    # imshow('', opening)
    # imshow('', img_copy)

    height, width = img.shape[:2]
    point_list = approx
    pts1 = np.float32([list(point_list[1]),
                    list(point_list[0]),
                    list(point_list[2]),
                    list(point_list[3])])

    # print(pts1)
    pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
    # print(pts2)
    M = cv2.getPerspectiveTransform(pts1, pts2)
    # print(M)
    img_result = cv2.warpPerspective(img, M, (width, height))
    # imshow('', img_result)
    str = pytesseract.image_to_string(img_result)
    print(str)
    return {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": str
                }
            }
        ]
    }
}


# @app.route('/')
# def helloworld():
#     return 'hello world!'

# db = {}
# if os.path.isfile('db.bin'):
#     with open('db.bin', 'rb') as f:
#         db = pickle.load(f)

# id = 0
# if os.path.isfile('id.bin'):
#     with open('id.bin', 'rb') as f:
#         id = pickle.load(f)

# @app.route('/users', methods=['POST'])
# def create_user():
#     # body = ...
#     # todo body에 id를 넣어준다.
#     global id
#     body = request.get_json()
#     body['id']=id
#     db[str(id)]=body
#     id += 1
#     with open('db.bin', 'wb') as f:
#         pickle.dump(db, f)
#     with open('id.bin', 'wb') as f:
#         pickle.dump(id, f)
#     return body


# @app.route('/users/<id>', methods=['GET'])
# def select_user(id):
#     return db[id]

# @app.route('/users/<id>', methods=['DELETE'])
# def delete_user(id):
#     del db[str(id)]
#     with open('db.bin', 'wb') as f:
#         pickle.dump(db, f)
#     return '삭제되었습니다.'

# @app.route('/users/<int:id>', methods=['PUT'])
# def put_user(id):
#     body = request.get_json()
#     body['id'] = id
#     del db[str(id)]
#     db[str(id)] = body
#     with open('db.bin', 'wb') as f:
#         pickle.dump(db, f)
#     return body