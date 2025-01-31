"""
                            NAME: KODINGNEXT
                            DATE: 6/7/2018
                            PROJECT NAME: Simple Dice Game
"""

import random

dice = random.randrange(1,7)
confirm = "yes"

print("Welcome to the dice game!")
print("In this program we will choose a random number between 1 to 6 for you!")
print("Let's start!")

while confirm != "no":
    print (dice)
    confirm = input("Again? Press enter to continue, Type no if you would like to stop.")

    if confirm == "no":
        print("Thanks for playing!")
        confirm = "no"
    dice = random.randrange(1,7)
    
            
    

