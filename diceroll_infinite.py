#Created by Kai Reinhold (kaireinhold on GitHub)

import rollDice
from rollDice import Dice

# Create an instance of the Dice class
dice = Dice()

while True:
    roll_a_dice = input("Would you like to roll a dice? (y/n) ").lower().strip()
    if roll_a_dice == "y" or roll_a_dice == "yes":
        dice.roll()  # Call the roll method of the dice object
        print(dice.rolls)  # Print the rolls from the dice instance
    else:
        print("Goodbye!")
        break
