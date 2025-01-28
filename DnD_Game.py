#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import os

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
    for_stats = 0
    roll_stats = 5
    rolls = []
    stats = []
    mods = {1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5}
    stat_types = {}
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
        stat_types = {"Str": stats[0], "Dex": stats[1], "Con": stats[2], "Int": stats[3], "Wis": stats[4], "Cha": stats[5]}
    else:
        if u_class.lower() == "barbarian":
            stats.sort()
            stat_types = {"Str": stats[5], "Dex": stats[3], "Con": stats[4], "Int": stats[0], "Wis": stats[2], "Cha": stats[1]}
        elif u_class.lower() == "fighter":
            stats.sort()
            stat_types = {"Str": stats[5], "Dex": stats[1], "Con": stats[3], "Int": stats[4], "Wis": stats[0], "Cha": stats[2]}
        elif u_class.lower() == "wizard":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[4], "Con": stats[3], "Int": stats[5], "Wis": stats[2], "Cha": stats[1]}
        elif u_class.lower() == "rogue":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[5], "Con": stats[4], "Int": stats[1], "Wis": stats[2], "Cha": stats[3]}
        elif u_class.lower() == "bard":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[4], "Con": stats[3], "Int": stats[1], "Wis": stats[2], "Cha": stats[5]}
        elif u_class.lower() == "druid":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[2], "Wis": stats[5], "Cha": stats[1]}
        elif u_class.lower() == "paladin":
            stats.sort()
            stat_types = {"Str": stats[5], "Dex": stats[1], "Con": stats[3], "Int": stats[0], "Wis": stats[2], "Cha": stats[4]}
        elif u_class.lower() == "cleric":
            stats.sort()
            stat_types = {"Str": stats[3], "Dex": stats[2], "Con": stats[4], "Int": stats[1], "Wis": stats[5], "Cha": stats[0]}
        elif u_class.lower() == "monk":
            stats.sort()
            stat_types = {"Str": stats[4], "Dex": stats[2], "Con": stats[3], "Int": stats[1], "Wis": stats[5], "Cha": stats[0]}
        elif u_class.lower() == "ranger":
            stats.sort()
            stat_types = {"Str": stats[5], "Dex": stats[3], "Con": stats[4], "Int": stats[1], "Wis": stats[2], "Cha": stats[0]}
        elif u_class.lower() == "sorcerer":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[2], "Wis": stats[1], "Cha": stats[5]}
        elif u_class.lower() == "warlock":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[1], "Wis": stats[2], "Cha": stats[5]}
        elif u_class.lower() == "artificer":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[5], "Wis": stats[2], "Cha": stats[1]}
        elif u_class.lower() == "andrew" or u_class.lower() == "luca" or u_class.lower() == "kai":
            #easter egg for friends/fellow dms :)
            stats = [20]
            stat_types = {"Str": stats[0], "Dex": stats[0], "Con": stats[0], "Int": stats[0], "Wis": stats[0], "Cha": stats[0]}
            user_class = ""
        elif u_class.lower() == "z" or u_class.lower() == "zurulien":
            stats.sort()
            stat_types = {"Str": stats[4], "Dex": stats[0], "Con": stats[1], "Int": stats[5], "Wis": stats[3], "Cha": stats[2]}
        else:
            stat_types = {"Str": stats[0], "Dex": stats[1], "Con": stats[2], "Int": stats[3], "Wis": stats[4], "Cha": stats[5]}
    return stat_types

def stat_increase(inc_amount = None):
    if inc_amount == None:
        inc_amount = int(input(""" How do you want to increase your stats?
(1) Increase 1 stat by 2 points
(2) Increase 2 stats by 1 point each
"""))
    if inc_amount == 1:
        stat_to_inc = input("What stat do you want to increase? (Choose 1: Str, Dex, Con, Int, Wis, Cha) ")
        counter = [1]
        for x in counter:
            if stat_to_inc.lower().strip() == "str":
                if stat_types["Str"] >= 19:
                    stat_types["Str"] = 20
                else:
                    stat_types["Str"] += 2
            elif stat_to_inc.lower().strip() == "dex":
                if stat_types["Dex"] >= 19:
                    stat_types["Dex"] = 20
                else:
                    stat_types["Dex"] += 2
            elif stat_to_inc.lower().strip() == "con":
                if stat_types["Con"] >= 19:
                    stat_types["Con"] = 20
                else:
                    stat_types["Con"] += 2
            elif stat_to_inc.lower().strip() == "int":
                if stat_types["Int"] >= 19:
                    stat_types["Int"] = 20
                else:
                    stat_types["Int"] += 2
            elif stat_to_inc.lower().strip() == "wis":
                if stat_types["Wis"] >= 19:
                    stat_types["Wis"] = 20
                else:
                    stat_types["Wis"] += 2
            elif stat_to_inc.lower().strip() == "cha":
                if stat_types["Cha"] >= 19:
                    stat_types["Cha"] = 20
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
                if stat_types["Str"] >= 20:
                    stat_types["Str"] = 20
                else:
                    stat_types["Str"] += 1
            elif stat.lower().strip() == "dex":
                if stat_types["Dex"] >= 20:
                    stat_types["Dex"] = 20
                else:
                    stat_types["Dex"] += 1
            elif stat.lower().strip() == "con":
                if stat_types["Con"] >= 20:
                    stat_types["Con"] = 20
                else:
                    stat_types["Con"] += 1
            elif stat.lower().strip() == "int":
                if stat_types["Int"] >= 20:
                    stat_types["Int"] = 20
                else:
                    stat_types["Int"] += 1
            elif stat.lower().strip() == "wis":
                if stat_types["Wis"] >= 20:
                    stat_types["Wis"] = 20
                else:
                    stat_types["Wis"] += 1
            elif stat.lower().strip() == "cha":
                if stat_types["Cha"] >= 20:
                    stat_types["Cha"] = 20
                else:
                    stat_types["Cha"] += 1

    print(stat_types)

