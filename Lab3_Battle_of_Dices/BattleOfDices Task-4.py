# BOD Task 4
# Add a variable to store the round winner, and explain if-statement

import random

print("Welcome to Battle of Dices!")

player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

# This variable will remember who won this round.
# At the start, it has the value None, which means "no winner yet".
round_winner = None

# Here comes the if-statement.
# An if-statement lets the code check a condition ("is something true?").
# The first part (if ...) checks if player 1's roll is higher than player 2's roll.
# If this is true, the code inside the block will run:
#   - round_winner is set to "Player 1"
#   - A message is printed saying player 1 wins this round
if player1_roll > player2_roll:
    round_winner = "Player 1"
    print("Player 1 wins this round!")
    print("Because", player1_roll, "is greater than", player2_roll)

# If the first condition is not true, Python checks the next part (elif ...)
# This checks if both rolls are the same (a tie).
# If this is true, the code inside this block will run:
#   - round_winner is set to "Tie"
#   - A message is printed saying it's a tie
elif player1_roll == player2_roll:
    round_winner = "Tie"
    print("Amaaazzinng! This round has a tie!")

# If neither of the above are true (so player 2 must have the higher roll),
# the code in the else block will run:
#   - round_winner is set to "Player 2"
#   - A message is printed saying player 2 wins
else:
    round_winner = "Player 2"
    print("Player 2 wins this round!")
    print("Because", player2_roll, "is greater than", player1_roll)

# After the if-statement, we print who won the round.
print("This round's winner is:", round_winner)
