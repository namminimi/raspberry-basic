# app_start.py
#flask에서 Flask클래스 불러오기
from flask import Flask
#Flask 객체 생성 __name__ 내파일명을 의미함
app = Flask(__name__)

#요청에 대한 응답 구현
@app.route("/")
def helloworld():
    return "Hello World"


@app.route("/led/on")
def led_on():
    return "LED ON"

@app.route("/led/off")
def led_off():
    return "LED OFF"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")