import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#trig와 echo핀의 출력/입력 설정
trig = 23
echo = 24
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

#trig 핀의 신호를 0으로 출력
GPIO.output(trig, False)
print("Wating for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(trig, True) #Triger핀에 펄스신호를 만들기위해 1 출려8ㄱ
        time.sleep(0.001)
        GPIO.output(trig, False)
        
        while GPIO.input(echo) == 0:
            start = time.time()      #Echo핀 상승시간
            
        while GPIO.input(echo) == 1:
            stop = time.time() # echo핀 하강 시간
            
        checktime = stop - start
        distance = checktime * 34300 / 2
        print("Distance : %.1f cm" % distance)
        time.sleep(0.4)         
except KeyboardInterrupt:
    print("Measurement stopped by User")
    pass
GPIO.cleanup()
