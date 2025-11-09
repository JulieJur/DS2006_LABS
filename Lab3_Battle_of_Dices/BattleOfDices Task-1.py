# BOD Task 1
# Figure 2 printing style
# We roll two D6 and print the results using + and str(...)

import random

print("Welcome to Battle of Dices!")

# roll a D6 for each player
player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

# Figure 2 style: use + and str() to join text and numbers
print("Player 1 rolled: " + str(player1_roll))
print("Player 2 rolled: " + str(player2_roll))
