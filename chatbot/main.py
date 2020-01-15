from flask import Flask, escape, request

app = Flask(__name__)

# set FLASK_APP=main.py
# flask run

db = {}
id = 0

@app.route('/users', methods=['POST'])
def create_user():
    # body = ...
    # todo body에 id를 넣어준다.
    global id
    body = request.get_json()
    body['id']=id
    print(body)
    db[str(id)]=body
    id += 1
    return body

@app.route('/users/<id>', methods=['GET'])
def select_user(id):
    return db[id]

@app.route('/users/<id>', methods=['DELETE'])
def select_user(id):
    del db[id]

# @app.route('/users/<id>', methods=['PUT'])
# def select_user(id):
#     return db[id]


# def hello():
#     name = request.args.get("name", "World")
#     return f'Hello, {escape(name)}!'


@app.route('/hi', methods=['GET','POST'])
def hi():
    return{
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
                    "altText": "보물상자입니다"
                }
            }
        ]
    }
}