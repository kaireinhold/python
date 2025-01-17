#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time

class dice:
    global rolls
    rolls = []
    def __init__(self):
        self.rolls = []

    def roll(di=None):
        """
        Simulate rolling dice with a specified number of sides and display the result.
    
        Input:
        - d<number> (str): A string where <number> represents the number of sides on the dice to roll, chosen by the user (e.g., 'd20' for a 20-sided die).
    
        Output:
        - str: A message indicating "Rolling d<number>..." followed by a wait of 1.5 seconds, and then another message displaying the rolled value (e.g., "d<number>: You rolled a <rolled value>!").
    
        Behavior:
        - Prompts the user to input a dice to roll (ie. 'd20' for a 20-sided dice.)
        - Rolls the specified dice and prints the result.
        - Waits for 1.5 seconds before displaying the result.
        - Detects if the rolled number should be preceded by 'an' (for example, 8 or 18) and adjusts the output message accordingly.

        Raises:
        - ValueError: If the input does not include the 'd' prefix, indicating the dice format.
        
        """

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
            time.sleep(1.5)
            roll_num = int(x[1:len(x)])
            roll_output = random.randint(1,roll_num)
            output_str = str(roll_output)
            if roll_output in an_list or str(output_str[0]) == "8":
                print(x + ": You rolled an", output_str + "!")
            else:
                print(x + ": You rolled a", output_str + "!")
            time.sleep(1)
            rolls.append(roll_output)

    def roll_no_output(di=None):
        """
        To Be Completed
        """
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
