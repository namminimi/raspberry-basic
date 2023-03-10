from urllib.parse import urlencode, unquote
import requests
import json





# Python3 샘플 코드 #


import requests

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={
        'serviceKey' : unquote('4iOtsbmDLEGr7L9im6qjMPmwORBPWPhfWS6lIzZXKZNKcrNdAPCI9AqXakt3ccbX9nRfuleDBgdwqvuiMpgMpw%3D%3D'), 
        'pageNo' : '1', 
        'numOfRows' : '1000', 
        'dataType' : 'JSON', 
        'base_date' : '20230310', 
        'base_time' : '0600', 
        'nx' : '55', 
        'ny' : '127' }

response = requests.get(url, params=params)
print("==============================response json data start =======================================")
print(response)
print("==============================response json data end =======================================")
print()
r_dict = json.loads(response.text)
r_response = r_dict.get("response")
r_body = r_response.get("body")
r_items = r_body.get("items")
r_item = r_items.get("item")

result = {}
for item in r_item:
    if(item.get("category") == "PTY"):
        result = item
        break
print("==============================python =======================================")       
#print(response.text)
print(result)
print("==============================python =======================================")   