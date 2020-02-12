from flask import Flask, render_template, request
import pickle
import yolo

app = Flask(__name__)

listData = [{'id':0, 'img':'book2.jpg', 'title':'책'},
            {'id':1, 'img':'dog.jpg', 'title':'개'},
            {'id':2, 'img':'person.jpg', 'title':'사람'}]

@app.route('/')
def index():
    return render_template('home.html', title='my home page')

@app.route('/image')
def image():    
    return render_template('image.html', listData=listData)

@app.route('/view')   # view?id=1
def view():

    id = request.args.get('id')
    return render_template('view.html', s=listData[int(id)])

@app.route('/fileupload', methods=['POST'])   # fileupload
def fileupload():
    f = request.files['file1']
    f.save('./static/' + f.filename)
    pathname=f'./static/{f.filename}'
    yolo.objectDetect(pathname)
    
    id = listData[len(listData)-1]['id']+1
    title = request.form.get('title')
    listData.append({'id':id, 'img':f.filename, 'title':title})

    return goURL('업로드 완료','/image')

@app.route('/deleteimage')   # deleteimage?id=1
def deleteimage():
    id = int(request.args.get('id'))
    for s in listData:
        if s['id']==id:
            listData.remove(s)
    
    return goURL('삭제 완료','/image')

def goURL(msg, url):
    html = '''
    <script>
        alert('@msg')
        window.location.href='@url'
    </script>
    '''
    html = html.replace('@msg',msg)
    html = html.replace('@url',url)
    
    return html

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)