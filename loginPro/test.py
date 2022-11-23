import json
import requests

api_url='http://127.0.0.1:5000/info'
str_data=requests.get(api_url).text
data=json.loads(str_data)
print(data)
print(data['logid'])
