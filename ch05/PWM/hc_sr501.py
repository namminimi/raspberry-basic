import RPi.GPIO as GPIO
import time

# led1 , led2 , 센서 입력핀 번호 설정
led_1 = 20
led_2 = 21
sensor = 17

# 불필요한 warning 제거, 핀모드 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# led핀의 입출력
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)

print("PIR Ready ..")
time.sleep(5) # PIR센서 준비 시간

try:
    while True:
        if GPIO.input(sensor) == 1:
            GPIO.output(led_1,1) #첫번째 led 켬
            GPIO.output(led_2,0) #두번째 led 끔
            print("Motion Detected!")
            time.sleep(0.1)
        if GPIO.input(sensor) == 0:
            GPIO.output(led_1,0)
            GPIO.output(led_2,1)
            print("Motion out!")
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()