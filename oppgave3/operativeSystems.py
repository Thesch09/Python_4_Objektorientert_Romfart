from math import floor

machinations = [] # My schemes, my plot, my conspiracies

class FoolishOS:
    def __init__(self, name, area, maxPower, kwh, age, power = None):
        machinations.append(self) # Add it to my machinations, my schemes, my plots, my conspiracies
        self.state = "nuetral" # What the machine is currently doing

        self.name = name # Name of the bot
        self.area = area # Where in the ship the bot is
        self.maxPower = maxPower # How much power it can have
        self.kwh = kwh # How much power it uses in an hour
        self.age = age # The age of the bot. Planned obsolescence is a very real thing, thus the machine will become worse over time. Measured in space years (TM)

        if power == None: # If power == None, aka no input was added it will be set to it's max power, otherwise it will be set to the power input
            self.power = self.maxPower
        else:
            self.power = power

    def haveANiceChitChat(self):
        return f"I am [{self.name}], and I am an operating system that has existed for [{self.age}] Space Years (TM).\nI exist [{self.area}] and I am currently [{self.state}]\nMy current power level is at [{self.power/(self.maxPower/100):.2f}%], aka [{self.power:.2f}/{self.maxPower} KW] and I use [{self.kwh} KWH]"

    def timeForMISSSIONNNNN(self): # This is a DougDoug reference
        return f"[{self.name}] is the base operating system, it doesn't have a mission"

    def recharge(self):
        self.state = "chargin'"
        self.power += self.kwh * max(self.age/10, 7.5) # Planned obsolescence
        if self.power >= self.maxPower:
            self.power = self.maxPower
            self.state = "nuetral"
            return f"Despite the fact that [{self.name}] is the base operating system, it has charged to full charge. [red]You will perish."

    def tickThisMachine(self):
        print(self.haveANiceChitChat())
        if self.state == "chargin'" or self.power <= self.maxPower/100*30:
            print(self.recharge())
            return f"[{self.name}] spent a Space Year (TM) chargin'"
        self.power -= self.kwh * floor(self.age/5)
        print(self.timeForMISSSIONNNNN())
        return f"[{self.name}] is done with its activities this Space Year"