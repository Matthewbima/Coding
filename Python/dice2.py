"""
                            NAME: KODINGNEXT
                            DATE: 6/7/2018
                            PROJECT NAME: More Complex Dice Game
"""

#Imports    
import random

#Variable Declarations
dice = random.randrange(1,7)
finish = "False"
stepcounter = 0
tile = 0
highscore = 30

#Opening
print("Welcome to how long will it take!")
print("Test your luck and see how long it'll take you to land at the finish line!")
print("The finish line will be on tile 20. Currently the highscore is finishing in "+str(highscore)+" steps")

#Main Game Loop
while finish != "True":

    #Dice Roll & Progress Tracking
    input("Please press enter to roll the dice!")
    dice = random.randrange(1,7)
    print (dice)
    stepcounter = stepcounter + 1
    tile = tile + dice

    #Initial Conditional Statement (Checks if the player have passed the finish line)
    if tile <= 20:
        print("Keep going! you're doing great! currently you're on tile number "+ str(tile))
    else:
        print("Congrats player! you have reached the finish line.")
        print("You have reached the finish line in "+str(stepcounter)+" amount of steps.")

        #Follow Up Conditional Statement (Checks if the user was able to reach a new high score)
        if stepcounter < highscore:
            print("Nice! That's a new highscore!")
            highscore = stepcounter
            #finish = "True"
        else:
            print("Thanks for playing player! you didn't reach the highscore.. but i'm sure you can do it next time!")
            #finish = "True"

        #Last Conditional Statement (Checks if the player would like to play again. If they do, the program will reset the step counter and tile counter)   
        answer = input("Would you like to play again? please answer with yes & no")
        if answer == "yes":
            stepcounter = 0
            tile = 0
            print("Good luck friend!")
        elif answer == "no":
            print("Thanks for playing!")
            finish = "True"
        else:
            print("You couldn't simply follow the instructions now can you? In anycase, I'll take that as a no.")
            print("Thanks for playing!")
            finish = "True"
            
        
    
   

    
    
            
    

