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
        pwm.ChangeDutyCycle(0)
        time.sleep(1)
        pwm.ChangeDutyCycle(25)
        time.sleep(1)
        pwm.ChangeDutyCycle(50)
        time.sleep(1)
        pwm.ChangeDutyCycle(75)
        time.sleep(1)
        pwm.ChangeDutyCycle(100)
        time.sleep(1)
        
finally:
    pwm.stop()
    GPIO.cleanup()        