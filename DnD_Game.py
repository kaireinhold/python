#import rollDice as r
import characterCreate
import random
import time
import sys

#diceroll = False
#makechar = False
#editchar = False
#dict_Name = {}
none = 0
play = 5
rolls = []
stats = []
mods = {}
def roll(di=None):
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
while none < 6:
    while play > 4:
        rolls = []
        start = input("Start? (y/n) ").lower().strip()
        if start == "y":
            play = 4
        else:
            none = False
            break

    while play > 0:
        play -= 1
        roll("d6")
        if rolls[-1] == 1:
            rolls.pop()
            play += 1
        elif len(rolls) == 4:
            print(rolls)
            rolls.remove(min(rolls))
            stats.append(sum(rolls))
            print(sum(rolls))
            mods[stats[-1]] = (stats[-1] - 10)//2
            rolls = []
            none += 1
            if none >= 6:
                print(stats)
                print(mods)
                break
            play = 5

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
        
