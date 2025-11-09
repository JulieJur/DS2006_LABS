# BOD Task 3
# Use Figure 1 for printing, then compare rolls as in Figure 4

import random

print("Welcome to Battle of Dices!")

player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

# Printing with commas lets us mix text and numbers easily.
print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

# Now we check who won the round.
# If player 1 has a higher number, print that player 1 wins.
# If both have the same number, it is a tie.
# Otherwise, player 2 has the higher number and wins.
if player1_roll > player2_roll:
    print("Player 1 wins this round!")
    print("Because", player1_roll, "is greater than", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    print("Player 2 wins this round!")
    print("Because", player2_roll, "is greater than", player1_roll)

# This code uses 'if', 'elif', and 'else' to check each case.
# Only one of these blocks will run each time the code is used.
