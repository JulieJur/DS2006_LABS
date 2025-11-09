# BOD Task 6
# Change the winner messages
#

import random  # We need random to roll dice

# This line prints a welcome message when the game starts.
print("Welcome to Battle of Dices!")

# Here we keep track of how many rounds each player has won.
player1_wins = 0  # Initialize player 1's win count to 0
player2_wins = 0  # Initialize player 2's win count to 0

# We roll the dice for both players. Each gets a random number between 1 and 6.
player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

# Print the result of each roll so we can see what each player got.
print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

# This variable will remember who won the round.
round_winner = None

# Now we check which player won the round.
# First, we check if player 1's roll is higher than player 2's roll.
if player1_roll > player2_roll:
    # If this is true, player 1 wins the round.
    # We add 1 to player 1's win count.
    player1_wins = player1_wins + 1
    # Remember who won the round.
    round_winner = "Player 1"
    # Print a message saying player 1 wins.
    print("Player 1 wins this round!")

# If the first if is not true, we check if both rolls are equal.
elif player1_roll == player2_roll:
    # If both numbers are the same, it's a tie.
    round_winner = "Tie"
    print("Amaaazzinng! This round has a tie!")

# If neither of the above were true, then player 2 must have the higher roll.
else:
    # Player 2 wins the round.
    player2_wins = player2_wins + 1
    round_winner = "Player 2"
    print("Player 2 wins this round!")

# Here we print a special message if someone has won 3 rounds.
# We check if player 1 has 3 wins.
if player1_wins == 3:
    # If so, print a cool message for player 1.
    print("Player 1 is the newest Battle of Dices Champion! ")

# If not, we check if player 2 has 3 wins.
elif player2_wins == 3:
    # If so, print a cool message for player 2.
    print("Player 2 is the newest Battle of Dices Champion! Hooray!")

# If nobody has 3 wins yet, print that the game continues.
else:
    print("This heated Battle of Dices is still going on! Who will win?")

# Print who won this round.
print("This round's winner is:", round_winner)

# Print the total number of wins for both players.
print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)
