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
# getdata()
def post_data():
    data={
        "name":"Hary",
        "roll": 300,
        "city":"Butwal"
        }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
post_data()
def update_data():
    data={
        'id':20,
        'name':'ani',
        'city':'Kritipur',
        'roll':50
        
        }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    dat=r.json()
    print(dat)
# update_data()
def delete_data():
    data={
        'id':18
        }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    dat=r.json()
    print(dat)
# delete_data()