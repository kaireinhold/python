import random
import time
import sys

forstats = 0
rollstats = 5
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

def statrolls():
    global forstats
    global rollstats
    global rolls
    global stats
    global mods
    while forstats < 6:
        while rollstats > 0:
            rollstats -= 1
            roll("d6")
            if rolls[-1] == 1:
                rolls.pop()
                rollstats += 1
            elif len(rolls) == 4:
                print(rolls)
                rolls.remove(min(rolls))
                stats.append(sum(rolls))
                print(sum(rolls))
                mods[stats[-1]] = (stats[-1] - 10)//2
                rolls = []
                forstats += 1
                if forstats >= 6:
                    print(stats)
                    print(mods)
                    break
                rollstats = 5
     
while rollstats > 4:
            rolls = []
            start = input("Start? (y/n) ").lower().strip()
            if start == "y":
                rollstats = 4
                statrolls()
            else:
                forstats = 0
                break
