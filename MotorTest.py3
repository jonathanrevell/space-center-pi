import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

for i in range(512*1):
    kit.stepper1.onestep()
    kit.stepper2.onestep()
