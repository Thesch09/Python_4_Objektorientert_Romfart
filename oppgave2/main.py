from rich import print
from spaceshipClass import Spaceship
from spaceSubclasses import spacechips, Observer, PeopleCarrier, OrbitalLaser

observer1 = Observer("The Eye That Watches", 300, 10, 50, 5000, 5)
theCarrier = PeopleCarrier("The Killer", 5000, 5000, 200, 10000, 3.1, 1000, 157, 10000, 8012)
theCarrier = PeopleCarrier("The Saviour", 5000, 5000, 200, 10000, 3.1, 1000, 157, 1000, 500)
orbeez = OrbitalLaser("Orbeez", 1000, 0, 500, 10000, 0.5, "the Asteroids")
spc = OrbitalLaser("Space Colony Ark", 10000, 200, 200, 2000000, 2, "THE MOON", "OBAMA")

for chip in spacechips:
    print(chip.provideInfo())
    print(chip.speedUp())
    print(chip.specialAttack())
    print()