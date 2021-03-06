from encoding import EncodedMessage

class Component:
    def __init__(self, name, ctype, defval=0):
        self.name = name
        self.ctype = ctype
        self.value = defval
    
    def setValue(self, val):
        self.value = val
    
    def encodeValueToMessage(self, msg):
        val = self.value
        if self.ctype == "led":
            return msg.encodeLED(val)
        elif self.ctype == "bargraph":
            return msg.encodeBarGraph(val)
        elif self.ctype == "bargraph15":
            return msg.encodeBarGraph(val, 15)
        elif self.ctype == "bargraph-reverse":
            return msg.encodeReverseBarGraph(val)
        elif self.ctype == "alphanumeric":
            return msg.encodeAlphaNumericNumber(val)
        else:
            raise Exception("Unrecognized component type " + str(self.ctype))

    def resetAndEncodeToMessage(self, msg):
        self.setValue(0)
        self.encodeValueToMessage(msg)


class ComponentSeries:
    def __init__(self, wire):
        self.wire = wire
        self.components = {}
        self.o_components = []

    def add(self, name, ctype, defval=0):
        if name in self.components:
            raise Exception("ComponentSeries already contains a component named: " + str(name))
        new_component = Component(name, ctype, defval)
        self.components[name] = new_component
        self.o_components.append(new_component)
        return

    def addInstance(self, name, new_component):
        if name in self.components:
            raise Exception("ComponentSeries already contains a component named: " + str(name))
        self.components[name] = new_component      
        self.o_components.append(new_component)

    def update(self, data):
        # Start a new encoded message
        msg = EncodedMessage()
        
        # Iterate through the fields
        for field in data:
            if field in self.components:
                self.components[field].setValue( data[field] )
                print("Set value of " + str(self.components[field].ctype) + " '" + str(field) + "' to " + str(data[field]))
            else:
                raise Exception("No component named " + str(field))

        # Iterate through the components in order to build the message
        for c in self.o_components:
            c.encodeValueToMessage(msg)

        self.wire.write(msg.data)

    def clear(self):
        print("Clearing series")

        # Start a new encoded message
        msg = EncodedMessage()

        # Iterate through the components in order to build the message
        for c in self.o_components:
            c.resetAndEncodeToMessage(msg)

        self.wire.write(msg.data)




