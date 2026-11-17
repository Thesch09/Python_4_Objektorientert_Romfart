#gwuess what, it's awnothwer mwain.pwy
from rich import print
from operativeSystems import machinations, FoolishOS, CheffOTron, Merrymer

johnOS = FoolishOS("FoolishOS", "EVERYWHERE and EVERYWHEN", 10, 0.01, 10000)
kawasaki = CheffOTron("Chef Kawasaki", "Cappy Sector", 1000, 1.72, 25, "thin-wiches")
bump = Merrymer("Bump and Uctions", "Game Zone 3000", 124, 2.32, 4, ["The Binding of Isaac", "Shadow the Hedgehog", "Donkey Kong Bonanza"], "The ULTIMATE GAME")

while True:
    for machination in machinations:
        print()
        machination.tickThisMachine()
        input("Press ENTER to continue")
        print()

    if input("Type \"END\" to end").lower().strip() == "end":
        break