import requests
import json
URL="http://192.168.31.252:8000/api/studentapi/"
def getdata(id=None):
    data={}
    if id is not None:
        data={'id':id}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# getdata()
def post_data():
    data={
        "name":"Bhakke",
        "roll": 6,
        "city":"Hemja"
        }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# post_data()
def update_data():
    data={
        'id':3,
        'name':'Mani',
        # 'city':'Lahan',
        # 'roll':50
        
        }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.patch(url=URL,headers=headers,data=json_data)
    dat=r.json()
    print(dat)
update_data()
def delete_data():
    data={
        'id':1
        }
    headers={'content-Type':'application/json'}   
    json_data=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=json_data)
    dat=r.json()
    print(dat)
# delete_data()