#라이브러리 불러오기 (BMP85/180)
import Adafruit_BMP.BMP085 as BMP085

#BMP180센서의 인스턴스 sensor생성
sensor = BMP085.BMP085()

#온도, 압력, 고도값을 읽어서 변수에 저장
temp = sensor.read_temperature()
pressure = sensor.read_pressure()
ALTitude = sensor.read_ALTitude()

#측정값을 출력
print("온도는 = {0:0.2f} *C" .format(temp))
print("압력은 = {0:0.2f} Pa" .format(pressure))
print("고도는 = {0:0.2f} m" .format(ALTitude))