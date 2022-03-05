import requests
import json
URL="http://127.0.0.1:8000/studentapi/"
def getdata(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
# getdata(18)
def post_data():
    data={
        "name":"Ram",
        "roll":20,
        "city":"lamghadi"
        }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
post_data()
def update_data():
    data={
        'id':5,
        'name':'rani'
        
        }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    dat=r.json()
    print(dat)
# update_data()
def delete_data():
    data={
        'id':12
        }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    dat=r.json()
    print(dat)
# delete_data()