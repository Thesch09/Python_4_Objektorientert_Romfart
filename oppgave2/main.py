from rich import print
from spaceshipClass import Spaceship
from spaceSubclasses import spacechips, Observer, PeopleCarrier

observer1 = Observer("The Eye That Watches", 300, 10, 50, 5000, 5)
theCarrier = PeopleCarrier("The Killer", 5000, 5000, 200, 10000, 3.1, 1000, 157, 10000, 8012)
theCarrier = PeopleCarrier("The Saviour", 5000, 5000, 200, 10000, 3.1, 1000, 157, 1000, 500)

for chip in spacechips:
    print(chip.provideInfo())
    print(chip.speedUp())
    print(chip.specialAttack())
    print(chip.specialAttack())
    print()