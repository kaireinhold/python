#Created by Kai Reinhold (kaireinhold on GitHub)

# Importing necessary libraries
import random  # For generating random numbers
import time    # For adding delays between actions
import sys     # Provides access to some variables used by the interpreter
import tkinter as tk  # Tkinter for creating GUI components
from tkinter import ttk, messagebox  # Importing specific Tkinter widgets
import os      # For interacting with the operating system

# Function to simulate rolling dice with output shown
def roll(di=None):
    global rolls
    global roll_output
    
    # Check if a dice parameter is passed, otherwise ask for user input
    if di == None:
        dice_chosen = input("What dice would you like to roll? (d[number] ")
    else:
        dice_chosen = di

    # Split the input string into individual dice types (e.g., "d6", "d20")
    dice_list = dice_chosen.lower().split()

    # List of "special" dice values to highlight
    an_list = [11, 18,]  # Dice numbers that should get a special message
    
    # Loop through each dice type chosen by the user
    for x in dice_list:
        # Ensure each dice entry contains the letter 'd' (to denote a dice)
        if "d" not in x:
            raise ValueError("Value must have a 'd' in front to specify that it is a dice")
        
        # Print the rolling message with a brief delay to simulate a dice roll
        print("Rolling "  + x + "...")
        time.sleep(1)
        
        # Extract the number of sides on the dice (after the 'd')
        roll_num = int(x[1:len(x)])

        # Generate a random roll result between 1 and the number of sides
        roll_output = random.randint(1, roll_num)
        
        # Convert the roll result to a string for easier manipulation
        output_str = str(roll_output)
        
        # If the roll result is in the special list or starts with '8', print a different message
        if roll_output in an_list or str(output_str[0]) == "8":
            print(x + ": You rolled an", output_str + "!")
        else:
            print(x + ": You rolled a", output_str + "!")
        
        # Small delay before the next roll to simulate realism
        time.sleep(0.5)

        # Append the result of the roll to a global list `rolls`
        rolls.append(roll_output)
    return rolls, roll_output

# Function to simulate rolling dice without displaying the output
def roll_no_output(di=None):
    global rolls
    global roll_output
    # Check if a dice parameter is passed, otherwise ask for user input
    if di == None:
        dice_chosen = input("What dice would you like to roll? (d[number] ")
    else:
        dice_chosen = di

    # Split the input string into individual dice types (e.g., "d6", "d20")
    dice_list = dice_chosen.lower().split()

    # List of "special" dice values to highlight (though not used here)
    an_list = [11, 18,]

    # Loop through each dice type chosen by the user
    for x in dice_list:
        # Ensure each dice entry contains the letter 'd' (to denote a dice)
        if "d" not in x:
            raise ValueError("Value must have a 'd' in front to specify that it is a dice")
        
        # Extract the number of sides on the dice (after the 'd')
        roll_num = int(x[1:len(x)])

        # Generate a random roll result between 1 and the number of sides
        roll_output = random.randint(1, roll_num)

        # Append the result of the roll to a global list `rolls`
        rolls.append(roll_output)
    return rolls, roll_output


