from rich import print
from spaceshipClass import Spaceship, spacechips

jS = Spaceship("Johnathan Spaceship", 1997, 800, 100, 1000, 2.3, 453.5)
dolphin = Spaceship("S.S. Dolphin", 20010, 2001, 201, 20010, 2.1)
theThirdShip = Spaceship("The Third Shiptuary", 2400, 240, 70, 2400, 0.24)
for chip in spacechips:
    print(chip.provideInfo())
    print(chip.speedUp())
    print()

print(jS.provideInfo())
print(jS.speedUp())