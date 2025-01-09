import random
import time
import rollDice

def new_Character():
    #open(w,"Characters.sql
    name = input("What would you like to call this character? ").strip()
    dict_Name = name.replace(" ", "_")
    print("Opening " + dict_Name + "...")
    dict_Name = {
        "Name": name,
        "Class": input("What is their class? ").strip(),
        "Race": input("What is their race? ").strip(),
        "Level": input("What is their level? ").strip(),
        }
    print(dict_Name)
    return dict_Name
def edit_Character():
    edit_Q = input("What character would you like to edit? (replace spaces with _) ").lower().strip()
    
    edit_Item = input("""What would you like to edit?
 (N)ame
 (C)lass
 (R)ace
 (L)evel
 (E)xit
 """).lower().strip()
