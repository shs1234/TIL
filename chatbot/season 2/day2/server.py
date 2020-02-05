from flask import Flask, request, jsonify
import requests
import json
import urllib
from bs4 import BeautifulSoup

def getWeather(city):
    url = 'https://search.naver.com/search.naver?query='
    url = url+urllib.parse.quote_plus(city+' 날씨')
    print(url)
    bs=BeautifulSoup(requests.get(url).text, 'html.parser')
    temp = bs.select('span.todaytemp') 
    desc = bs.select('p.cast_txt')
    
#     return temp[0].text + '˚/' + desc[0].text
#     딕셔너리로 리턴하는걸 선호함. 쓰는놈이 변형해서 쓸 수 있기때문
    return {'temp':temp[0].text, 'desc':desc[0].text} 

app = Flask(__name__)

@app.route('/') #데코레이터. 아래 함수의 위 아래로 특정한 코드를 붙여줌.
def home():

    return 'hello^^'

@app.route('/weather')
def weather():
    city = request.args.get('city')
    info = getWeather(city)
    
    return jsonify(info)
    # return '<font color=red>' + info['desc'] + '</font>'

@app.route('/dialogflow', methods=['POST', 'GET'])
def dialogflow():
    res = {'fulfillmentText':'hello!'}
    return jsonify(res)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) # 0.0.0.0 : 자기 아이피 저절로 채워줌.