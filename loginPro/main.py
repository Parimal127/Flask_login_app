from flask import Flask,render_template,request
import json
import requests

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

#The fuction is not fully made,It authorize user but not keep him log in. 
@app.route('/auth',methods=['GET','POST'])
def auth():
    if request.method=='POST':
        api_url='http://127.0.0.1:5000/info' #Trial on localhost
        str_data=requests.get(api_url).text
        data=json.loads(str_data)
        if request.form['userid']==data['logid'] and request.form['pass']==data['password'] :
            return render_template('index.html')
        else:
            return render_template('login.html')


if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1', port=5002)
