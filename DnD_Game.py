#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time
import sys

for_stats = 0
roll_stats = 5
rolls = []
stats = []
mods = {}
stat_types = {}

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
        rolls.append(roll_output)

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
        rolls.append(roll_output)

def stat_roll(u_class=None):
    global for_stats
    global roll_stats
    global rolls
    global stat_types
    global stats
    global mods
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
    if u_class == None or u_class == "":
        stat_types = {
        "Str": stats[0],
        "Dex": stats[1],
        "Con": stats[2],
        "Int": stats[3],
        "Wis": stats[4],
        "Cha": stats[5]
        }
    else:
        stats.sort()
        if u_class.lower() == "barbarian":
            stat_types = {
            "Str": stats[5],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[0],
            "Wis": stats[2],
            "Cha": stats[1]
            }
        elif u_class.lower() == "fighter":
            stat_types = {
            "Str": stats[5],
            "Dex": stats[1],
            "Con": stats[3],
            "Int": stats[4],
            "Wis": stats[0],
            "Cha": stats[2]
            }
        elif u_class.lower() == "wizard":
            stat_types = {
            "Str": stats[0],
            "Dex": stats[4],
            "Con": stats[3],
            "Int": stats[5],
            "Wis": stats[2],
            "Cha": stats[1]
            }
        elif u_class.lower() == "rogue":
            stat_types = {
            "Str": stats[0],
            "Dex": stats[5],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[3]
            }
        elif u_class.lower() == "bard":
            stat_types = {
            "Str": stats[0],
            "Dex": stats[4],
            "Con": stats[3],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[5]
            }
        elif u_class.lower() == "druid":
            stat_types = {
            "Str": stats[0],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[2],
            "Wis": stats[5],
            "Cha": stats[1]
            }
        elif u_class.lower() == "paladin":
            stat_types = {
            "Str": stats[5],
            "Dex": stats[1],
            "Con": stats[3],
            "Int": stats[0],
            "Wis": stats[2],
            "Cha": stats[4]
            }
        elif u_class.lower() == "cleric":
            stat_types = {
            "Str": stats[3],
            "Dex": stats[2],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[5],
            "Cha": stats[0]
            }
        elif u_class.lower() == "monk":
            stat_types = {
            "Str": stats[4],
            "Dex": stats[2],
            "Con": stats[3],
            "Int": stats[1],
            "Wis": stats[5],
            "Cha": stats[0]
            }
        elif u_class.lower() == "ranger":
            stat_types = {
            "Str": stats[5],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[0]
            }
        elif u_class.lower() == "sorcerer":
            stat_types = {
            "Str": stats[0],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[2],
            "Wis": stats[1],
            "Cha": stats[5]
            }
        elif u_class.lower() == "warlock":
            stat_types = {
            "Str": stats[0],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[5]
            }
        elif u_class.lower() == "artificer":
            stat_types = {
            "Str": stats[0],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[5],
            "Wis": stats[2],
            "Cha": stats[1]
            }
        elif u_class.lower() == "andrew" or u_class.lower() == "luca" or u_class.lower() == "kai":
            #easter egg for friends/fellow dms :)
            stats = [20]
            mods = {
                20: 5
                }
            stat_types = {
            "Str": stats[0],
            "Dex": stats[0],
            "Con": stats[0],
            "Int": stats[0],
            "Wis": stats[0],
            "Cha": stats[0]
            }
##        elif u_class.lower() == "z" or u_class.lower() == "zurulien":
##            stat_types = {
##            "Str": stats[4],
##            "Dex": stats[0],
##            "Con": stats[1],
##            "Int": stats[5],
##            "Wis": stats[3],
##            "Cha": stats[2]
##            }

    return stat_types
     
while roll_stats > 4:
            rolls = []
            start = input("Start? (y/n) ").lower().strip()
            if start == "y":
                user_class = input("What class do you choose? (Barbarian, Fighter, Wizard, Rogue, Bard, Druid, Paladin, Cleric, Monk, Ranger, Sorcerer, Warlock, Artificer) ").strip()
                roll_stats = 4
                stat_roll(user_class)
            else:
                sys.exit()

if user_class.lower() == "andrew" or user_class.lower() == "luca" or user_class.lower() == "kai":
    print(f"""You are {user_class}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
elif user_class.lower() == "artificer":
    print(f"""You are an {user_class}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
elif user_class.lower() == "" or user_class == None:
    print(f"""Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")

else:
    print(f"""You are a {user_class}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
