import random
import time
import sys

for_stats = 0
roll_stats = 5
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
        time.sleep(1)
        roll_num = int(x[1:len(x)])
        roll_output = random.randint(1,roll_num)
        output_str = str(roll_output)
        if roll_output in an_list or str(output_str[0]) == "8":
            print(x + ": You rolled an", output_str + "!")
        else:
            print(x + ": You rolled a", output_str + "!")
        time.sleep(0.5)
        return rolls.append(roll_output)

def roll_no_output(di=None):
    if di == None:
        dice_chosen = input("What dice would you like to roll? (d[number] ")
    else:
        dice_chosen = di
    dice_list = dice_chosen.lower().split()
    an_list = [11, 18,]
    for x in dice_list:
        if "d" not in x:
            raise ValueError("Value must have a 'd' in front to specify that it is a dice")
        
        roll_num = int(x[1:len(x)])
        roll_output = random.randint(1,roll_num)
        return rolls.append(roll_output)

def stat_roll():
    global for_stats
    global roll_stats
    global rolls
    while for_stats < 6:
        while roll_stats > 0:
            roll_stats -= 1
            roll_no_output("d6")
            if rolls[-1] == 1:
                rolls.pop()
                roll_stats += 1
            elif len(rolls) == 4:
                rolls.remove(min(rolls))
                stats.append(sum(rolls))
                mods[stats[-1]] = (stats[-1] - 10)//2
                rolls = []
                for_stats += 1
                if for_stats >= 6:
                    break
                roll_stats = 5
     
while roll_stats > 4:
            rolls = []
            start = input("Start? (y/n) ").lower().strip()
            if start == "y":
                roll_stats = 4
                stat_roll()
            else:
                for_stats = 0
                break

stat_types = {
    "Str": stats[0],
    "Dex": stats[1],
    "Con": stats[2],
    "Int": stats[3],
    "Wis": stats[4],
    "Cha": stats[5]
    }

print(f"""Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
