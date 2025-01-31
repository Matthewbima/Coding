import random
from logo import logo

dice = random.randrange(1,7)
finish = False
stepcounter = 0
tile = 0
highscore = 30

print(logo)
print("Welcome to Snakes and Ladders!")
print("Climb to the top of the tower to win, get there as fast as you can!")
print("The tower has 50 floors. The current highscore is "+str(highscore)+" roll")


while not finish:


    input("Press ENTER to roll the dice!")
    dice = random.randrange(1,7)
    print (f'You roll a {dice}')
    stepcounter = stepcounter + 1
    tile = tile + dice


    if tile > 50:
        print("Congrats player! you have reached the top!")
        print("You have reached the finish line in only "+str(stepcounter)+" roll.")

        if stepcounter < highscore:
            print("Nice! That's a new highscore!")
            highscore = stepcounter

        else:
            print("Thanks for playing player! you didn't reach the highscore.. but i'm sure you can do it next time!")

        answer = input("Would you like to play again? (y/n))").lower()
        if answer == "y":
            stepcounter = 0
            tile = 0
            print("Here we go again!")
        elif answer == "n":
            print("Thanks for playing! Goodbye!")
            finish = True
        else:
            print("You couldn't simply follow the instructions now can you? In any case, I'll take that as a no.")
            print("Thanks for playing!")
            finish = True

    else:
        print("Keep going! you're doing great! currently you're on floor "+ str(tile)+". You have "+ str(51 - tile) +" floor(s) to go")
        if tile % 7 == 0 and tile + 9 <= 50:
            tile = tile + 9
            print("You have reached a special floor, you found a trampoline and it makes you jump 9 floor forward. You're now at floor " + str(tile) + ".")
        elif tile % 6 == 0 and tile % 7 != 0:
            tile = tile - 3
            print("You have reached a special floor, but it has a crack on the ground and makes you drop 3 floors down. You're now at floor " + str(tile) + ".")
        elif tile % 5 == 0 and tile % 7 != 0 and tile % 6 != 0 and tile + 5 <=50:

            print(f"You've entered a special room! This is the head tail room! "
                  f"If you got it right, go forward 5 tiles, if wrong go back 5 tiles!")

            coinBreak = False
            while not coinBreak:
                coinGuess = input("What's it gonna be? Head or Tail?").lower()
                coin = random.randrange(1, 3)
                def cts(cn):
                    if cn == 1:
                        return "Head"
                    else:
                        return "Tail"
                print(f'The coin flips! and it lands on {cts(coin)}')
                if coinGuess == "head":
                    coinGuess = 1
                    coinBreak = True
                elif coinGuess == "tail":
                    coinGuess = 2
                    coinBreak = True
                else:
                    print("Sorry, that's not a valid option!")

            if coinGuess == coin:
                print("You got it right!!")

                tile = tile + 5
            else:
                print("You're WRONG!")

                tile = tile - 5
            print("You're now at floor " + str(tile) + ".")

        elif tile % 4 == 0 and tile % 5 != 0 and tile % 6 != 0 and tile % 7 != 0:
            possibleAnswers = ["Rock", "Paper", "Scissors"]
            enemySelection = ""
            playerSelection = ""
            end = False
            AnswerCheck = False

            # Opening
            print("Welcome to rock, paper, and scissors! Floor")
            print("For today's match, you will be facing an AI opponent. ")
            print("A win boost you 5 floors !\n")


            # Result Checker
            def winOrLose(enemySelection, playerSelection):
                if playerSelection == "Rock" and enemySelection == "Scissors" or playerSelection == "Paper" and enemySelection == "Rock" or playerSelection == "Scissors" and enemySelection == "Paper":
                    return "win"

                elif playerSelection == enemySelection:
                    return "tie"

                else:
                    return "lose"


            while end != True:
                AnswerCheck = False
                print("ROCK, PAPER, SCISSORS, SHOOT.\n")
                answer = input("(please input your answer. 0 = Rock, 1 = Paper, 2 = Scissors.)\n")
                enemySelection = random.choice(possibleAnswers)

                while AnswerCheck != True:
                    if not answer.isdigit():
                        answer = input("Your input is invalid, please try again\n")
                    else:
                        answer = int(answer)
                        if answer == 0 or answer == 1 or answer == 2:
                            AnswerCheck = True
                            playerSelection = possibleAnswers[answer]
                            results = winOrLose(enemySelection, playerSelection)
                            if results == "win":
                                print("your enemy played, " + enemySelection)
                                print("You WIN! Congratulations!")
                                tile = tile + 5
                                print("You're now at floor " + str(tile) + ".")
                                end = True
                            elif results == "tie":
                                print("your enemy played " + enemySelection + " as well, and so..")
                                print("It's a draw folks!. Let's try that again!\n ")
                            else:
                                print("your enemy played, " + enemySelection)
                                print("you LOSE! Better luck next time!")
                                print("You're now at floor " + str(tile) + ".")
                                end = True

                        else:
                            answer = input("Your input is invalid, please try again\n")