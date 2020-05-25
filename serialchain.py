import queue
from gpiozero import LED, OutputDevice

class SerialChain:
    def __init__(self, data_pin=None, clock_pin=None, latch_pin=None):
        self.pins = {}
        self.queue = queue.Queue()
        self.writing = False

        self.pins["data"]  = OutputDevice(data_pin)
        self.pins["clock"] = OutputDevice(clock_pin)
        self.pins["latch"] = OutputDevice(latch_pin)

    def write(self, data):
        """
        Queues up data to be sent on the bus
        and writes the message out if the bus is idle
        """
        self.queue.put(data)
        self.__nextMessage()

    def __nextMessage(self):
        """
        If not currently writing out to the bus, it'll start writing queued messages to the bus
        and continue until all the queued messages are exhausted
        """
        if not self.writing:
            if not self.queue.empty():
                self.writing = True
                data = self.queue.get()
                self.__write(data)
                self.writing = False

                # After writing a message, send the next one
                self.__nextMessage()
            else:
                print("No more messages in queue")
        else:
            print("Bus in use, will get next message after complete")

    def __write(self, data):
        """
        Writes out data to the chain
        """

        for bit in data:
            if bit == True:
                self.pins["data"].on()
            else:
                self.pins["data"].off()
            self.pins["clock"].on()
            self.pins["clock"].off()
        
        self.__endMessage()
    
    def __endMessage(self):
        """
        Latches the written message
        """
        self.pins["latch"].on()
        self.pins["clock"].on()
        self.pins["clock"].off()
        self.pins["latch"].off()