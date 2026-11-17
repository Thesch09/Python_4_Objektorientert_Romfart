from math import floor
from random import randint
from rich import print

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
        return f"I am [{self.name}], and I am an operating system that has existed for [{self.age}] Space Years (TM).\nI exist [{self.area}] and I am currently [{self.state}].\nMy current power level is at [{self.power/(self.maxPower/100):.2f}%], aka [{self.power:.2f}/{self.maxPower} KW] and I use [{self.kwh} KWH]."

    def timeForMISSSIONNNNN(self): # This is a DougDoug reference
        return f"[{self.name}] is the base operating system, it doesn't have a mission"

    def recharge(self):
        self.state = "chargin'"
        self.power += max(1, 10-self.kwh) * (10 - min(self.age/10, 7.5)) # Planned obsolescence
        if self.power >= self.maxPower:
            self.power = self.maxPower
            self.state = "nuetral"
            return f"Despite the fact that [{self.name}] is the base operating system, it has charged to full charge. [red]You will perish."
        return f"[{self.name}] spent a Space Year (TM) chargin'"

    def tickThisMachine(self):
        print(self.haveANiceChitChat())
        print()
        if self.state == "chargin'" or self.power <= self.maxPower/100*30:
            print(self.recharge())
            print()
            self.age += 1
            return f"[{self.name}] spent a Space Year (TM) chargin'"
        self.power -= self.kwh * floor(self.age/5)
        if self.power < 0:
            self.power = 0
        print(self.timeForMISSSIONNNNN())
        print()
        self.age += 1
        return f"[{self.name}] is done with its activities this Space Year"

class CheffOTron(FoolishOS):
    def __init__(self, name, area, maxPower, kwh, age, whichMeal, power = None):
        super().__init__(name, area, maxPower, kwh, age, power)
        self.whichMeal = whichMeal

    def haveANiceChitChat(self):
        return f"I am [{self.name}], and I am a Cheff-O-Tron that has existed for [{self.age}] Space Years (TM).\nI work in the [{self.area}] and I am currently [{self.state}].\nMy current power level is at [{self.power/(self.maxPower/100):.2f}%], aka [{self.power:.2f}/{self.maxPower} KW] and I use [{self.kwh} KWH].\nI make [{self.whichMeal}] for the employes in the [{self.area}]."

    def timeForMISSSIONNNNN(self): # This is still a DougDoug reference
        return f"[{self.name}] is making [{self.whichMeal}]! Specifically [{max(1,floor(randint(10, 15)/10*randint(10, 200)-self.age*1.5))}] orders of [{self.whichMeal}]"

    def recharge(self):
        self.state = "chargin'"
        self.power += max(1, 10-self.kwh) * max(self.age/10, 1.5) # Planned obsolescence
        if self.power >= self.maxPower:
            self.power = self.maxPower
            self.state = "nuetral"
            return f"[{self.name}] has finished chargin' and is ready to make [{self.whichMeal}]"
        return f"[{self.name}] spent a Space Year (TM) chargin'"

class Merrymer(FoolishOS):
    def __init__(self, name, area, maxPower, kwh, age, games, favGame, power = None):
        super().__init__(name, area, maxPower, kwh, age, power)
        self.games = games
        self.favGame = favGame

    def haveANiceChitChat(self):
        hasFavGame = f"with my favourite one being [{self.favGame}], which I don't have :(" # text that shows user wheter or not the Merrymer has it's favourite videographical game
        if self.favGame in self.games:
            hasFavGame = f"with my favourite one being [{self.favGame}], which I have :D"
        return f"I am [{self.name}], and I am a Merrymer that has existed for [{self.age}] Space Years (TM).\nI provide joy, merriment and entertainment to the people in the [{self.area}].\nMy current power level is at [{self.power/(self.maxPower/100):.2f}%], aka [{self.power:.2f}/{self.maxPower} KW] and I use [{self.kwh} KWH].\nThe games I play are {self.games}, {hasFavGame}"

    def timeForMISSSIONNNNN(self): # It's a DougDoug reference!
        game = self.games[randint(0, len(self.games)-1)]
        if game == self.favGame:
            return f"[{self.name}] is playing a game! Specifically it's favourite game, [{game}]!"
        return f"[{self.name}] is playing a game! Specifically [{game}]"

    def recharge(self):
        self.state = "chargin'"
        self.power += max(1, 10-self.kwh) * max(self.age/10, 0.5) # Planned obsolescence
        if self.power >= self.maxPower:
            self.power = self.maxPower
            self.state = "nuetral"
            return f"[{self.name}] has finished chargin' and is ready to play games!"
        return f"[{self.name}] spent a Space Year (TM) chargin'"

class RoboticSpiderThatWillEatEveryoneYouKnowAndLoveForSafety(FoolishOS): # This is the part where he kills you
    def __init__(self, name, area, maxPower, kwh, age, maxHP, maxRoboticMana, baseDmg, variableDmg, secretMove, roboticMana = None, hp = None, power = None):
        super().__init__(name, area, maxPower, kwh, age, power)
        self.maxHP = maxHP
        self.maxRoboticMana = maxRoboticMana
        self.baseDmg = baseDmg
        self.variableDmg = variableDmg
        self.secretMove = secretMove

        self.state = "alive"

        self.hp = hp
        if hp == None:
            self.hp = self.maxHP
        self.roboticMana
        if roboticMana == None:
            self.roboticMana = self.maxRoboticMana

    def timeForMISSSIONNNNN(self): # Despite everything, it's still a DougDoug reference
        if randint(1,3) == 3 or self.state == "combat":
            pass # initiate combat
        elif randint(1,9) == 9:
            pass # create a new Robotic Spider that will eat everyone you know and love for safety. They art a parasite
        elif randint(1,27) == 27:
            self.hp = 0
            self.state = "exploded"
            return f"[{self.name}] randomly just exploded. It's dead now. Yikes."
        return f"[{self.name}] is going to kill something"