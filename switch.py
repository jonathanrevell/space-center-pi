import RPi.GPIO as GPIO

def switch(pin):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  return GPIO.input(pin)