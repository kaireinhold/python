#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time
import sys

for_stats = 0
roll_stats = 5
rolls = []
stats = []
mods = {
    1: -5,
    2: -4,
    3: -4,
    4: -3,
    5: -3,
    6: -2,
    7: -2,
    8: -1,
    9: -1,
    10: 0,
    11: 0,
    12: 1,
    13: 1,
    14: 2,
    15: 2,
    16: 3,
    17: 3,
    18: 4,
    19: 4,
    20: 5
    }
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
        if u_class.lower() == "barbarian":
            stats.sort()
            stat_types = {
            "Str": stats[5],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[0],
            "Wis": stats[2],
            "Cha": stats[1]
            }
        elif u_class.lower() == "fighter":
            stats.sort()
            stat_types = {
            "Str": stats[5],
            "Dex": stats[1],
            "Con": stats[3],
            "Int": stats[4],
            "Wis": stats[0],
            "Cha": stats[2]
            }
        elif u_class.lower() == "wizard":
            stats.sort()
            stat_types = {
            "Str": stats[0],
            "Dex": stats[4],
            "Con": stats[3],
            "Int": stats[5],
            "Wis": stats[2],
            "Cha": stats[1]
            }
        elif u_class.lower() == "rogue":
            stats.sort()
            stat_types = {
            "Str": stats[0],
            "Dex": stats[5],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[3]
            }
        elif u_class.lower() == "bard":
            stats.sort()
            stat_types = {
            "Str": stats[0],
            "Dex": stats[4],
            "Con": stats[3],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[5]
            }
        elif u_class.lower() == "druid":
            stats.sort()
            stat_types = {
            "Str": stats[0],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[2],
            "Wis": stats[5],
            "Cha": stats[1]
            }
        elif u_class.lower() == "paladin":
            stats.sort()
            stat_types = {
            "Str": stats[5],
            "Dex": stats[1],
            "Con": stats[3],
            "Int": stats[0],
            "Wis": stats[2],
            "Cha": stats[4]
            }
        elif u_class.lower() == "cleric":
            stats.sort()
            stat_types = {
            "Str": stats[3],
            "Dex": stats[2],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[5],
            "Cha": stats[0]
            }
        elif u_class.lower() == "monk":
            stats.sort()
            stat_types = {
            "Str": stats[4],
            "Dex": stats[2],
            "Con": stats[3],
            "Int": stats[1],
            "Wis": stats[5],
            "Cha": stats[0]
            }
        elif u_class.lower() == "ranger":
            stats.sort()
            stat_types = {
            "Str": stats[5],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[0]
            }
        elif u_class.lower() == "sorcerer":
            stats.sort()
            stat_types = {
            "Str": stats[0],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[2],
            "Wis": stats[1],
            "Cha": stats[5]
            }
        elif u_class.lower() == "warlock":
            stats.sort()
            stat_types = {
            "Str": stats[0],
            "Dex": stats[3],
            "Con": stats[4],
            "Int": stats[1],
            "Wis": stats[2],
            "Cha": stats[5]
            }
        elif u_class.lower() == "artificer":
            stats.sort()
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
            stat_types = {
            "Str": stats[0],
            "Dex": stats[0],
            "Con": stats[0],
            "Int": stats[0],
            "Wis": stats[0],
            "Cha": stats[0]
            }
        elif u_class.lower() == "z" or u_class.lower() == "zurulien":
            stats.sort()
            stat_types = {
            "Str": stats[4],
            "Dex": stats[0],
            "Con": stats[1],
            "Int": stats[5],
            "Wis": stats[3],
            "Cha": stats[2]
            }
        else:
            stat_types = {
        "Str": stats[0],
        "Dex": stats[1],
        "Con": stats[2],
        "Int": stats[3],
        "Wis": stats[4],
        "Cha": stats[5]
        }
    return stat_types

