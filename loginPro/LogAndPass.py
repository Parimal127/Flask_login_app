from flask import Flask,render_template,jsonify,request
import json
app=Flask(__name__)

@app.route('/info',methods=['GET'])
def send():
    if request.method=='GET': 
        cred={'logid':'parimal','password':'pcrox'}
        
        return json.dumps(cred)
    

if __name__=='__main__':
    app.run(debug=True)