# Function to simulate rolling stats for a character (ability scores)
def stat_roll(u_class=None):
    # Declare global variables to track stats, rolls, and stat modifiers
    global for_stats
    global roll_stats
    global rolls
    global stat_types
    global stats
    
    # Initialize variables for tracking the number of stats to roll and the rolls
    for_stats = 0
    roll_stats = 5  # 5 rolls per stat
    rolls = []  # List to hold individual roll results
    stats = []  # List to hold the sum of the rolled stats
    stat_types = {}  # Dictionary to store the final ability scores

    # Loop to generate the 6 stats (Str, Dex, Con, Int, Wis, Cha)
    while for_stats < 6:
        # Roll stats by rolling a d6 5 times (standard stat rolling)
        while roll_stats > 0:
            roll_stats -= 1  # Decrease the number of rolls remaining for this stat
            roll_no_output("d6")  # Call the function to roll a d6 (side effect: updates `rolls`)
            
            # If a roll is a 1, discard it and roll again (penalizing bad rolls)
            if rolls[-1] == 1:
                rolls.pop()  # Remove the 1 from the rolls list
                roll_stats += 1  # Increase the roll count to redo this roll
            elif len(rolls) == 4:
                # After 4 valid rolls, discard the lowest roll and sum the rest
                rolls.remove(min(rolls))  # Remove the smallest value
                stats.append(sum(rolls))  # Append the sum of the remaining 3 rolls to `stats`
                rolls = []  # Reset the rolls list for the next stat
                for_stats += 1  # Increment the stat count
                if for_stats >= 6:
                    break  # Stop once all 6 stats are rolled
                roll_stats = 5  # Reset the roll count for the next stat

    # Special stat assignment for specific character names (Easter egg for certain characters)
    if char_name.lower() == "z" or char_name.lower() == "zurulien":
        stats.sort()  # Sort stats for this character
        stat_types = {"Str": stats[4], "Dex": stats[0], "Con": stats[1], "Int": stats[5], "Wis": stats[3], "Cha": stats[2]}  # Assign stats
    elif char_name.lower() == "andrew" or char_name.lower() == "luca" or char_name.lower() == "kai":
        # Special Easter egg for friends/fellow DMs
        stats = [20]  # Assign max value (20) to all stats
        stat_types = {"Str": stats[0], "Dex": stats[0], "Con": stats[0], "Int": stats[0], "Wis": stats[0], "Cha": stats[0]}  # Set all stats to 20
    elif u_class == None or u_class == "":
        # If no class is specified, just assign stats in order
        stat_types = {"Str": stats[0], "Dex": stats[1], "Con": stats[2], "Int": stats[3], "Wis": stats[4], "Cha": stats[5]}
    else:
        # Assign stats based on the selected class (this part handles class-specific stat priorities)
        if u_class[0].lower() == "barbarian":
            stats.sort()  # Sort stats in ascending order
            stat_types = {"Str": stats[5], "Dex": stats[3], "Con": stats[4], "Int": stats[0], "Wis": stats[2], "Cha": stats[1]}  # Assign stats based on class
        elif u_class[0].lower() == "fighter":
            stats.sort()
            stat_types = {"Str": stats[5], "Dex": stats[1], "Con": stats[3], "Int": stats[4], "Wis": stats[0], "Cha": stats[2]}
        elif u_class[0].lower() == "wizard":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[4], "Con": stats[3], "Int": stats[5], "Wis": stats[2], "Cha": stats[1]}
        elif u_class[0].lower() == "rogue":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[5], "Con": stats[4], "Int": stats[1], "Wis": stats[2], "Cha": stats[3]}
        elif u_class[0].lower() == "bard":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[4], "Con": stats[3], "Int": stats[1], "Wis": stats[2], "Cha": stats[5]}
        elif u_class[0].lower() == "druid":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[2], "Wis": stats[5], "Cha": stats[1]}
        elif u_class[0].lower() == "paladin":
            stats.sort()
            stat_types = {"Str": stats[5], "Dex": stats[1], "Con": stats[3], "Int": stats[0], "Wis": stats[2], "Cha": stats[4]}
        elif u_class[0].lower() == "cleric":
            stats.sort()
            stat_types = {"Str": stats[3], "Dex": stats[2], "Con": stats[4], "Int": stats[1], "Wis": stats[5], "Cha": stats[0]}
        elif u_class[0].lower() == "monk":
            stats.sort()
            stat_types = {"Str": stats[4], "Dex": stats[2], "Con": stats[3], "Int": stats[1], "Wis": stats[5], "Cha": stats[0]}
        elif u_class[0].lower() == "ranger":
            stats.sort()
            stat_types = {"Str": stats[5], "Dex": stats[3], "Con": stats[4], "Int": stats[1], "Wis": stats[2], "Cha": stats[0]}
        elif u_class[0].lower() == "sorcerer":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[2], "Wis": stats[1], "Cha": stats[5]}
        elif u_class[0].lower() == "warlock":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[1], "Wis": stats[2], "Cha": stats[5]}
        elif u_class[0].lower() == "artificer":
            stats.sort()
            stat_types = {"Str": stats[0], "Dex": stats[3], "Con": stats[4], "Int": stats[5], "Wis": stats[2], "Cha": stats[1]}
        else:
            # Default stat assignment if no specific class is selected
            stat_types = {"Str": stats[0], "Dex": stats[1], "Con": stats[2], "Int": stats[3], "Wis": stats[4], "Cha": stats[5]}
    
    # Return the dictionary of final stat assignments
    return stat_types

