# BOD Task 2
# Replace the code in Figure 2 with the code in Figure 3

import random

print("Welcome to Battle of Dices!")

player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

print("Player 1 rolled: " + player1_roll)
print("Player 2 rolled: " + player2_roll)

# -----------------------------------------
# Why does this code not work?
#
# player1_roll and player2_roll are numbers (integers) like 1, 2, 3, 4, 5, 6 and so on.
# "Player 1 rolled: " is text (a string).
# In Python, you can't use + to add text and a number together.
# Python stops the program and gives a TypeError.
#
# The error message will say:
#   TypeError: can only concatenate str (not "int") to str
#
# This means: Python wants both things with + to be strings (text).
# If one is a number, you get an error.
#
# To fix this, you need to change the number to a string first with str():
#   print("Player 1 rolled: " + str(player1_roll))
#
# Or, you can use a comma in print() which lets you mix text and numbers:
#   print("Player 1 rolled:", player1_roll)
