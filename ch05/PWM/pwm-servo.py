import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#서보핀 출력설정
GPIO.setup(servo_pin, GPIO.OUT)

#PWM 인스턴스 생성 주파수 50
servo = GPIO.PWM(servo_pin, 50)

#듀티비 0 으로 시작
servo.start(0)

try:
    while True:
        #듀비피를 변경하여 서보 모터를 원하는 만큼 움직임
        servo.ChangeDutyCycle(7.5) # 90도
        time.sleep(1)
        servo.ChangeDutyCycle(12.8)# 180도
        time.sleep(1)
        servo.ChangeDutyCycle(2.5) #0도
except KeyboardInterrupt:
    pass
servo.stop()      
GPIO.cleanup()  
        