def stat_increase():
    inc_amount = int(input(""" How do you want to increase your stats?
(1) Increase 1 stat by 2 points
(2) Increase 2 stats by 1 point each
"""))
    if inc_amount == 1:
        stat_to_inc = input("What stat do you want to increase? (Choose 1: Str, Dex, Con, Int, Wis, Cha) ")
        counter = [1]
        for x in counter:
            if stat_to_inc.lower().strip() == "str":
                if stat_types["Str"] == 20:
                    continue
                else:
                    stat_types["Str"] += 2
            elif stat_to_inc.lower().strip() == "dex":
                if stat_types["Dex"] == 20:
                    continue
                else:
                    stat_types["Dex"] += 2
            elif stat_to_inc.lower().strip() == "con":
                if stat_types["Con"] == 20:
                    continue
                else:
                    stat_types["Con"] += 2
            elif stat_to_inc.lower().strip() == "int":
                if stat_types["Int"] == 20:
                    continue
                else:
                    stat_types["Int"] += 2
            elif stat_to_inc.lower().strip() == "wis":
                if stat_types["Wis"] == 20:
                    continue
                else:
                    stat_types["Wis"] += 2
            elif stat_to_inc.lower().strip() == "cha":
                if stat_types["Cha"] == 20:
                    continue
                else:
                    stat_types["Cha"] += 2
    elif inc_amount == 2:
        stats_to_inc = input("What stats do you want to increase? (Choose 2, separate by a comma: Str, Dex, Con, Int, Wis, Cha) ")
        inc_list = stats_to_inc.split(",")
        if len(inc_list) > 2:
            incs = inc_list
            inc_list = [incs[0], incs[1]]
        for stat in inc_list:
            if stat.lower().strip() == "str":
                if stat_types["Str"] == 20:
                    continue
                else:
                    stat_types["Str"] += 1
            elif stat.lower().strip() == "dex":
                if stat_types["Dex"] == 20:
                    continue
                else:
                    stat_types["Dex"] += 1
            elif stat.lower().strip() == "con":
                if stat_types["Con"] == 20:
                    continue
                else:
                    stat_types["Con"] += 1
            elif stat.lower().strip() == "int":
                if stat_types["Int"] == 20:
                    continue
                else:
                    stat_types["Int"] += 1
            elif stat.lower().strip() == "wis":
                if stat_types["Wis"] == 20:
                    continue
                else:
                    stat_types["Wis"] += 1
            elif stat.lower().strip() == "cha":
                if stat_types["Cha"] == 20:
                    continue
                else:
                    stat_types["Cha"] += 1

    print(stat_types)

def set_level():
    global user_level
    user_level = int(input("What level is your character? (number) "))
    if user_level >= 19:
        stat_increase()
        stat_increase()
        stat_increase()
        stat_increase()
        stat_increase()
    elif user_level >= 16:
        stat_increase()
        stat_increase()
        stat_increase()
        stat_increase()
    elif user_level >= 12:
        stat_increase()
        stat_increase()
        stat_increase()
    elif user_level >= 8:
        stat_increase()
        stat_increase()
    elif user_level >= 4:
        stat_increase()
    return user_level

while roll_stats > 4:
            rolls = []
            start = input("Start? (y/n) ").lower().strip()
            if start == "y":
                user_class = input("What class do you choose? (Barbarian, Fighter, Wizard, Rogue, Bard, Druid, Paladin, Cleric, Monk, Ranger, Sorcerer, Warlock, Artificer) ").strip()
                roll_stats = 4
                stat_roll(user_class)
                print(stats)
                print(stat_types)
                set_level()
            else:
                sys.exit()

if user_class.lower() == "andrew" or user_class.lower() == "luca" or user_class.lower() == "kai" or user_class.lower() == "z" or user_class.lower() == "zurulien":
    print(f"""You are {user_class}! Your level is {user_level}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
    
elif user_class.lower() == "artificer":
    print(f"""You are an {user_class}! Your level is {user_level}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
    
elif user_class == None or user_class == "" or user_class != 'barbarian' or user_class != 'fighter' or user_class != 'wizard' or user_class != 'rogue' or user_class != 'bard' or user_class != 'druid' or user_class != 'paladin' or user_class != 'cleric' or user_class != 'monk' or user_class != 'ranger' or user_class != 'sorcerer' or user_class != 'warlock' or user_class != 'artificer' or user_class != 'andrew' or user_class != 'luca' or user_class != 'kai' or user_class != 'z' or user_class != "zurulien":
    print(f"""Your level is {user_level}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
    
else:
    print(f"""You are a {user_class}! Your level is {user_level}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})
""")
