# from gpiozero import LED
from time import sleep
from pins import serial0
from serialchain import SerialChain
from encoding import EncodedMessage
from klein import run, route
from components import ComponentSeries
import json

print("Started SpacePi")

# Create the serial chain and set which pins it uses
barGraphChain = SerialChain(data_pin=17, clock_pin=11, latch_pin=24)

barGraphComponents = ComponentSeries(barGraphChain)

# Order is critical, this should be the order on the wire
barGraphComponents.add("water", "bargraph")
barGraphComponents.add("oxygen", "bargraph")
barGraphComponents.add("nitrogen", "bargraph")

# # Start a new encoded message
# msg = EncodedMessage()

# # Add as many parts to the message as are on the circuit
# msg.encodeBarGraph(9)           # 9 LEDs lit from left to right 
# msg.encodeReverseBarGraph(3)    # 7 unlit, then 3 lit from left to right
# msg.encodeBarGraph(2)

# # Writes the message out to the barGraphChain and latches it when done
# barGraphChain.write(msg.data)


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
