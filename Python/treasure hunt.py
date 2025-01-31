import random

# Set up the game grid size
grid_size = 5

# Generate random treasure location
treasure_x = random.randint(1, grid_size)
treasure_y = random.randint(1, grid_size)

# Initial player guess
guess_x = 0
guess_y = 0

print(f"Welcome to the Treasure Hunt!")
print(f"Find the hidden treasure on a {grid_size}x{grid_size} grid.")

# Game loop
while (guess_x != treasure_x) or (guess_y != treasure_y):
    # Player's guess
    guess_x = int(input(f"Guess the X coordinate (1-{grid_size}): "))
    guess_y = int(input(f"Guess the Y coordinate (1-{grid_size}): "))

    # Check the guess
    if guess_x == treasure_x and guess_y == treasure_y:
        print("Congratulations! You found the treasure!")
    else:
        if guess_x < treasure_x:
            print("The treasure is further to the right.")
        elif guess_x > treasure_x:
            print("The treasure is further to the left.")

        if guess_y < treasure_y:
            print("The treasure is further down.")
        elif guess_y > treasure_y:
            print("The treasure is further up.")

print("Game Over!")
