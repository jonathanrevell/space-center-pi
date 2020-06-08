import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
def potentiometer(pin):
	loops = 0
	total = 0
	while loops != 100:
		length = 0
		reset = 0
		GPIO.setup(pin, GPIO.OUT, initial=1)
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		while reset == 0:
			if GPIO.input(pin) == 0:
				reset = 1
			length += 1
		total += length
		loops += 1
	total = total/100
	if total < 278:
		return (0)
	elif total < 290:
		return (1)
	elif total < 309:
		return (2)
	elif total < 336:
		return (3)
	elif total < 376:
		return (4)
	elif total < 434:
		return (5)
	elif total < 518:
		return (6)
	elif total < 641:
		return (7)
	elif total < 821:
		return (8)
	elif total < 1083:
		return (9)
	else:
		return (10)

while True:
	result1 = potentiometer(24)
	result2 = potentiometer(18)
	print (result1)
	print (result2)
	
	#	print (max(int((((math.log(average)-4.6)*10)-4.7)/11*10.5),0))
	#	print (int(((math.sqrt(average)-12)*1.2)/12*10.5))
	#	print (int(int(average/10-14)/3))
