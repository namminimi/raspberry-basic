from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

Led = 8
GPIO.setmode(GPIO.BOARD) #컨넥터 pin번로 사용 BCM ===> GPIO번호로

GPIO.setup(Led, GPIO.OUT, initial = GPIO.LOW)

@app.route("/")
def helloworld():
    return "Hello world"

@app.route("/led")
def led():
    state = request.args.get("state")
    if state == "on":
        GPIO.output(Led,GPIO.HIGH)
        return "LED ON"
    elif state == "off": 
        GPIO.output(Led, GPIO.LOW)
        return "LED OFF"
    elif state == "error":
        return "쿼리스트링으로 state 가 전달되지 않음"
    else:
        return "잘못된 쿼리스트링 전달됨"

""" @app.route("/led/off")
def led_off():
    GPIO.output(Led,GPIO.LOW)
    return "LED OFF" """

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")