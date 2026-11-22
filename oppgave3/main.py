#gwuess what, it's awnothwer mwain.pwy
from rich import print
from operativeSystems import machinations, FoolishOS, CheffOTron, Merrymer, RoboticSpiderThatWillEatEveryoneYouKnowAndLoveForSafety
import os

johnOS = FoolishOS("FoolishOS", "EVERYWHERE and EVERYWHEN", 10, 0.01, 10000)
kawasaki = CheffOTron("Chef Kawasaki", "Cappy Sector", 1000, 1.72, 25, "thin-wiches")
bump = Merrymer("Bump and Uctions", "Game Zone 3000", 124, 2.32, 4, ["The Binding of Isaac", "Shadow the Hedgehog", "Donkey Kong Bonanza"], "The ULTIMATE GAME")
turbo = RoboticSpiderThatWillEatEveryoneYouKnowAndLoveForSafety("Turbo", "Suger Rush", 1000, 0.73, 20, 200, 100, 7, (-7,4), "Turbotastic")

onlyRSTWEEYKALFS = input("Do you only want to see Robotic Spiders That Will Eat Everyone You Know And Love For Safety?\n").lower().strip()
while True:
    for machination in machinations:
        os.system('cls' if os.name == 'nt' else 'clear')
        if onlyRSTWEEYKALFS == "yes":
            try:
                numberThatOnlyAppearsIfYouOnlyWantRSTWEEYKALFS = machination.hp
            except AttributeError:
                continue
        print(machination.tickThisMachine())
        input("Press ENTER to continue")
        print()

    if input("Type \"END\" to end").lower().strip() == "end":
        break