import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)

pwm = GPIO.PWM(18, 100)


# 옥타브 배열
""" Frq = [4186, 4699, 5274, 5588, 6272, 7040, 7902, 4186] """
z = 262 #도
x = 294 #레
c = 330 #미
v = 349 #파
b = 392 #솔
n = 440 #라
m = 523 #시
a = 277 #도#
f = 379 #파#
u = 123 #시b
t = 92 #솔b

""" 도 레미 도 미 도 미
레 미 파파 미레파
미 파 솔미 솔미 솔
파 솔 라라 솔파 라
솔 도레미파솔라
라 레 미파솔라시
시 미 파#솔라시도
시 시(내림)라 파 시 솔 도
도도레미파솔라시도 솔 도
 """

Frq = [z, x,c,z,c,z,c,x,c,v,v,c,x,v,c,v,b,v,b,v,b,v,b,n,n,b,v,n,
       b,z,x,c,v,b,n,n,x,c,v,b,n,m,m,c,f,b,n,m,z,m,u,n,v,m,t,z,a,z,x,c,v,b,n,m,b,a]
speed = 0.3 #음과 음 사이 시간 설정 0.5초

pwm.start(10)

try:
    while 1:
        for fr in Frq:
            pwm.ChangeFrequency(fr)
            time.sleep(speed)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()
