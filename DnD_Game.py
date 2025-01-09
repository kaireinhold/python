import rollDice
import characterCreate
import time
import sys

diceroll = False
makechar = False
editchar = False
none = False

start = input("Start? (y/n) ").lower().strip()
if start == "y":
    none = True
else:
    none = False
    sys.exit()

while none == True:
    todo = input("""
What would you like to do?
(R)oll A Dice
(M)ake A New Character
(E)dit character
(N) Exit
""").lower().strip()
    if todo == "r":
        diceroll = True
    elif todo == "m":
        makechar = True
    elif todo == "e":
        editchar = True
    elif todo == "n":
        none = False
        time.sleep(0.5)
    else:
        raise ValueError("Not a valid input")
    while diceroll == True:
        dice_Q = input("Would you like to roll a dice? (y/n)").lower().strip()
        if dice_Q == "y":
            rollDice.roll()
            time.sleep(1)
        elif dice_Q == "n":
            time.sleep(1)
            diceroll = False
    while makechar == True:
        characterCreate.new_Character()
        makechar = False
    while editchar == True:
        characterCreate.edit_Character()
        editchar = False
        
