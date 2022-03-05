import json
import requests
link="http://127.0.0.1:8000/stuinfo/"
json_data=requests.get(url=link)
data=json_data.json()
print(data)