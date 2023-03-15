import RPi.GPIO as GPIO
from flask import Flask, render_template,request

app = Flask(__name__)

#불필요한 warning제거 GPIO핀모드 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins = {
    23:{'name':'RED LED','state':GPIO.LOW},
    24:{'name':'YELLOW LED','state':GPIO.LOW},
    25:{'name':'Green LED','state':GPIO.LOW},
}

# pins내에 있는 모든 핀들을 출력으로 설정하고 초기 LED off
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)

@app.route('/')
def main():
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
    #templateData에 저장
    templateData = {
        'pins':pins
    }
    return render_template('homeLED.html',**templateData)  

# 웹 서버의 url주소로 접근하면 main()
@app.route('/<changePin>/<action>')
def action(changePin,action):
    changePin = int(changePin)
    deviceName = pins[changePin]['name']
    if action == 'on':
        GPIO.output(changePin, GPIO.HIGH)
    if action == 'off':
        GPIO.output(changePin, GPIO.LOW)
    pins[changePin]['state'] = GPIO.input(changePin)
    templateData = {
        'pins': pins
    }        
    return render_template('homeLED.html', **templateData)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
    