def set_level():
    global user_level
    user_level = int(input("What level is your character? (number) "))
    if user_level >= 19:
        stat_increase(), stat_increase(), stat_increase(), stat_increase(), stat_increase()
    elif user_level >= 16:
        stat_increase(), stat_increase(), stat_increase(), stat_increase()
    elif user_level >= 12:
        stat_increase(), stat_increase(), stat_increase()
    elif user_level >= 8:
        stat_increase(), stat_increase()
    elif user_level >= 4:
        stat_increase()
    return user_level

def set_race(race = None):
    global user_race
    global movement_speed
    global darkvision
    global languages
    if race == None:
        user_race = input("What race is your character? (Dwarf, Half-orc, Elf, Halfling, Human, Dragonborn, Gnome, Half-elf, Tiefling, Aasimar, Changeling, Kenku, Warforged, Arachne, Shifter, Aarakocra, Kobold, Fire Genasi, Air Genasi, Earth Genasi, Water Genasi) ")
    else:
        user_race = race    
    if user_race.lower().strip() == "dwarf":
        stat_types["Con"] += 2
        movement_speed = 25
        darkvision = True
        languages = ["Common", "Dwarvish"]
    elif user_race.lower().strip() == "half-orc":
        stat_types["Str"] += 2
        stat_types["Con"] += 1
        movement_speed = 30
        darkvision = True
        languages = ["Common", "Orc"]
    elif user_race.lower().strip() == "elf":
        stat_types["Dex"] += 2
        movement_speed = 30
        darkvision = True
        languages = ["Common", "Elven"]
    elif user_race.lower().strip() == "halfling":
        stat_types["Dex"] += 2
        movement_speed = 25
        darkvision = False
        languages = ["Common", "Halfling"]
    elif user_race.lower().strip() == "human":
        stat_types["Str"] += 1
        stat_types["Dex"] += 1
        stat_types["Con"] += 1
        stat_types["Int"] += 1
        stat_types["Wis"] += 1
        stat_types["Cha"] += 1
        movement_speed = 30
        darkvision = False
        languages = ["Common", input("Choose 1 language other than Common: ")]
    elif user_race.lower().strip() == "dragonborn":
        stat_types["Str"] += 2
        stat_types["Cha"] += 1
        movement_speed = 30
        darkvision = False
        languages = ["Common", "Draconic"]
    elif user_race.lower().strip() == "gnome":
        stat_types["Int"] += 2
        movement_speed = 25
        darkvision = True
        languages = ["Common", "Gnomish"]
    elif user_race.lower().strip() == "half-elf":
        stat_types["Cha"] += 2
        stat_increase(2)
        movement_speed = 30
        darkvision = True
        languages = ["Common", "Elven", input("Choose 1 language other than Common and Elven: ")]
    elif user_race.lower().strip() == "tiefling":
        stat_types["Cha"] += 2
        movement_speed = 30
        darkvision = True
        languages = ["Common", "Infernal"]
    elif user_race.lower().strip() == "aasimar" or user_race.lower().strip() == "changeling" or user_race.lower().strip() == "kenku" or user_race.lower().strip() == "shifter" or user_race.lower().strip() == "aarakocra" or user_race.lower().strip() == "kobold" or user_race.lower().strip() == "fire genasi" or user_race.lower().strip() == "air genasi" or user_race.lower().strip() == "water genasi" or user_race.lower().strip() == "earth genasi":
        stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha): ")] += 1
        inc_2 = int(input("Would you like to increase one score by 2 points (1), or 2 scores by 1 point each (2)? "))
        if inc_2 == 1:
            stat_increase(1)
        elif inc_2 == 2:
            stat_increase(2)
        if user_race.lower().strip() == "air genasi":
            movement_speed = 35
        else:
            movement_speed = 30
        darkvision = True
        languages = ["Common", input("What language other than Common have you agreed on with your DM? ")]
    elif user_race.lower().strip() == "warforged":
        stat_types["Con"] += 2
        stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha): ")] += 1
        movement_speed = 30
        darkvision = False
        languages = ["Common", input("Choose 1 language other than Common: ")]
    elif user_race.lower().strip() == "arachne":
        stat_types["Dex"] += 2
        stat_types["Wis"] += 1
        movement_speed = 30
        darkvision = True
        languages = ["Common", "Undercommon"]
    elif user_race.lower().strip() == "starling" or user_race.lower().strip() == "bloodling" or user_race.lower().strip() == "core starling" or user_race.lower().strip() == "shadeling" or user_race.lower().strip() == "crystalling" or user_race.lower().strip() == "symbioling" or user_race.lower().strip() == "pure starling":
        current_race = user_race
        if user_race.lower().strip() != "pure starling":
            prev_race = input("What race were you before? ")
            set_race(prev_race)
            movement_speed += 10
        else:
            set_race("human")
            movement_speed += 15
        user_race = current_race
        stat_increase(2)
        darkvision = True
        languages.append("Sangulect")
    else:
        movement_speed = 30
        darkvision = False
        languages = ["Common"]
    print(stat_types)

