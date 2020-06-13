import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

# 512 Steps are a full rotation
MAX_STEPS = 512

class StepMotor:
    def __init__(self, stepper):
        self.stepper = stepper
        self.position = 0
        self.minPosition = 0
        self.minValue = 0.0
        self.maxPosition = MAX_STEPS
        self.maxValue = MAX_STEPS - 1.0
        self.valueMultiplier = 1.0

    def setMin(self, position, value):
        self.minPosition = position
        self.minValue = value

    def setMax(self, position, value):
        self.maxPosition = position
        self.maxValue = value

    def reset(self):
        self.backward(512)
        self.position = 0

    '''
    Because we may only be using part of the guage
    And because the guage values are likely not 0 - 512
    We translate the position to a value
    '''
    def calculateValueMultiplier(self):
        steps = self.maxPosition - self.minPosition
        valRange = self.maxValue - self.minValue
        self.valueMultiplier = valRange / steps

    def __computeValue(self):
        delta = self.position - self.minPosition
        newVal = delta * self.valueMultiplier
        newVal = round(newVal)
        if(newVal > self.maxValue):
            print("Step motor tried to set value " + str(newVal) + " over max: " + str(self.maxValue))
            newVal = self.maxValue
        if(newVal < self.minValue):
            print("Step motor tried to set value " + str(newVal) + " below min: " + str(self.minValue))
            newVal = self.minValue
        
        self.value = newVal
        return newVal

    def setPosition(self, newPosition):
        delta = newPosition - self.position
        if(delta > 0):
            self.forward(delta)
        elif(delta < 0):
            self.backward(abs(delta))

    '''
    Encodes a value into a new position on the gauge
    '''
    def encodeValue(self, newValue):
        delta = newValue - self.minValue
        newPos = delta / self.valueMultiplier
        newPos = round(newPos)
        if(newPos > self.maxPosition):
            print("Step motor tried to set position " + str(newPos) + " over max: " + str(self.maxPosition))
            newPos = self.maxPosition
        if(newPos < self.minPosition):
            print("Step motor tried to set position " + str(newPos) + " below min: " + str(self.minPosition))
            newPos = self.minPosition
        self.setPosition(newPos)
    
    
    def forward(self, steps):
        counter = 0
        while counter < steps:
            self.stepper.onestep(direction=self.stepper.FORWARD)
            counter += 1
            self.__inc_val()
        self.__computeValue()

    def backward(self, steps):
        counter = 0
        while counter < steps:
            self.stepper.onestep(direction=self.stepper.BACKWARD)
            counter += 1
            self.__dec_val()
        self.__computeValue()

    def __inc_val(self):
        if(self.position + 1 >= MAX_STEPS): 
            self.position = 0
        else:
            self.position += 1

    def __dec_val(self):
        if(self.position - 1 <= 0): 
            self.position = MAX_STEPS - 1
        else:
            self.position -= 1


PressureGauge = StepMotor(kit.stepper1)
TemperatureGauge = StepMotor(kit.stepper2)