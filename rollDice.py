#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time

class Dice:
    def __init__(self):
        self.rolls = []  # Instance-level roll list

    def roll(self, di=None):
        """
        Simulate rolling dice with a specified number of sides and display the result.
    
        Input:
        - d<number> (str): A string where <number> represents the number of sides on the dice to roll, chosen by the user (e.g., 'd20' for a 20-sided die).
    
        Output:
        - str: A message indicating "Rolling d<number>..." followed by a wait of 1.5 seconds, and then another message displaying the rolled value (e.g., "d<number>: You rolled a <rolled value>!").
    
        Behavior:
        - Prompts the user to input a dice to roll (ie. 'd20' for a 20-sided dice.)
        - Rolls the specified dice and prints the result.
        - Waits for 1 seconds before displaying the result.
        - Detects if the rolled number should be preceded by 'an' (for example, 8 or 18) and adjusts the output message accordingly.
        - Appends the roll output for each roll to the list named 'rolls'

        Raises:
        - ValueError: If the input does not include the 'd' prefix, indicating the dice format.
        
        """
        
        if di is None:
            dice_chosen = input("What dice would you like to roll? (d[number]) ")
        else:
            dice_chosen = di

        dice_list = dice_chosen.lower().split()
        self.rolls = []  # Reset rolls list before each roll
        an_list = [11, 18]
        processed_dice = []
    
        for dice in dice_list:
            if "d" not in dice:
                raise ValueError("Value must have a 'd' in front to specify that it is a dice")
            parts = dice.split("d")
            if parts[0] == "":  
                num_rolls = 1
            else:
                num_rolls = int(parts[0])
            try:
                die_type = int(parts[1])
            except ValueError:
                raise ValueError(f"Invalid dice type in '{dice}'.")
            for _ in range(num_rolls):
                processed_dice.append(die_type)
                
        for die in processed_dice:
            print(f"Rolling d{die}...")
            time.sleep(1)
            roll_output = random.randint(1, die)
            output_str = str(roll_output)
            if roll_output in an_list or output_str.startswith("8"):
                print(f"d{die}: You rolled an {output_str}!")
            else:
                print(f"d{die}: You rolled a {output_str}!")

            time.sleep(0.5)
            self.rolls.append(roll_output)  # Add roll to instance list

        return self.rolls  # Return the rolls for the current instance
    
    def roll_no_output(self, di=None):
        """
        Simulate rolling dice with a specified number of sides and display the result.
    
        Input:
        - d<number> (str): A string where <number> represents the number of sides on the dice to roll, chosen by the user (e.g., 'd20' for a 20-sided die).
    
        Output:
        - None.
    
        Behavior:
        - Prompts the user to input a dice to roll (ie. 'd20' for a 20-sided dice.)
        - Rolls the specified dice and prints the result.
        - Appends the roll output for each roll to the list named 'rolls'

        Raises:
        - ValueError: If the input does not include the 'd' prefix, indicating the dice format.
        
        """
        
        if di is None:
            dice_chosen = input("What dice would you like to roll? (d[number]) ")
        else:
            dice_chosen = di

        dice_list = dice_chosen.lower().split()
        self.rolls = []  # Reset rolls list before each roll
        processed_dice = []
    
        for dice in dice_list:
            if "d" not in dice:
                raise ValueError("Value must have a 'd' in front to specify that it is a dice")
            parts = dice.split("d")
            if parts[0] == "":  
                num_rolls = 1
            else:
                num_rolls = int(parts[0])
            try:
                die_type = int(parts[1])
            except ValueError:
                raise ValueError(f"Invalid dice type in '{dice}'.")
            for _ in range(num_rolls):
                processed_dice.append(die_type)
                
        for die in processed_dice:
            roll_output = random.randint(1, die)
            self.rolls.append(roll_output)  # Add roll to instance list

        return self.rolls  # Return the rolls for the current instance
