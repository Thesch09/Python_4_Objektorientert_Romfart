from spaceshipClass import Spaceship, spacechips
from math import ceil

class Observer(Spaceship):
    def specialAttack(self):
        return f"Spaceship [{self.name}] is observing the planet. It will always observe"

class PeopleCarrier(Spaceship):
    def __init__(self, name, maxSpeed, speed, throtle, maxFuel, fuelEfficiency, maxPeople, people, maxNutrients, nutrients, fuel = None):
        super().__init__(name, maxSpeed, speed, throtle, maxFuel, fuelEfficiency, fuel)
        self.maxPeople = maxPeople
        self.people = people
        self.maxNutrients = maxNutrients
        self.nutrients = nutrients
        self.consumeRate = 3.5
        self.humanNutrients = 75

    def provideInfo(self):
        return f"I am the spaceship [{self.name}].\nI am moving at [{self.speed} KM/H].\nMy max speed is [{self.maxSpeed} KM/H]\nI can speed up with [{self.throtle} KM/H] by using [{self.fuelEfficiency} L] fuel per [KM/H]\nMy current fuel level is at [{self.fuel/(self.maxFuel/100):.2f}%], aka [{self.fuel:.2f}/{self.maxFuel} L]\nI am a People Carrier, there are a total of [{self.people}] out of [{self.maxPeople}] people on board.\nMy current nutrient level is at [{self.nutrients/(self.maxNutrients/100):.2f}%], aka [{self.nutrients:.2f}/{self.maxNutrients} KG]"

    def specialAttack(self):
        neededNutrients = self.consumeRate * self.people
        if self.nutrients >= neededNutrients:
            self.nutrients -= neededNutrients
            return f"The [{self.people}] people aboard spaceship [{self.name}] have consumed [{neededNutrients} KG] nutrients."
        lostPeople = ceil((neededNutrients - self.nutrients)/self.humanNutrients)
        self.people -= lostPeople
        self.nutrients += lostPeople * self.humanNutrients
        #print(ceil((neededNutrients - self.nutrients)/self.humanNutrients) * self.humanNutrients)
        self.nutrients -= neededNutrients
        return f"The [{self.people}] people aboard spaceship [{self.name}] have consumed [{neededNutrients} KG] nutrients. But... [{lostPeople}] people are missing...?"