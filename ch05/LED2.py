import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #GPIO핀들의 번호를 지정하느 ㄴ규칠 설정
LED_pin = 2
GPIO.setup(LED_pin, GPIO.OUT)
try:
    while True:
        GPIO.output(LED_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_pin, GPIO.LOW)
        time.sleep(1)
        
finally:
    GPIO.cleanup()        