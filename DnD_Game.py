import rollDice
import characterCreate
import time
import sys

diceroll = False
makechar = False
none = False

start = input("Start? ").lower().strip()
if start == "yes":
    none = True
else:
    none = False
    sys.exit()

while none == True:
    todo = input("""
What would you like to do?
Roll A Dice
Make A New Character
""").lower().strip()
    if todo == "roll a dice":
        diceroll = True
    elif todo == "make a new character":
        makechar = True
    else:
        none = False
        time.sleep(0.5)
        sys.exit()
    
    while diceroll == True:
        dice_Q = input("Would you like to roll a dice? ").lower().strip()
        if dice_Q == "yes":
            rollDice.roll()
            time.sleep(1)
        elif dice_Q == "no":
            print("ok")
            time.sleep(1)
            diceroll = False
    while makechar == True:
        characterCreate.new_Character()
        makechar = False
