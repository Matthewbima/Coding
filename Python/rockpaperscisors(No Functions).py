"""
                            NAME: KODINGNEXT
                            DATE: 6/7/2018
                            PROJECT NAME: Rock, Paper, Scissors
"""

#Imports
import random

#Variable Declarations
possibleAnswers = ["Rock", "Paper", "Scissors"]
enemySelection = ""
playerSelection = ""
end = False
AnswerCheck = False

#Opening
print("Welcome to rock, paper, and scissors!")
print("For today's match, you will be facing an AI opponent. ")
print("Good luck player! and In anycase, let's start the match!\n")
    
#Main Game Loop
while end != True:
    AnswerCheck = False
    print("ROCK, PAPER, SCISSORS, SHOOT.\n")
    answer = int(input("(please input your answer. 0 = Rock, 1 = Paper, 2 = Scissors.)\n"))
    enemySelection = random.choice(possibleAnswers)

    while AnswerCheck != True:
       
        if answer == 0 or answer == 1 or answer == 2:
            AnswerCheck = True
            playerSelection = possibleAnswers[answer]
            if playerSelection == "Rock" and enemySelection == "Scissors" or playerSelection == "Paper" and enemySelection == "Rock" or playerSelection == "Scissors" and enemySelection == "Paper":
                print("your enemy played, " + enemySelection)
                print("You WIN! Congratulations!")
                end = True
            elif playerSelection == enemySelection:
                print("your enemy played " + enemySelection + " as well, and so..")
                print("It's a draw folks!. Let's try that again!\n ")
            else:
                print("your enemy played, " + enemySelection)   
                print("you LOSE! Better luck next time!")
                end = True
        else:
            answer = int(input("Your input is invalid, please try again\n"))
           
        
    
    

            
        
    
   

    
    
            
    

