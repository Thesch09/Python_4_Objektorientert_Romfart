from math import floor
from random import randint
from rich import print

machinations = [] # My schemes, my plot, my conspiracies
possibleTargets = ["a random civilian", "another RSTWEEYKALFS", "a CheffOTron", "a Merrymer", "a deliberately chosen civilian", "a space cop", "Brennan Lee Mulligan", "Siffrin nolastname", "two random civilians (gasp)"]

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
        return f"[{self.name}] is making \[{self.whichMeal}]! Specifically [{max(1,floor(randint(10, 15)/10*randint(10, 200)-self.age*1.5))}] orders of \[{self.whichMeal}]"

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
        self.target = None

        self.state = "alive"
        if age == 0:
            self.state = "newborn"
        
        self.offspring = 0

        self.hp = hp
        if hp == None:
            self.hp = self.maxHP
        self.roboticMana = maxRoboticMana
        if roboticMana == None:
            self.roboticMana = self.maxRoboticMana

    def haveANiceChitChat(self):
        return f"I am [{self.name}], and I am a Robotic Spider That Will Eat Everyone You Know And Love (for safety) that has existed for [{self.age}] Space Years (TM).\nI devour things in [{self.area}].\nMy current power level is at [{self.power/(self.maxPower/100):.2f}%], aka [{self.power:.2f}/{self.maxPower} KW] and I use [{self.kwh} KWH].\nI am currently on [{self.hp}/{self.maxHP} HP], [{self.roboticMana:.2f}/{self.maxRoboticMana} RM] and I am currently \[{self.state}].\nMy base damage is [{self.baseDmg}], can vary with [{self.variableDmg}] and my secret move is [{self.secretMove}]"

    def tickThisMachine(self):
        if self.state == "exploded":
            return f"[{self.name}] is exploded"
        elif self.hp <= 0:
            return f"[{self.name}] is dead"
        self.roboticMana += self.maxRoboticMana / 10 + self.roboticMana / 25
        if self.roboticMana > self.maxRoboticMana:
            self.roboticMana = self.maxRoboticMana
        if self.state != "combat":
            print(self.haveANiceChitChat())
        if self.state == "newborn":
            self.state = "alive"
            return f"[{self.name}] just got created, so it doesn't do anything"
        if self.power <= 0:
            input()
            return self.explode()
        self.power -= self.kwh * floor(self.age/5)
        if self.power < 0:
            self.power = 0
        print(self.timeForMISSSIONNNNN())
        print()
        self.age += 1
        return f"[{self.name}] is done with its activities this Space Year"

    def explode(self):
        dmg = floor(self.maxHP/randint(1,5))
        self.hp -= dmg
        if self.hp <= 0:
            self.state = "exploded"
            return f"[{self.name}] randomly just exploded. It's dead now. Yikes."
        return f"[{self.name}] randomly just exploded. It took [{dmg}] damage. Yikes."

    def timeForMISSSIONNNNN(self): # Despite everything, it's still a DougDoug reference
        brainwaves = randint(1,15)
        if self.state != "combat":
            input()
        if brainwaves <= 6 or self.state == "combat":
            if brainwaves > 6:
                brainwaves = randint(1,6)
            return self.warWarNeverChanges(brainwaves)
        elif brainwaves <= 9 and self.roboticMana >= floor(self.maxRoboticMana/2): # create a new Robotic Spider that will eat everyone you know and love for safety. They art a parasite
            offspring = RoboticSpiderThatWillEatEveryoneYouKnowAndLoveForSafety(f"{self.name}+{self.offspring}", self.area, self.maxPower + randint(1, 10), self.kwh, 0, self.maxHP + randint(1, 10), self.maxRoboticMana + randint(1, 10), self.baseDmg + randint(1, 10), (self.variableDmg[0] + randint(1, 5), self.variableDmg[1] + randint(5, 10)), self.secretMove)
            self.roboticMana -= floor(self.maxRoboticMana/2)
            self.offspring += 1
            return f"[{self.name}] cloned itself using [{floor(self.maxRoboticMana/2)} RM]."
        elif brainwaves == 15:
            self.explode()
        return f"[{self.name}] is going to kill something"

    def warWarNeverChanges(self,bw):
        # intro to combat
        if self.state != "combat":
            self.state = "combat"
            self.target = "a random civilian"
            if randint(1,2) == 1:
                self.target = possibleTargets[randint(0,len(possibleTargets)-1)]
            print(f"[{self.name}] has started a fight against \[{self.target}]!")
        else:
            print(f"[{self.name} - STATUS]")
            print(f"[{self.hp}/{self.maxHP} HP]")
            print(f"[{self.roboticMana:.2f}/{self.maxRoboticMana} RM]")
            print()
        
        if self.RSTWEEYKALFSturn(bw): # RSTWEEYKALFS' turn
            input()
            return self.targetTurn() # Targets turn
        else:
            input()
            self.state = "alive"
            return f"[{self.name}] won the battle against \[{self.target}]"

    def RSTWEEYKALFSturn(self, bw):
        notOver = False
        if bw == 6 and self.roboticMana >= floor(20+self.maxRoboticMana/7):
            dmg = max(1, self.baseDmg + randint(self.variableDmg[0], self.variableDmg[1]))*2
            print(f"[{self.name}] is using [{self.secretMove}] on \[{self.target}]!")
            print(f"It dealt [{dmg}] damage!")
            print(f"[{self.name}] used [{floor(20+self.maxRoboticMana/7)} RM]")
            self.roboticMana -= floor(20+self.maxRoboticMana/7)
            oddsVictor = randint(1,3)
            if self.target == "Brennan Lee Mulligan":
                oddsVictor = randint(1,10)
            if oddsVictor != 3:
                notOver = True

        elif bw >= 4 and self.hp != self.maxHP:
            notOver = True
            heal = randint(5, floor(self.maxHP/20)) + floor(self.age/20)
            if self.hp > self.maxHP:
                self.hp = self.maxHP
            print(f"[{self.name}] is healing itself for [{heal} HP]!")

        else:
            print(f"[{self.name}] is attacking \[{self.target}]")
            dmg = self.baseDmg + randint(self.variableDmg[0], self.variableDmg[1])
            print(f"It dealt [{dmg}] damage!")
            oddsVictor = randint(1,6)
            if self.target == "Brennan Lee Mulligan":
                oddsVictor = randint(1,20)
            if dmg == 0:
                oddsVictor = 0
            if oddsVictor != 6:
                notOver = True

        return notOver

    def targetTurn(self):
        brainwaves = randint(1,3)
        if brainwaves == 1:
            if self.target == "Siffrin nolastname":
                return f"\[{self.target}] snapped their fingers! They are faster now!\nThe battle is not over"
            elif self.target == "Brennan Lee Mulligan":
                dmg = randint(10, 15) + floor(self.age/4)
                self.hp -= dmg
                if self.hp <= 0:
                    self.state = "dead"
                    return f"\[{self.target}] does a weak attack against [{self.name}] dealing [{dmg}] damage... and won! [{self.name}] is dead now"
                return f"\[{self.target}] does a weak attack against [{self.name}] dealing [{dmg}] damage...\nThe battle is not over"
            return f"\[{self.target}] cowered in fear\nThe battle is not over"
        elif brainwaves == 2:
            if self.target == "Siffrin nolastname":
                return f"\[{self.target}] closed their eyes...\nThe battle is not over"
            elif self.target == "Brennan Lee Mulligan":
                dmg = randint(10, 25) + floor(self.age/3)
                self.hp -= dmg
                if self.hp <= 0:
                    self.state = "dead"
                    return f"\[{self.target}] does a strong attack against [{self.name}] dealing [{dmg}] damage... and won! [{self.name}] is dead now"
                return f"\[{self.target}] does a strong attack against [{self.name}] dealing [{dmg}] damage...\nThe battle is not over"
            return f"\[{self.target}] tried to run away, but [{self.name}] is too fast\nThe battle is not over"
        else:
            if self.target == "Siffrin nolastname":
                print(f"\[{self.target}] says a cool one liner")
                dmg = randint(10, 35) + floor(self.age/2)
            elif self.target == "Brennan Lee Mulligan":
                dmg = randint(20, 50) + floor(self.age/2)
                self.hp -= dmg
                if self.hp <= 0:
                    self.state = "dead"
                    return f"\[{self.target}] does an ultimate attack against [{self.name}] dealing [{dmg}] damage... and won! [{self.name}] is dead now"
                return f"\[{self.target}] does an ultimate attack against [{self.name}] dealing [{dmg}] damage...\nThe battle is not over"
            else:
                dmg = randint(1, 15) + floor(self.age/2)
            self.hp -= dmg
            if self.hp <= 0:
                self.state = "dead"
                return f"\[{self.target}] attacked [{self.name}] dealing [{dmg}] damage... and won! [{self.name}] is dead now"
            return f"\[{self.target}] attacked [{self.name}] dealing [{dmg}] damage...\nThe battle is not over"