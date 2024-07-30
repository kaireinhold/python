userNoun1 = input("Choose a noun! ")
print("You chose the noun " + userNoun1 + "!")
change = input("Would you like to change that word? ")
if change == "Y" or change == "Yes" or change == "yes" or change == "y":
    userNoun1 = input("Choose a noun! ")
    print("You changed the noun to " + userNoun1 + "!")
    
userNounPlural = input("Choose a plural noun! ")
print("You chose the plural noun " + userNounPlural + "!")
change = input("Would you like to change that word? ")
if change == "Y" or change == "Yes" or change == "yes" or change == "y":
    userNounPlural = input("Choose a plural noun! ")
    print("You changed the plural noun to " + userNounPlural + "!")

userNoun2 = input("Choose a noun! ")
print("You chose the noun " + userNoun2 + "!")
change = input("Would you like to change that word? ")
if change == "Y" or change == "Yes" or change == "yes" or change == "y":
    userNoun2 = input("Choose a noun! ")
    print("You changed the noun to " + userNoun2 + "!")

userPlace = input("Choose a place! ")
print("You chose the place " + userPlace + "!")
change = input("Would you like to change that word? ")
if change == "Y" or change == "Yes" or change == "yes" or change == "y":
    userPlace = input("Choose a place! ")
    print("You changed the place to " + userPlace + "!")

userAdj = input("Choose an adjective! ")
print("You chose the adjective " + userAdj + "!")
change = input("Would you like to change that word? ")
if change == "Y" or change == "Yes" or change == "yes" or change == "y":
    userAdj = input("Choose an adjective! ")
    print("You chose the adjective " + userAdj + "!")

print("Did you know I have a pet " + userNoun1 + "?")
print("It likes to run around and play with all of the " + userNounPlural + "!")
print("One morning, I woke up and he was wearing a " + userNoun2 + " for a hat!")
print("I especially like to take him to the " + userPlace + ",")
print("Because he shows off his " + userAdj + " side!")

print(" ")
print("Thank you for playing!")
leave = input("Would you like to exit? ")
if change == "Y" or change == "Yes" or change == "yes" or change == "y":
    exit()
