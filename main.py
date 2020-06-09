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
   potTemp = potentiometer(23)
   potHumid = potentiometer(24)
   potElec = potentiometer(25)
   potScrub = potentiometer(8)
   potOxy = potentiometer(7)
   potNitro = potentiometer(12)
   swTemp1 = switch(4)
   swTemp2 = switch(17)
   swHumid1 = switch(27)
   swHumid2 = switch(22)
   swElec1 = switch(10)
   swElec2 = switch(9)
   swOxy1 = switch(11)
   swOxy2 = switch(5)
   swNitro1 = switch(6)
   swNitro2 = switch(13)
   sw11 = switch(19)
   sw12 = switch(26)

def startServer():
   PORT = 8080
   @route("/")
   def hello(request):
      return "Hello, world!"

   @route("/data", methods=['POST'])
   def do_post(request):
      content = json.loads(request.content.read())
      body = dict(content)
      barGraphComponents.update(body)
      return "Success!"

   run("0.0.0.0", 8080)

#Start Alphanumeric Flickering
#try:
#  Thread(target=alternateLED).start()
#except:
#  print "Error: unable to start thread"

# Create the serial chain and set which pins it uses
#barGraphChain = SerialChain(data_pin=17, clock_pin=11, latch_pin=24)

#barGraphComponents = ComponentSeries(barGraphChain)

# Order is critical, this should be the order on the wire
#barGraphComponents.add("water", "bargraph")
#barGraphComponents.add("oxygen", "bargraph")
#barGraphComponents.add("nitrogen", "bargraph")

# # Start a new encoded message
# msg = EncodedMessage()

# # Add as many parts to the message as are on the circuit
# msg.encodeBarGraph(9)           # 9 LEDs lit from left to right 
# msg.encodeReverseBarGraph(3)    # 7 unlit, then 3 lit from left to right
# msg.encodeBarGraph(2)

# # Writes the message out to the barGraphChain and latches it when done
# barGraphChain.write(msg.data)


