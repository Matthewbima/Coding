#Number Guessing Game Objectives:

# Include an ASCII art logo.py.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

random_number = random.randint(1,50)
HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10

# Functions Area
def compare(target, guess):
  """Check answer is it the same with the guess submitted by the user returns True if the user get it right and return False if the user still got it wrong"""
  if guess == target:
    print(f"You got it! The answer is {target}")
  elif guess > target:
    print("Too High")
  elif guess < target:
    print("Too Low")

def check_lives(lives):
  if lives > 0:
    print(f"Attempts remaining {lives}")
  else:
    return True

def set_difficulties():
  difficulties_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if difficulties_input == "easy":
    return EASY_ATTEMPTS
  elif difficulties_input == "hard":
    return HARD_ATTEMPTS
  else:
    print("You neither input 'hard' or 'easy'. I will take that as easy")
    return EASY_ATTEMPTS

def game():
  print("Welcome to the number guessing game!")
  print("I am thinking of a number between 1 and 50, can you guess what number it is? ")

  turns = set_difficulties()
  guess = 0

  while turns > 0 and guess != random_number:
    check_lives(turns)
    guess = int(input("Make a guess: "))

    turns -= 1

    compare(target = random_number, guess = guess)
    
    if turns == 0:
      print("You ran out of attempts!")

# Functions Area END

game()