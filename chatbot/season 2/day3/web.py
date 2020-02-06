from flask import Flask, request, jsonify
import json
from bs4 import BeautifulSoup
import requests
import urllib
import pickle

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cnt=0

@app.route('/')
def home():
    html = '''
    <h1>hello!</h1>
    <img src=/static/yellow.jpg>
    <br>
    <iframe
    allow="microphone;"
    width="350"
    height="430"
    src="https://console.dialogflow.com/api-client/demo/embedded/shs">
    </iframe>
    '''
    return html

@app.route('/counter')
def counter():
    global cnt
    cnt += 1
    sentence=''
    for num in str(cnt):
        sentence += '<img src=/static/'+num+'.png width=60>'
    
    return f'{sentence}명이 방문했습니다.'

@app.route('/weather', methods=['POST','GET'])
def weather():
    # if request.method == 'GET':
    #     req = request.args # args : get방식만 받을 수 있음. 뒤에 ? 표시
    # else :
    #     req = request.form # form : post방식. 보이지 않음.  https://blog.outsider.ne.kr/312
    req = request.args if request.method == 'GET' else request.form

    city = req.get('city')

    return f'{city} 날씨 좋음'

def getQuery(txt) :
    url = 'https://search.naver.com/search.naver?where=kdic&query='
    url = url+urllib.parse.quote_plus(txt)
    print(url)

    bs=BeautifulSoup(requests.get(url).text, 'html.parser')

    output = bs.select('p.txt_box')
    
    return [node.text for node in output]

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

def processDialog(req) :
    
    answer = req['queryResult']['fulfillmentText']
    intentName = req['queryResult']['intent']['displayName'] 
    
    if intentName == 'query' :
        word = req["queryResult"]['parameters']['any'] 
        text = getQuery(word)[0]                
        res = {'fulfillmentText': text}   

    elif intentName=='order2' and req['queryResult']['allRequiredParamsPresent'] == True:
        params=req['queryResult']['parameters']['food_number']
        price = {'짜장면':5000, '짬뽕':10000, '탕수육':20000}
        output = [food.get('number-integer',1)*price[food.get('food')] for food in params]
        text = sum(output)
        res = {'fulfillmentText': text}

    elif intentName=='weather' and req['queryResult']['allRequiredParamsPresent'] == True:
        date = req['queryResult']['parameters']['date']
        geo_city = req['queryResult']['parameters']['geo-city']

        info = getWeather(geo_city)
        text = geo_city+'의 온도는 '+ info['temp']+'°C입니다. '+info['desc']
        res = {'fulfillmentText': text}
    
    else :
        res = {'fulfillmentText': answer}           
        
    return res


@app.route('/dialogflow', methods=['POST','GET'])
def dialogflow():
    
    if request.method == 'GET' :
        file = request.args.get("file")        
        with open(file, encoding='UTF8') as json_file:
            req = json.load(json_file)    
            print(json.dumps(req, indent=4, ensure_ascii=False))            
    else :
        req = request.get_json(force=True)    
        print(json.dumps(req, indent=4, ensure_ascii=False))    
    
    
    return  processDialog(req)

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)