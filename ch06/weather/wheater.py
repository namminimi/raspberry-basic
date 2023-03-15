from urllib.parse import urlencode, unquote
import requests
import json
from flask import Flask, request
from flask import render_template
app = Flask(__name__)
def weatherFetch(areatext):
    areanx = "102"
    areany = "84"
    if(areatext == "울산"):
        areanx = "102"
        areany = "84"
    elif(areatext == "남구"):
        areanx = "102"
        areany = "84"
    elif(areatext == "중구"):
        areanx = "101"
        areany = "84"
    elif(areatext == "동구"):
        areanx = "104"
        areany = "83"
    elif(areatext == "북구"):
        areanx = "103"
        areany = "85"
    else:
        areanx = "102"
        areany = "81"
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params ={
        'serviceKey' : unquote('EqIc%2BYY8ndXvnIHlW77WRBUqvqjVmDjn5e6alb5KhKvqafzMSN%2FHJMMCGTepwrGpeIEzhsygoGwtJKuL4JPv6g%3D%3D'), 
        'pageNo' : '1', 
        'numOfRows' : '1000', 
        'dataType' : 'JSON', 
        'base_date' : '20230315', 
        'base_time' : '0600', 
        'nx' : areanx, 
        'ny' : areany 

    }
    response = requests.get(url, params=params)
    r_dict = json.loads(response.text)
    r_response = r_dict.get("response")
    r_body = r_response.get("body")
    r_items = r_body.get("items")
    r_item = r_items.get("item")
    
    result = {}
    for item in r_item:
        if(item.get("category") == "T1H"):
            result=item
            break
    return result

# aa = weatherFetch("울산")
# print(aa)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather/<mapnumber>")
def weatherCh(mapnumber):
    try:
        re = weatherFetch(mapnumber)
        return re
    except expression as identifier:
        return "fail"
if __name__ == "__main__":

    app.run(host="0.0.0.0")