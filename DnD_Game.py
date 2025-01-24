#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time
import sys
from DnD_function_library import *

rolls = []
stats = []
stat_types = {}
for_stats = 0
roll_stats = 5
user_race = ""
movement_speed = 30
darkvision = False
languages = []

while roll_stats > 4:
            rolls = []
            start = input("Start? (y/n) ").lower().strip()
            if start == "y":
                user_class = input("What class do you choose? (Barbarian, Fighter, Wizard, Rogue, Bard, Druid, Paladin, Cleric, Monk, Ranger, Sorcerer, Warlock, Artificer) ").strip()
                roll_stats = 4
                stat_roll(user_class)
                print(stat_types)
                if user_class.lower().strip() == "z" or user_class.lower().strip() == "zurulien":
                    set_race("Pure Starling")
                else:
                    set_race()
                set_level()
                alignment = input("What is your alignment? (Chaotic Good, Neutral Good, Lawful Good, Lawful Neutral, True Neutral, Chaotic Neutral, Lawful Evil, Neutral Evil, Chaotic Evil) ")
            else:
                sys.exit()

if user_class.lower() == "andrew" or user_class.lower() == "luca" or user_class.lower() == "kai" or user_class.lower() == "z" or user_class.lower() == "zurulien":
    print(f"""You are {user_class}!
Your level is {user_level}!
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
    
elif user_class == None or user_class == "" or user_class.lower() != 'barbarian' and user_class.lower() != 'fighter' and user_class.lower() != 'wizard' and user_class.lower() != 'rogue' and user_class.lower() != 'bard' and user_class.lower() != 'druid' and user_class.lower() != 'paladin' and user_class.lower() != 'cleric' and user_class.lower() != 'monk' and user_class.lower() != 'ranger' and user_class.lower() != 'sorcerer' and user_class.lower() != 'warlock' and user_class.lower() != 'artificer':
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
    print(f"""You are a {user_class}!
Your level is {user_level}!
Your stats are:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]})
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]})
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]})
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]})
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]})
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]})""")
print(f"Your alignment is {alignment}!")

if user_race.lower().strip() == "aasimar" or user_race.lower().strip() == "air genasi" or user_race.lower().strip() == "arachne" or user_race.lower().strip() == "aarakocra" or user_race.lower().strip() == "earth genasi" or user_race.lower().strip() == "elf":
    print(f"You are an {user_race}!")
else:
    print(f"You are a {user_race}!")

print(f"Your movement speed is {movement_speed}!")
if darkvision == True:
    print("You have darkvision!")
else:
    None
print(f"You know these languages:")
for x in languages:
      print("-", x)

'''
TBA:
-Core Starling
-Starling
-Shadeling
-Crystalling
-Bloodling
-Pure Starling
-Symbioling
Silenced
Starved
'''
