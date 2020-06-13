from gpiozero import LED
from time import sleep
from pins import serial0
from serialchain import SerialChain
from encoding import EncodedMessage
from klein import run, route
from components import ComponentSeries
import json
from threading import Thread
from Potentiometer import potentiometer
from switch import switch
from motors import PressureGauge, TemperatureGauge
from maze import Maze
from testing import testBargraphs

PORT = 8080

print("Started SpacePi")

#Setting Up the Outputs for the Alphanumeric Flicker
Out1 = LED(20)
Out2 = LED(21)

def alternateLED():
   while 1:
       Out1.on()
       Out2.off()
       Out1.off()
       Out2.on()

def readInputs():
   inputData = {}
   inputData["temperature"] = potentiometer(23)
   inputData["humidity"] = potentiometer(24)
   inputData["electrolysis"] = potentiometer(25)
   inputData["scrubbing"] = potentiometer(8)
   inputData["oxygen"] = potentiometer(7)
   inputData["nitrogen"] = potentiometer(12)
   inputData["swTemp1"] = switch(4)
   inputData["swTemp2"] = switch(17)
   inputData["swHumid1"] = switch(27)
   inputData["swHumid2"] = switch(22)
   inputData["swElec1"] = switch(10)
   inputData["swElec2"] = switch(9)
   inputData["swOxy1"] = switch(11)
   inputData["swOxy2"] = switch(5)
   inputData["swNitro1"] = switch(6)
   inputData["swNitro2"] = switch(13)
   inputData["maze"] = mazeInstance.read()
   inputData["sw12"] = switch(26)
   inputData["sw13"] = switch(16)
   return inputData

def startServer():
   
   @route("/")
   def hello(request):
      return "Hello, world!"

   @route("/data", methods=['POST'])
   def do_post(request):
      content = json.loads(request.content.read())
      body = dict(content)
      mainSeries.update(body)
      
      PressureGauge.encodeValue(body["pressure"])
      TemperatureGauge.encodeValue(body["temperature"])

      return "Success!"

   @route("/inputs", methods=['GET'])
   def do_get(request):
      return readInputs()

   run("0.0.0.0", PORT)



#Reset Step Motors
print("Resetting guages")
PressureGauge.reset()
TemperatureGauge.reset()

#Start Alphanumeric Flickering
try:
  Thread(target=alternateLED).start()
except:
  print ("Error: unable to start thread")

# Create the serial chain and set which pins it uses
barGraphChain = SerialChain(data_pin=18, clock_pin=15, latch_pin=14)

mainSeries = ComponentSeries(barGraphChain)
mazeInstance = Maze(19)

# Order is critical, this should be the order on the wire

# 1 [10 bits] Maze
mainSeries.addInstance("maze", mazeInstance)

# 2 [55 bits] Bargraphs
mainSeries.add("waste", "bargraph")
mainSeries.add("water", "bargraph15")
mainSeries.add("hydrogen", "bargraph")
mainSeries.add("oxygen", "bargraph")
mainSeries.add("nitrogen", "bargraph")

# 3 [5 bits] Leds
mainSeries.add("wasteWarning", "led")
mainSeries.add("waterWarning", "led")
mainSeries.add("hydrogenWarning", "led")
mainSeries.add("oxygenWarning", "led")
mainSeries.add("nitrogenWarning", "led")

# 13 x 8 shift for alphanumeric
# 200 Total


print("RUNNING BOOT TEST")
testBargraphs(mainSeries, ["waste", "water", "hydrogen", "oxygen", "nitrogen"])

startServer()
