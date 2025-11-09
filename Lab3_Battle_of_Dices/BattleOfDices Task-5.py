# BOD Task 5
# Add variables to keep track of wins

import random

print("Welcome to Battle of Dices!")

# These variables will count how many rounds each player has won so far. zero at the start, because no rounds have been played yet.
player1_wins = 0
player2_wins = 0

player1_roll = random.randint(1, 6)  # Random number between 1 and 6 for player 1
player2_roll = random.randint(1, 6)  # Random number between 1 and 6 for player 2

print("Player 1 rolled:", player1_roll)  # Print player 1's roll
print("Player 2 rolled:", player2_roll)  # Print player 2's roll

# We use round_winner to remember who won this round. None at the start, because we haven't checked yet. We will check in the if statements below.
round_winner = None

# Now we use if, elif, and else to check who won, just like before.
# But now, we also add 1 to the winner's score when they win.
if player1_roll > player2_roll:
    # Player 1 rolled higher, so they win this round.
    player1_wins = player1_wins + 1  # Add 1 to player 1's win count
    round_winner = "Player 1"
    print("Player 1 wins this round!")
    print("Because", player1_roll, "is greater than", player2_roll)
elif player1_roll == player2_roll:
    # Both rolls are the same, so it's a tie.
    round_winner = "Tie"
    print("Amaaazzinng! This round has a tie!")
else:
    # Player 2 rolled higher, so they win this round.
    player2_wins = player2_wins + 1  # Add 1 to player 2's win count
    round_winner = "Player 2"
    print("Player 2 wins this round!")
    print("Because", player2_roll, "is greater than", player1_roll)

# Print out who won this round.
print("This round's winner is:", round_winner)

# Print the total wins for each player so far. # New line added
print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)
