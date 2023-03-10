import RPi.GPIO as GPIO
import time

#GPIO 핀모드 지정
GPIO.setmode(GPIO.BCM)

ledpin = 2

#GPIO 출력 지정
GPIO.setup(ledpin, GPIO.OUT)
pwm = GPIO.PWM(ledpin, 1000) #led핀에 1000hz pwm을 출력
pwm.start(0)

try:
    while True:
        for i in range(0, 101, 5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
        for j in range(100, -1, -5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
finally:
    pwm.stop()
    GPIO.cleanup()                
                 