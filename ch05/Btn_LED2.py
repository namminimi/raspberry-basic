import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_pin = 2
sw_pin = 17
GPIO.setup(LED_pin,GPIO.OUT)
GPIO.setup(sw_pin,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(sw_pin)== GPIO.HIGH:
			GPIO.output(LED_pin,GPIO.HIGH)
		else:
			GPIO.output(LED_pin, GPIO.LOW)
finally:
	GPIO.cleanup()
