import queue
from gpiozero import LED, OutputDevice

class XSPIMessage:
    def __init__(self, address, message):
        self.address = address
        self.message = message

class XSPISoftwareBus:
    """
    This has some similarities to the SPI Protocol, but ultimately is not the same.
    We have 3 pins we use to determine the address of the device we want to write to.
    We have a clock pin used to synchronize the clock to the devices.
    We write out data on one pin in a serial fashion
    We have a dedicated pin for "start" and "stop" which are used for latching and reset of the devices
    """
    def __init__(self, pindict):
        self.pins = {}
        self.queue = queue.Queue()
        self.writing = False

        self.pins["data"] = OutputDevice(pindict["data"])
        self.pins["clock"] = OutputDevice(pindict["clock"], active_high=True)
        self.pins["address1"] = OutputDevice(pindict["address1"])
        self.pins["address2"] = OutputDevice(pindict["address2"])
        self.pins["address3"] = OutputDevice(pindict["address3"])
        self.pins["start"] = OutputDevice(pindict("start"))
        self.pins["end"] = OutputDevice(pindict("end"))

    def write(self, address, data):
        """
        Queues up data to be sent on the bus
        and writes the message out if the bus is idle
        """
        self.queue.put(XSPIMessage(address, data))
        self.__nextMessage()

    def __nextMessage(self):
        """
        If not currently writing out to the bus, it'll start writing queued messages to the bus
        and continue until all the queued messages are exhausted
        """
        if not self.writing:
            if not self.queue.empty():
                self.writing = True
                msg = self.queue.get()
                self.__write(msg.address, msg.data)
                self.writing = False

                # After writing a message, send the next one
                self.__nextMessage()
            else:
                print("No more messages in queue")
        else:
            print("Bus in use, will get next message after complete")

    def __write(self, address, data):
        """
        Writes out data to the device at the given address
        """
        # Sets the address and activates the start pin
        self.__startMessage(address)

        for bit in data:
            if bit == True:
                self.pins["data"].on()
            else:
                self.pins["data"].off()
            self.pins["clock"].on()
            self.pins["clock"].off()
        
        self.__endMessage()
            
    def __startMessage(self, address):
        """
        Sets the address pins and activates the start pin
        """
        self.pins["end"].off()
        
        addressBin = "{0:b}".format(address)
        
        # Resolve address
        for i, bit in enumerate(addressBin):
            if bit == "1":
                self.pins["address" + str(i)].on()
            else:
                self.pins["address" + str(i)].off()

        # Send the start message
        self.pins["start"].on()

        self.pins["clock"].on()
        self.pins["clock"].off()
    
    def __endMessage(self):
        """
        Clears the address and sets the end pin
        """
        self.pins["start"].off()
        self.pins["end"].on()

        self.pins["address1"].off()
        self.pins["address2"].off()
        self.pins["address3"].off()

        self.pins["clock"].on()
        self.pins["clock"].off()


        


        