# Function to handle stat increases based on user choice
def stat_increase(inc_amount = None):
    # If no input is provided for how to increase the stats, ask the user
    if inc_amount == None:
        inc_amount = int(input(""" How do you want to increase your stats?
(1) Increase 1 stat by 2 points
(2) Increase 2 stats by 1 point each
"""))
    
    # Case 1: Increase 1 stat by 2 points
    if inc_amount == 1:
        # Ask the user which stat they want to increase
        stat_to_inc = input("What stat do you want to increase? (Choose 1: Str, Dex, Con, Int, Wis, Cha) ")
        counter = [1]  # Loop counter, only runs once because we are only increasing one stat
        for x in counter:
            # Check the stat the user chose and increase it by 2 points
            if stat_to_inc.lower().strip() == "str":
                stat_types["Str"] += 2
            elif stat_to_inc.lower().strip() == "dex":
                stat_types["Dex"] += 2
            elif stat_to_inc.lower().strip() == "con":
                stat_types["Con"] += 2
            elif stat_to_inc.lower().strip() == "int":
                stat_types["Int"] += 2
            elif stat_to_inc.lower().strip() == "wis":
                stat_types["Wis"] += 2
            elif stat_to_inc.lower().strip() == "cha":
                stat_types["Cha"] += 2

    # Case 2: Increase 2 stats by 1 point each
    elif inc_amount == 2:
        # Ask the user which two stats they want to increase
        stats_to_inc = input("What stats do you want to increase? (Choose 2, separate by a comma: Str, Dex, Con, Int, Wis, Cha) ")
        inc_list = stats_to_inc.split(",")  # Split the input string into a list of stats to increase
        # If more than two stats are chosen, only take the first two
        if len(inc_list) > 2:
            incs = inc_list
            inc_list = [incs[0], incs[1]]
        
        # Increase each of the chosen stats by 1 point
        for stat in inc_list:
            if stat.lower().strip() == "str":
                stat_types["Str"] += 1
            elif stat.lower().strip() == "dex":
                stat_types["Dex"] += 1
            elif stat.lower().strip() == "con":
                stat_types["Con"] += 1
            elif stat.lower().strip() == "int":
                stat_types["Int"] += 1
            elif stat.lower().strip() == "wis":
                stat_types["Wis"] += 1
            elif stat.lower().strip() == "cha":
                stat_types["Cha"] += 1

    # Print the updated stat values after the increase
    print(stat_types)
    
    # Return the updated dictionary of stats
    return stat_types

# Function to set the character's level and apply stat increases based on the level
def set_level():
    global user_level  # Define user_level as a global variable
    
    # Ask the user to input their character's level
    user_level = int(input("What level is your character? (number) "))
    
    # Apply stat increases based on the user's character level
    # The higher the level, the more stat increases the character gets
    if user_level > 20:
        stat_increase(), stat_increase(), stat_increase(), stat_increase()
        for level in range(19, user_level+1, 4):
            stat_increase()
    if user_level >= 19:
        # If level is 19 or higher, apply five stat increases
        stat_increase(), stat_increase(), stat_increase(), stat_increase(), stat_increase()
    elif user_level >= 16:
        # If level is between 16 and 18, apply four stat increases
        stat_increase(), stat_increase(), stat_increase(), stat_increase()
    elif user_level >= 12:
        # If level is between 12 and 15, apply three stat increases
        stat_increase(), stat_increase(), stat_increase()
    elif user_level >= 8:
        # If level is between 8 and 11, apply two stat increases
        stat_increase(), stat_increase()
    elif user_level >= 4:
        # If level is between 4 and 7, apply one stat increase
        stat_increase()
    
    # Return the user's level to be used elsewhere in the program
    return user_level