while True:
    rolls = []
    start = input("Start? (y/n) ").lower().strip()
    if start == "y":
        username = os.getlogin()
        save = input("Would you like to save your character to a text file? (y/n) ")
        if save.lower().strip() == "y":
            save_type = input("Would you like to overwrite a file that was already made (or make a new file) (1), or add to a file that was already made (2)? ").lower().strip()
        char_name = input("What is your character's name? ")
        user_class = input("What class do you choose? (Barbarian, Fighter, Wizard, Rogue, Bard, Druid, Paladin, Cleric, Monk, Ranger, Sorcerer, Warlock, Artificer) ").strip()
        roll_stats = 4
        stat_roll(user_class)
        print(stat_types)
        if char_name.lower().strip() == "z" or char_name.lower().strip() == "zurulien":
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
    print(f"You know these languages:")
    for x in languages:
        print("-", x)

    if save.lower().strip() == "y":
        # Define the absolute path where you want to create the folder
        folder_path = f"C:\\Users\\{username}\\Documents\\character_sheets"  # Change this path as needed

        # Check if the folder already exists
        if not os.path.exists(folder_path):
            # If the folder doesn't exist, create it
            os.makedirs(folder_path)
        file_name = f"{char_name}_character_sheet.txt"  # Adjust this to your dynamic name
        full_path = os.path.join(folder_path, file_name)

        if save_type == "1":
            with open(full_path, "w+") as file:
                file.write(f"""
Name: {char_name}
Class: {user_class}
Race: {user_race}
Level: {user_level}
Alignment: {alignment}

Stats:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]}))
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]}))
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]}))
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]}))
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]}))
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]}))

Movement Speed: {movement_speed}\n""")

                if darkvision == True:
                    file.write("""Darkvision\n""")
    
                file.write("\nLanguages:\n")
                for x in languages:
                    file.write(f"- {x}\n")

                # Create a hidden root window
                root = tk.Tk()
                root.withdraw()  # Hide the root window

                # Set the root window as topmost
                root.attributes('-topmost', True)

                # Show the messagebox
                messagebox.showinfo("Success", f"Character sheet saved to {char_name}_character_sheet.txt!")

                # Reset the topmost attribute and destroy the root window
                root.attributes('-topmost', False)
                root.destroy()
                file.seek(0) # Move the file pointer to the beginning before reading
                print(file.read()) # Read the file contents and print it
                print(f'Absolute path to the file: {full_path}')
                file.close()

        if save_type == "2":
            with open(full_path, "a+") as file:
                file.write(f"""
Name: {char_name}
Class: {user_class}
Race: {user_race}
Level: {user_level}
Alignment: {alignment}

Stats:
Strength: {stat_types["Str"]} ({mods[stat_types["Str"]]}))
Dexterity: {stat_types["Dex"]} ({mods[stat_types["Dex"]]}))
Constitution: {stat_types["Con"]} ({mods[stat_types["Con"]]}))
Intelligence: {stat_types["Int"]} ({mods[stat_types["Int"]]}))
Wisdom: {stat_types["Wis"]} ({mods[stat_types["Wis"]]}))
Charisma: {stat_types["Cha"]} ({mods[stat_types["Cha"]]}))

Movement Speed: {movement_speed}\n""")

                if darkvision == True:
                    file.write("""Darkvision\n""")
    
                file.write("\nLanguages:\n")
                for x in languages:
                    file.write(f"- {x}\n")

                # Create a hidden root window
                root = tk.Tk()
                root.withdraw()  # Hide the root window

                # Set the root window as topmost
                root.attributes('-topmost', True)

                # Show the messagebox
                messagebox.showinfo("Success", f"Character sheet saved to {char_name}_character_sheet.txt!")

                # Reset the topmost attribute and destroy the root window
                root.attributes('-topmost', False)
                root.destroy()
                file.seek(0) # Move the file pointer to the beginning before reading
                print(file.read()) # Read the file contents and print it
                print(f'Absolute path to the file: {full_path}')
                file.close()


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
