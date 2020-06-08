from gpiozero import LED
from time import sleep

clock = LED(14)
strobe = LED(15)
data = LED(18)
Out1 = LED(20)
Out2 = LED(21)


def push_value(val):
	if val:
		data.on()
	else:
		data.off()
	clock.on()
#	sleep(0.0001)
	clock.off()
#	sleep(0.0001)

while True:
	strobe.off()
	Out1.on()
	Out2.off()
	
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	
	print("End1")
		
	strobe.on()
	
	strobe.off()
	Out1.off()
	Out2.on()
	
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	push_value(True)
	push_value(False)
	
	print("End2")
		
	strobe.on()