# Function to set the character's race and apply race-specific stat bonuses
def set_race(race = None):
    global user_race  # Global variable to store the user's race
    global movement_speed  # Global variable for the character's movement speed
    global darkvision  # Global variable indicating whether the character has darkvision
    global languages  # Global list to store the languages known by the character
    
    # Ask the user for their character's race if not provided
    if race == None:
        user_race = input("What race is your character? (Dwarf, Half-orc, Elf, Halfling, Human, Dragonborn, Gnome, Half-elf, Tiefling, Aasimar, Changeling, Kenku, Warforged, Arachne, Shifter, Aarakocra, Kobold, Fire Genasi, Air Genasi, Earth Genasi, Water Genasi) ")
    else:
        user_race = race  # Use the provided race if passed as an argument

    # Apply race-specific stat bonuses, movement speed, darkvision, and languages
    # Each race has different attributes that get applied here
    if user_race.lower().strip() == "dwarf":
        stat_types["Con"] += 2  # Dwarfs gain +2 Constitution
        movement_speed = 25  # Dwarfs have a movement speed of 25
        darkvision = True  # Dwarfs have darkvision
        languages = ["Common", "Dwarvish"]  # Dwarfs speak Common and Dwarvish
    elif user_race.lower().strip() == "half-orc":
        stat_types["Str"] += 2  # Half-orcs gain +2 Strength
        stat_types["Con"] += 1  # Half-orcs gain +1 Constitution
        movement_speed = 30  # Half-orcs have a movement speed of 30
        darkvision = True  # Half-orcs have darkvision
        languages = ["Common", "Orc"]  # Half-orcs speak Common and Orc
    elif user_race.lower().strip() == "elf":
        stat_types["Dex"] += 2  # Elves gain +2 Dexterity
        movement_speed = 30  # Elves have a movement speed of 30
        darkvision = True  # Elves have darkvision
        languages = ["Common", "Elven"]  # Elves speak Common and Elven
    elif user_race.lower().strip() == "halfling":
        stat_types["Dex"] += 2  # Halflings gain +2 Dexterity
        movement_speed = 25  # Halflings have a movement speed of 25
        darkvision = False  # Halflings do not have darkvision
        languages = ["Common", "Halfling"]  # Halflings speak Common and Halfling
    elif user_race.lower().strip() == "human":
        # Humans gain +1 to all stats
        stat_types["Str"] += 1
        stat_types["Dex"] += 1
        stat_types["Con"] += 1
        stat_types["Int"] += 1
        stat_types["Wis"] += 1
        stat_types["Cha"] += 1
        movement_speed = 30  # Humans have a movement speed of 30
        darkvision = False  # Humans do not have darkvision
        languages = ["Common", input("Choose 1 language other than Common: ")]  # Humans speak Common and one other language
    elif user_race.lower().strip() == "dragonborn":
        stat_types["Str"] += 2  # Dragonborn gain +2 Strength
        stat_types["Cha"] += 1  # Dragonborn gain +1 Charisma
        movement_speed = 30  # Dragonborn have a movement speed of 30
        darkvision = False  # Dragonborn do not have darkvision
        languages = ["Common", "Draconic"]  # Dragonborn speak Common and Draconic
    elif user_race.lower().strip() == "gnome":
        stat_types["Int"] += 2  # Gnomes gain +2 Intelligence
        movement_speed = 25  # Gnomes have a movement speed of 25
        darkvision = True  # Gnomes have darkvision
        languages = ["Common", "Gnomish"]  # Gnomes speak Common and Gnomish
    elif user_race.lower().strip() == "half-elf":
        stat_types["Cha"] += 2  # Half-elves gain +2 Charisma
        stat_increase(2)  # Half-elves also get two stat increases
        movement_speed = 30  # Half-elves have a movement speed of 30
        darkvision = True  # Half-elves have darkvision
        languages = ["Common", "Elven", input("Choose 1 language other than Common and Elven: ")]  # Half-elves speak Common, Elven, and one other language
    elif user_race.lower().strip() == "tiefling":
        stat_types["Cha"] += 2  # Tieflings gain +2 Charisma
        movement_speed = 30  # Tieflings have a movement speed of 30
        darkvision = True  # Tieflings have darkvision
        languages = ["Common", "Infernal"]  # Tieflings speak Common and Infernal
    # Many additional races with specific attributes
    elif user_race.lower().strip() == "aasimar" or user_race.lower().strip() == "changeling" or user_race.lower().strip() == "kenku" or user_race.lower().strip() == "shifter" or user_race.lower().strip() == "aarakocra" or user_race.lower().strip() == "kobold" or user_race.lower().strip() == "fire genasi" or user_race.lower().strip() == "air genasi" or user_race.lower().strip() == "water genasi" or user_race.lower().strip() == "earth genasi":
        stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha): ")] += 1  # Choose 1 stat to increase by 1
        inc_2 = int(input("Would you like to increase one score by 2 points (1), or 2 scores by 1 point each (2)? "))  # Choose if one stat should increase by 2 or two stats by 1 each
        if inc_2 == 1:
            stat_increase(1)  # Apply 1 stat increase
        elif inc_2 == 2:
            stat_increase(2)  # Apply 2 stat increases
        if user_race.lower().strip() == "air genasi":
            movement_speed = 35  # Air Genasi move faster (35)
        else:
            movement_speed = 30  # Other races move at a normal speed (30)
        darkvision = True  # Most of these races have darkvision
        languages = ["Common", input("What language other than Common have you agreed on with your DM? ")]  # Ask for a DM-approved language
    elif user_race.lower().strip() == "warforged":
        stat_types["Con"] += 2  # Warforged gain +2 Constitution
        stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha): ")] += 1  # Warforged get to increase another stat by 1
        movement_speed = 30  # Warforged have a movement speed of 30
        darkvision = False  # Warforged do not have darkvision
        languages = ["Common", input("Choose 1 language other than Common: ")]  # Warforged speak Common and one other language
    elif user_race.lower().strip() == "arachne":
        stat_types["Dex"] += 2  # Arachne gain +2 Dexterity
        stat_types["Wis"] += 1  # Arachne gain +1 Wisdom
        movement_speed = 30  # Arachne have a movement speed of 30
        darkvision = True  # Arachne have darkvision
        languages = ["Common", "Undercommon"]  # Arachne speak Common and Undercommon
    elif user_race.lower().strip() == "starling" or user_race.lower().strip() == "bloodling" or user_race.lower().strip() == "core starling" or user_race.lower().strip() == "shadeling" or user_race.lower().strip() == "crystalling" or user_race.lower().strip() == "symbioling" or user_race.lower().strip() == "pure starling":
        current_race = user_race  # Store current race to handle complex starling-related logic
        if user_race.lower().strip() != "pure starling":
            prev_race = input("What race were you before? ")  # Get previous race if not pure starling
            set_race(prev_race)  # Call set_race to apply the previous race
            movement_speed += 10  # Increase movement speed for certain starlings
        else:
            set_race("human")  # If pure starling, reset to human race
            movement_speed += 15  # Increase movement speed for pure starling
        user_race = current_race  # Restore the current race
        stat_increase(2)  # Apply two stat increases
        darkvision = True  # Starling races have darkvision
        languages.append("Sangulect")  # Starling races speak Sangulect
    else:
        # Default case for any unrecognized races
        movement_speed = 30  # Default movement speed
        darkvision = False  # Default: no darkvision
        languages = ["Common"]  # Default language is Common
        
    # Output the character's stats for verification
    print(stat_types)

