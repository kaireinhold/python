import random
import time
import rollDice

def new_Character():
    name = input("What would you like to call this character? ")
    dict_Name = name.replace(" ", "_")
    print("Opening " + dict_Name + "...")
    dict_Name = {
        "Name": name,
        "Class": input("What is their class? "),
        "Race": input("What is their race? "),
        "Level": input("What is their level? "),
        }
    print(dict_Name["Name"] + ", " + dict_Name["Race"] + ", " + dict_Name["Class"] + ", " + dict_Name["Level"])
