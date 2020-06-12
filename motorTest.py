import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

#512 Steps are a full rotation
def motorForward(motor,steps):
    loops = 0
    if motor == 1:
        while loops < steps:
            kit.stepper1.onestep(direction=stepper.FORWARD)
            loops += 1
    if motor == 2:
        while loops < steps:
            kit.stepper2.onestep(direction=stepper.FORWARD)
            loops += 1

def motorBackward(motor,steps):
    loops = 0
    if motor == 1:
        while loops < steps:
            kit.stepper1.onestep(direction=stepper.BACKWARD)
            loops += 1
    if motor == 2:
        while loops < steps:
            kit.stepper2.onestep(direction=stepper.BACKWARD)
            loops += 1