def calc_hit_points(level=1, u_class=None, con_modifier=1):
    global hp_max
    hp_max = 0  # Initialize the max HP variable
    # Check if the user's class is a list (multiclass character)
    if isinstance(u_class, list): 
        for var in u_class:  # Iterate through each class in the list
            # If class is None or empty, assume default hit dice (d8)
            if var == None or var == "":
                hp_max += 8 + con_modifier  # Base HP for level 1
                for num in range(level - 1):  # Roll hit dice for remaining levels
                    hp_max += con_modifier  # Add Constitution modifier
                    roll_no_output("d8")  # Roll a d8 hit die
                    hp_max += rolls[len(rolls)-1]  # Add the rolled result
            else:
                # Check if the class belongs to the d8 hit dice group
                if var.lower().strip() in ["artificer", "bard", "druid", "cleric", "monk", "rogue", "warlock"]:
                    hp_max += 8 + con_modifier  # Base HP for level 1
                    if level != 1:
                        for num in range((level - 1) // len(u_class)):  # Roll hit dice for remaining levels
                            hp_max += con_modifier
                            roll_no_output("d8")  # Roll a d8
                            hp_max += rolls[len(rolls)-1]
                
                # Check if the class belongs to the d10 hit dice group
                elif var.lower().strip() in ["fighter", "paladin", "ranger"]:
                    hp_max += 10 + con_modifier  # Base HP for level 1
                    if level != 1:
                        for num in range((level - 1) // len(u_class)):
                            hp_max += con_modifier
                            roll_no_output("d10")  # Roll a d10
                            hp_max += rolls[len(rolls)-1]

                # Check if the class belongs to the d6 hit dice group
                elif var.lower().strip() in ["sorcerer", "wizard"]:
                    hp_max += 6 + con_modifier  # Base HP for level 1
                    if level != 1:
                        for num in range((level - 1) // len(u_class)):
                            hp_max += con_modifier
                            roll_no_output("d6")  # Roll a d6
                            hp_max += rolls[len(rolls)-1]

                # Check if the class is a Barbarian (d12 hit dice)
                elif var.lower().strip() == "barbarian":
                    hp_max += 12 + con_modifier  # Base HP for level 1
                    if level != 1:
                        for num in range((level - 1) // len(u_class)):
                            hp_max += con_modifier
                            roll_no_output("d12")  # Roll a d12
                            hp_max += rolls[len(rolls)-1]

                # Default case (unknown class), assume d8 hit dice
                else:
                    hp_max += 12 + con_modifier
                    if level != 1:
                        for num in range((level - 1) // len(u_class)):
                            hp_max += con_modifier
                            roll_no_output("d8")  # Roll a d8
                            hp_max += rolls[len(rolls)-1]

    # If the class is None or an empty string (assume default d8 hit dice)
    elif u_class == None or u_class == "":
        hp_max += 8 + con_modifier  # Base HP for level 1
        for num in range(level - 1):
            hp_max += con_modifier
            roll_no_output("d8")  # Roll a d8
            hp_max += rolls[len(rolls)-1]

    return hp_max  # Return the final calculated max HP

# Initialize dictionary to assign proficiency bonus
proficiency = {1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5}
            
while True:
    rolls = []  # Initialize a list to store the rolls
    start = input("Start? (y/n) ").lower().strip()  # Ask the user to start the character creation process
    if start == "y":
        username = os.getlogin()  # Get the current user's login name
        save = input("Would you like to save your character to a text file? (y/n) ")  # Ask if the user wants to save the character
        if save.lower().strip() == "y":
            save_type = input("Would you like to overwrite a file that was already made (or make a new file) (1), or add to a file that was already made (2)? ").lower().strip()  # Ask how the user wants to save the file
        char_name = input("What is your character's name? ").strip()  # Get the character's name
        if char_name.lower() != "andrew" and char_name.lower() != "luca" and char_name.lower() != "kai" and char_name.lower() != "z" and char_name.lower() != "zurulien":
            user_class = input("What class do you choose? (Barbarian, Fighter, Wizard, Rogue, Bard, Druid, Paladin, Cleric, Monk, Ranger, Sorcerer, Warlock, Artificer. If you choose multiple, it will automatically distribute your levels evenly between them. Separate with a space. Put priority class first.) ").strip().split(" ")  # Get the character's class
        else:
            user_class = ""  # Special case for certain character names, no class assigned
        roll_stats = 4  # Number of dice to roll for stats (could be defined elsewhere)
        stat_roll(user_class)  # Call the function to roll stats based on the class
        print(stat_types)  # Print the rolled stats
        if char_name.lower().strip() == "z" or char_name.lower().strip() == "zurulien":
            set_race("Pure Starling")  # Assign the race "Pure Starling" for specific names
            user_class = ["Barbarian", "Wizard"]
            user_race = "Eye of Mind"
        else:
            set_race()  # Set race for other characters
        set_level()  # Set the character's level

        mod_str = (stat_types["Str"] - 10) // 2
        mod_dex = (stat_types["Dex"] - 10) // 2
        mod_con = (stat_types["Con"] - 10) // 2
        mod_int = (stat_types["Int"] - 10) // 2
        mod_wis = (stat_types["Wis"] - 10) // 2
        mod_cha = (stat_types["Cha"] - 10) // 2
        
        calc_hit_points(user_level, user_class, mod_con)
        if user_level >= 17:
            proficiency_bonus = 6
        else:
            proficiency_bonus = proficiency[user_level]
        alignment = input("What is your alignment? (Chaotic Good, Neutral Good, Lawful Good, Lawful Neutral, True Neutral, Chaotic Neutral, Lawful Evil, Neutral Evil, Chaotic Evil) ")  # Get the character's alignment

    else:
        break  # Exit the program if the user doesn't want to start
    if save.lower().strip() == "n":
        if char_name.lower() == "andrew" or char_name.lower() == "luca" or char_name.lower() == "kai" or char_name.lower() == "z" or char_name.lower() == "zurulien":
            # If character name matches predefined names, print their stats in a specific format
            print(f"""You are {char_name}!
Your level is {user_level}!
Your Hit Point Maximum is {hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {stat_types["Str"]} ({mod_str})
Dexterity: {stat_types["Dex"]} ({mod_dex})
Constitution: {stat_types["Con"]} ({mod_con})
Intelligence: {stat_types["Int"]} ({mod_int})
Wisdom: {stat_types["Wis"]} ({mod_wis})
Charisma: {stat_types["Cha"]} ({mod_cha})
""")
    
        elif user_class[0].lower() == "artificer":
            # Special case for Artificer class, print their stats
            print(f"""You are an {user_class}!
Your level is {user_level}!
Your Hit Point Maximum is {hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {stat_types["Str"]} ({mod_str})
Dexterity: {stat_types["Dex"]} ({mod_dex})
Constitution: {stat_types["Con"]} ({mod_con})
Intelligence: {stat_types["Int"]} ({mod_int})
Wisdom: {stat_types["Wis"]} ({mod_wis})
Charisma: {stat_types["Cha"]} ({mod_cha})
""")
    
        elif user_class == None or user_class == "" or user_class[0].lower() != 'barbarian' and user_class[0].lower() != 'fighter' and user_class[0].lower() != 'wizard' and user_class[0].lower() != 'rogue' and user_class[0].lower() != 'bard' and user_class[0].lower() != 'druid' and user_class[0].lower() != 'paladin' and user_class[0].lower() != 'cleric' and user_class[0].lower() != 'monk' and user_class[0].lower() != 'ranger' and user_class[0].lower() != 'sorcerer' and user_class[0].lower() != 'warlock' and user_class[0].lower() != 'artificer':
            # Print stats for a non-specific class (or undefined class)
            print(f"""Your level is {user_level}!
Your Hit Point Maximum is {hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {stat_types["Str"]} ({mod_str})
Dexterity: {stat_types["Dex"]} ({mod_dex})
Constitution: {stat_types["Con"]} ({mod_con})
Intelligence: {stat_types["Int"]} ({mod_int})
Wisdom: {stat_types["Wis"]} ({mod_wis})
Charisma: {stat_types["Cha"]} ({mod_cha})
""")
    
        else:
            # General case for valid classes, print their stats
            print(f"""You are a {user_class}!
Your level is {user_level}!
Your Hit Point Maximum is {hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {stat_types["Str"]} ({mod_str})
Dexterity: {stat_types["Dex"]} ({mod_dex})
Constitution: {stat_types["Con"]} ({mod_con})
Intelligence: {stat_types["Int"]} ({mod_int})
Wisdom: {stat_types["Wis"]} ({mod_wis})
Charisma: {stat_types["Cha"]} ({mod_cha})
""")
        print(f"Your alignment is {alignment}!")  # Output the character's alignment

        # Print the race and movement speed information
        if user_race.lower().strip() == "aasimar" or user_race.lower().strip() == "air genasi" or user_race.lower().strip() == "arachne" or user_race.lower().strip() == "aarakocra" or user_race.lower().strip() == "earth genasi" or user_race.lower().strip() == "elf":
            print(f"You are an {user_race}!")  # Special case for certain races
        else:
            print(f"You are a {user_race}!")  # General case for other races
        print(f"Your movement speed is {movement_speed}!")  # Output the character's movement speed

        # Check if the character has darkvision and print the information
        if darkvision == True:
            print("You have darkvision!")
        print(f"You know these languages:")  # Print the languages the character knows
        for x in languages:
            print("-", x)

    elif save.lower().strip() == "y":

        # Initialize dividers
        divider1 = "\n✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏\n"
        divider2 = "\n•───────•°•❀•°•───────•\n"
        divider3 = "\n︵‿︵‿୨♡୧‿︵‿︵\n"
        divider4 = "\n✿　.　˚　. 　 ˚　✿.\n"
        divider5 = "\n⊹˚₊‧───────────────‧₊˚⊹\n"
        divider6 = "\n⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆\n"
        divider7 = "\n➽───────────────❥\n"
        divider8 = "\n· • —– ٠ ✤ ٠ —– • ·\n"
        divider9 = "\n⋅•⋅⋅•⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅∙∘☽༓☾∘∙•⋅⋅⋅•⋅⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅\n"
        divider10 = "\n•─────⋅☾ ☽⋅─────•\n"

        # Ask user what divider they want to use, if any.
        divider_choice = input("""What divider would you like to use?
(1) ✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏
(2) •───────•°•❀•°•───────•
(3) ︵‿︵‿୨♡୧‿︵‿︵
(4) ✿　.　˚　. 　 ˚　✿.
(5) ⊹˚₊‧───────────────‧₊˚⊹
(6) ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆
(7) ➽───────────────❥
(8) · • —– ٠ ✤ ٠ —– • ·
(9) ⋅•⋅⋅•⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅∙∘☽༓☾∘∙•⋅⋅⋅•⋅⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅
(10) •─────⋅☾ ☽⋅─────•
(0) None
""") 
        
        # Define the absolute path where the character sheet will be saved
        folder_path = f"C:\\Users\\{username}\\Documents\\character_sheets"  # Path where the file will be stored

        # Check if the folder exists, if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = f"{char_name}_character_sheet.txt"  # Define the filename
        full_path = os.path.join(folder_path, file_name)  # Create the full file path

        if save_type == "1":
            # If save_type is 1, overwrite the existing file or create a new one
            with open(full_path, "w+", encoding="utf-8") as file:
                file.write(f"""
Name: {char_name}
Class: {user_class}
Race: {user_race}
Level: {user_level}
Alignment: {alignment}

Initiative Bonus: {mod_dex}

Hit Point Maximum: {hp_max}

Stats:
Strength: {stat_types["Str"]} ({mod_str})
Dexterity: {stat_types["Dex"]} ({mod_dex})
Constitution: {stat_types["Con"]} ({mod_con})
Intelligence: {stat_types["Int"]} ({mod_int})
Wisdom: {stat_types["Wis"]} ({mod_wis})
Charisma: {stat_types["Cha"]} ({mod_cha})

Proficiency Bonus: {proficiency_bonus}

Movement Speed: {movement_speed}\n""")

                # If the character has darkvision, write it to the file
                if darkvision == True:
                    file.write("""Darkvision\n""")
    
                file.write("\nLanguages:\n")  # Write the languages known by the character
                for x in languages:
                    file.write(f"- {x}\n")

                if divider_choice.strip() == "0": #if user inputted '0', no divider.
                    None
                else:
                    file.write(eval(f"divider{divider_choice}")) #write user-chosen divider to file and divider to separate
                    
                # Display a success message to the user using tkinter
                root = tk.Tk()
                root.withdraw()  # Hide the tkinter root window
                root.attributes('-topmost', True)  # Make the messagebox topmost
                messagebox.showinfo("Success", f"Character sheet saved to {char_name}_character_sheet.txt!")  # Show the success message
                root.attributes('-topmost', False)  # Reset the topmost attribute
                root.destroy()  # Destroy the tkinter window
                file.seek(0)  # Move the file pointer to the beginning before reading
                print(file.read())  # Read and print the file contents
                print(f'Absolute path to the file: {full_path}')  # Print the file's absolute path
                file.close()

        if save_type == "2":
            # If save_type is 2, append to an existing file
            with open(full_path, "a+", encoding="utf-8") as file:
                file.write(f"""
Name: {char_name}
Class: {user_class}
Race: {user_race}
Level: {user_level}
Alignment: {alignment}

Initiative Bonus: {mod_dex}

Hit Point Maximum: {hp_max}

Stats:
Strength: {stat_types["Str"]} ({mod_str})
Dexterity: {stat_types["Dex"]} ({mod_dex})
Constitution: {stat_types["Con"]} ({mod_con})
Intelligence: {stat_types["Int"]} ({mod_int})
Wisdom: {stat_types["Wis"]} ({mod_wis})
Charisma: {stat_types["Cha"]} ({mod_cha})

Proficiency Bonus: {proficiency_bonus}

Movement Speed: {movement_speed}\n""")

                if darkvision == True:
                    file.write("""Darkvision\n""")
    
                file.write("\nLanguages:\n")  # Write the languages known by the character
                for x in languages:
                    file.write(f"- {x}\n")

                if divider_choice.strip() == "0": # If user inputted '0', no divider.
                    None
                else:
                    file.write(eval(f"divider{divider_choice}")) # Write user-chosen divider to file and divider to separate

                # Display a success message to the user using tkinter
                root = tk.Tk()
                root.withdraw()  # Hide the tkinter root window
                root.attributes('-topmost', True)  # Make the messagebox topmost
                messagebox.showinfo("Success", f"Character sheet saved to {char_name}_character_sheet.txt!")  # Show the success message
                root.attributes('-topmost', False)  # Reset the topmost attribute
                root.destroy()  # Destroy the tkinter window
                file.seek(0)  # Move the file pointer to the beginning before reading
                print(file.read())  # Read and print the file contents
                print(f'Absolute path to the file: {full_path}')  # Print the file's absolute path
                file.close()

'''
Features to be added!

TBA races:
    Goliath

    Homebrew:
        -Core Starling
        -Starling
        -Shadeling
        -Crystalling
        -Bloodling
        -Pure Starling
        -Symbioling
        Silenced
        Starved


TBA features (numbers = priority/difficulty estimate):
    Spells (3)
    Skills (1)
    AC (2)
'''
