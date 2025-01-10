#import rollDice as r
import characterCreate
import random
import time
import sys

#diceroll = False
#makechar = False
#editchar = False
#dict_Name = {}
none = True
play = False
rolls = []
def roll(di=None):
    """
    Simulate rolling dice with a specified number of sides and display the result.

    Input:
    - d<number> (str): A string where <number> represents the number of sides on the dice to roll, chosen by the user (e.g., 'd20' for a 20-sided die).
    
    Output:
    - str: A message indicating "Rolling d<number>..." followed by a wait of 1.5 seconds, and then another message displaying the rolled value (e.g., "d<number>: You rolled a <rolled value>!").
    
    Behavior:
    - Prompts the user to input a dice to roll (ie. 'd20' for a 20-sided dice.)
    - Rolls the specified dice and prints the result.
    - Waits for 1.5 seconds before displaying the result.
    - Detects if the rolled number should be preceded by 'an' (for example, 8 or 18) and adjusts the output message accordingly.

    Raises:
    - ValueError: If the input does not include the 'd' prefix, indicating the dice format.
        
    """

    if di == None:
        dice_chosen = input("What dice would you like to roll? (d[number] ")
    else:
        dice_chosen = di
    dice_list = dice_chosen.lower().split()
    an_list = [11, 18,]
    for x in dice_list:
        if "d" not in x:
            raise ValueError("Value must have a 'd' in front to specify that it is a dice")
        
        print("Rolling "  + x + "...")
        #time.sleep(1.5)
        roll_num = int(x[1:len(x)])
        roll_output = random.randint(1,roll_num)
        output_str = str(roll_output)
        if roll_output in an_list or str(output_str[0]) == "8":
            print(x + ": You rolled an", output_str + "!")
        else:
            print(x + ": You rolled a", output_str + "!")
        #time.sleep(1)
        return rolls.append(roll_output)
while none == True:
    while play == False:
        rolls = []
        start = input("Start? (y/n) ").lower().strip()
        if start == "y":
            play = True
        else:
            none = False
            break

    while play == True:
        roll("d100")
        if rolls[-1] == 1:
            print(rolls)
            print(len(rolls))
            play = False
            
        """elif rolls[-1] in rolls[0:-1]:
            print(rolls)
            print(len(rolls))
            play = False"""

#while play == True:
#    todo = input("""
#What would you like to do?
#(R)oll A Dice
#(M)ake A New Character
#(E)dit character
#(N) Exit
#""").lower().strip()
#    if todo == "r":
#        diceroll = True
#    elif todo == "m":
#        makechar = True
#    elif todo == "e":
#        try:
#            characterCreate.edit_Character()
#        except:
#            print("NameError: You have not made a character yet.")
#    elif todo == "n":
#        play = False
#        time.sleep(0.5)
#    else:
#        raise ValueError("Not a valid input")
#    while diceroll == True:
#        dice_Q = input("Would you like to roll a dice? (y/n)").lower().strip()
#        if dice_Q == "y":
#            r.dice.roll()
#            time.sleep(1)
#        elif dice_Q == "n":
#            time.sleep(1)
#            diceroll = False
#    while makechar == True:
#        characterCreate.new_Character()
#        makechar = False
#    while editchar == True:
#        characterCreate.edit_Character()
#        editchar = False
        
