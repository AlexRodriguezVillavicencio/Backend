import requests
import json

from requests.models import Response
url = 'http://127.0.0.1:8000/api/'

headers_post= {'content-type':'application/json'}
data_post = {"usuario":"alexander","password":"alex12345"}
p = requests.post('http://127.0.0.1:8000/api/login', data=json.dumps(data_post),headers=headers_post)


# print(p.text)
response = json.loads(p.text)
token_key = response['token']
print(token_key)

headers = {
    'Authorization' : 'token ' + token_key
}
r = requests.get(url,headers=headers)
print(r.text)