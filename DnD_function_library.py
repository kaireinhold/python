#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time

class Functions:
    def __init__(self):
        self.rolls = []
        self.stats = []
        self.stat_types = {}
        self.for_stats = 0
        self.roll_stats = 5
        self.user_race = ""
        self.movement_speed = 30
        self.darkvision = False
        self.languages = []

    def roll(self, di=None):
        """
        Simulate rolling dice with a specified number of sides and display the result.
        """
        if di is None:
            dice_chosen = input("What dice would you like to roll? (d[number] ")
        else:
            dice_chosen = di
        dice_list = dice_chosen.lower().split()
        an_list = [11, 18]
        for x in dice_list:
            if "d" not in x:
                raise ValueError("Value must have a 'd' in front to specify that it is a dice")
        
            print("Rolling "  + x + "...")
            time.sleep(1.5)
            roll_num = int(x[1:])
            roll_output = random.randint(1, roll_num)
            output_str = str(roll_output)
            if roll_output in an_list or str(output_str[0]) == "8":
                print(x + ": You rolled an", output_str + "!")
            else:
                print(x + ": You rolled a", output_str + "!")
            time.sleep(1)
            self.rolls.append(roll_output)
    
    def roll_no_output(self, di=None):
        """
        Simulate rolling dice with a specified number of sides but no output.
        """
        if di is None:
            dice_chosen = input("What dice would you like to roll? (d[number] ")
        else:
            dice_chosen = di
        dice_list = dice_chosen.lower().split()
        an_list = [11, 18]
        for x in dice_list:
            if "d" not in x:
                raise ValueError("Value must have a 'd' in front to specify that it is a dice")
        
            roll_num = int(x[1:])
            roll_output = random.randint(1, roll_num)
            self.rolls.append(roll_output)

    def stat_roll(self, u_class=None):
        while self.for_stats < 6:
            while self.roll_stats > 0:
                self.roll_stats -= 1
                self.roll_no_output("d6")
                if self.rolls[-1] == 1:
                    self.rolls.pop()
                    self.roll_stats += 1
                elif len(self.rolls) == 4:
                    self.rolls.remove(min(self.rolls))
                    self.stats.append(sum(self.rolls))
                    self.rolls = []
                    self.for_stats += 1
                    if self.for_stats >= 6:
                        break
                    self.roll_stats = 5
        if u_class is None or u_class == "":
            self.stat_types = {
                "Str": self.stats[0],
                "Dex": self.stats[1],
                "Con": self.stats[2],
                "Int": self.stats[3],
                "Wis": self.stats[4],
                "Cha": self.stats[5]
            }
        else:
            # (Your class-specific logic here)
            pass
        print(self.stat_types)
        return self.stat_types
    
    def stat_increase(self, inc_amount=None):
        if inc_amount is None:
            inc_amount = int(input(""" How do you want to increase your stats?
    (1) Increase 1 stat by 2 points
    (2) Increase 2 stats by 1 point each
    """))
        if inc_amount == 1:
            stat_to_inc = input("What stat do you want to increase? (Choose 1: Str, Dex, Con, Int, Wis, Cha) ")
            if stat_to_inc.lower().strip() == "str":
                if self.stat_types["Str"] < 20:
                    self.stat_types["Str"] += 2
            # (repeat for other stats)
        elif inc_amount == 2:
            stats_to_inc = input("What stats do you want to increase? (Choose 2, separate by a comma: Str, Dex, Con, Int, Wis, Cha) ")
            # (repeat for other stats)
        print(self.stat_types)
        return self.stat_types
    
    def set_level(self, u_level=None):
        if u_level is None:
            u_level = int(input("What level is your character? (number) "))
        user_level = u_level
        if u_level >= 19:
            for _ in range(5):
                self.stat_increase()
        elif u_level >= 16:
            for _ in range(4):
                self.stat_increase()
        # (repeat for other levels)
        return user_level
    
    def set_race(self, race=None):
        if race is None:
            self.user_race = input("What race is your character? (Dwarf, Half-orc, Elf, Halfling, Human, Dragonborn, Gnome, Half-elf, Tiefling, Aasimar, Changeling, Kenku, Warforged, Arachne, Shifter, Aarakocra, Kobold, Fire Genasi, Air Genasi, Earth Genasi, Water Genasi) ")
        else:
            self.user_race = race    
        if self.user_race.lower().strip() == "dwarf":
            self.stat_types["Con"] += 2
            self.movement_speed = 25
            self.darkvision = True
            self.languages = ["Common", "Dwarvish"]
        # (repeat for other races)
        return self.user_race, self.movement_speed, self.darkvision, self.languages, self.stat_types
