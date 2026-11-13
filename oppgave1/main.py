from rich import print

class Spaceship:
    def __init__(self, name, maxSpeed, speed, throtle, maxFuel, fuelEfficiency, fuel = None):
        if fuel == None:
            fuel = maxFuel
        self.name = name # Name of ship, ie Halberd. String
        self.maxSpeed = maxSpeed # Max speed of the ship. Int
        self.speed = speed # The current speed of the ship in KM/H. Float
        self.throtle = throtle # How much faster the ship gets when it speeds up. Float
        self.maxFuel = maxFuel # The max amount of fuel a ship can have. Int
        self.fuelEfficiency = fuelEfficiency # How much fuel the ship consumes per KM/H it speeds up. Float
        self.fuel = fuel # The current fuel the ship has. Float
        self.isExploded = False # Has the ship exploded? Bool

    def provideInfo(self):
        return f"I am spaceship [[{self.name}]].\nI am moving at [[{self.speed} KM/H]].\nMy max speed is [[{self.maxSpeed} KM/H]]\nI can speed up with [[{self.throtle} KM/H]] by using [[{self.fuelEfficiency} L]] fuel per [[KM/H]]\nMy current fuel level is at [[{self.fuel/(self.maxFuel/100):.2f}%]], aka [[{self.fuel}/{self.maxFuel} L]]"

    def speedUp(self):
        additionalMessage = "" # Provides extra flavor to the user when the function succeeds
        
        speedDiff = self.speed + self.throtle - self.maxSpeed # Check the difference between would-be new speed and max speed
        usedThrotle = self.throtle 
        if speedDiff > 0: # If speedDiff is a positive number, subract it from the throtle
            usedThrotle -= speedDiff
            additionalMessage += f" [[{self.name}]] is now at max speed!"

        usedFuel = self.fuelEfficiency * usedThrotle # Calc fuel usage
        fuelDiff = self.fuel - usedFuel # Check how much fuel the ship will have afterwards
        if fuelDiff < 0: # If future fuel is less than 0, it will
            additionalMessage += f" [[{self.name}]] is now out of fuel!"
            usedThrotle += fuelDiff / self.fuelEfficiency  # Due to the if, I am very sure that this will be negative. 1 - -1 = 2 and 1 + -1 = 0
            usedFuel = self.fuelEfficiency * usedThrotle
        
        self.speed += usedThrotle
        self.fuel -= self.fuelEfficiency*usedThrotle
        return f"Spaceship [[{self.name}]] has sped up to [[{self.speed:.2f} KM/H]] using [[{usedFuel:.2f} L]] fuel and has [[{self.fuel:.2f} L]] fuel remaining.{additionalMessage}"

jS = Spaceship("Johnathan Spaceship", 1997, 800, 100, 1000, 2.3, 453.5)
print(jS.provideInfo())
print(jS.speedUp())
print(jS.speedUp())