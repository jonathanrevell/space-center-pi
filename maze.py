import RPi.GPIO as GPIO
from gpiozero import InputDevice
from components import Component

class Maze(Component):
    def __init__( self, result_pin ):
        super().__init__("maze", "maze")
        self.pins = {
            "pins": InputDevice(result_pin)
        }
        self.chemicalMap = {
            "amonia": 1,
            "methyl alcohol": 2,
            "acetone": 3,
            "carbon monoxide": 4,
            "hydrogen": 5
        }
        self.activeChemical = None
        self.activeEndpoint = None
    
    def read():
        return self.pins["result"].is_active
    
    def setValue(self, val):
        self.activeChemical = val["chemical"]
        self.activeEndpoint = val["endpoint"]
    
    def encodeValueToMessage(self, msg):
        if(self.activeChemical == None):
            inputNum = 0
        else:
            inputNum = self.chemicalMap[self.activeChemical]
        
        if(self.activeEndpoint == None):
            endNum = 0
        else:
            endNum = self.activeEndpoint
        return msg.encodeMazeValues(inputNum, endNum)

    def resetAndEncodeToMessage(self, msg):
        self.activeChemical = None
        self.activeEndpoint = None
        return self.encodeValueToMessage(msg)
        
    

    