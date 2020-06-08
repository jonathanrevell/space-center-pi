import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

data = 21
clock = 20
strobe = 16

def set_pin(pin,val):
	if val:
		GPIO.output(pin, GPIO.HIGH)
	else:
		GPIO.output(pin, GPIO.LOW)
	GPIO.output(clock, GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(clock, GPIO.LOW)
	time.sleep(0.05)
	
while True:
	GPIO.output(strobe, GPIO.LOW)
	
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)

	GPIO.output(strobe, GPIO.HIGH)
	
	GPIO.output(strobe, GPIO.LOW)
	
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)
	set_pin(data,False)
	set_pin(data,True)

	GPIO.output(strobe, GPIO.HIGH)
