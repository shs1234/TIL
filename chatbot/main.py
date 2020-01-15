from flask import Flask, escape, request
import pickle, os

app = Flask(__name__)

# set FLASK_APP=main.py
# flask run

@app.route('/')
def helloworld():
    return 'hello world!'

db = {}
if os.path.isfile('db.bin'):
    with open('db.bin', 'rb') as f:
        db = pickle.load(f)

id = 0
if os.path.isfile('id.bin'):
    with open('id.bin', 'rb') as f:
        id = pickle.load(f)

@app.route('/users', methods=['POST'])
def create_user():
    # body = ...
    # todo body에 id를 넣어준다.
    global id
    body = request.get_json()
    body['id']=id
    db[str(id)]=body
    id += 1
    with open('db.bin', 'wb') as f:
        pickle.dump(db, f)
    with open('id.bin', 'wb') as f:
        pickle.dump(id, f)
    return body


@app.route('/users/<id>', methods=['GET'])
def select_user(id):
    return db[id]

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    del db[str(id)]
    with open('db.bin', 'wb') as f:
        pickle.dump(db, f)
    return '삭제되었습니다.'

@app.route('/users/<int:id>', methods=['PUT'])
def put_user(id):
    body = request.get_json()
    body['id'] = id
    del db[str(id)]
    db[str(id)] = body
    with open('db.bin', 'wb') as f:
        pickle.dump(db, f)
    return body