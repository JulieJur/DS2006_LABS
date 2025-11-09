# BOD Task 7
# Play several rounds WITHOUT a loop
#
#
# This version repeats the code for each round.
# It is long and hard to update, but helps you see how a program works step by step.
# Repeat all steps for the next round. Copy-paste is used itself to show. that every round is a copy of the previous one.
# No loops are used in this version of the game, this is just copy and paste of the same code for each round.
# The code for every round is exactly the same, just like copy-paste.
# This makes the code very long and hard to update, but it helps me see how the game works step by step.
# The purpose of this version is to learn how the game runs for as many rounds as I want, without using any loops-related control structures, like while or for loops.


import random  # This gives us the ability to roll dice, using random numbers , just like mixing a numbers in a hat.

# Print a welcome message at the start so the user knows what this game is.
print("Welcome to Battle of Dices, we are ready to roll and have ton of fun!")

# These variables will count how many rounds each player has won so far in the game.
player1_wins = 0  # Start at 0, no wins yet
player2_wins = 0  # Start at 0, no wins yet

# This variable will keep track of who wins each round.
# We start with None, meaning "no one has won this round yet."
round_winner = None

# ------------- ROUND 1 -------------
# Before we roll, we want the user to press ENTER.
input("\nPress ENTER to roll the dice for Round 1...")

# Each player rolls their die: a random number between 1 and 6.
player1_roll = random.randint(1, 6)  # Player 1 rolls the die
player2_roll = random.randint(1, 6)  # Player 2 rolls the die

# Print what each player rolled so we can see their numbers.
print("Player 1 rolled:", player1_roll)  # Print Player 1's roll
print("Player 2 rolled:", player2_roll)  # Print Player 2's roll

# Now we check who won this round.
if player1_roll > player2_roll:
    # If Player 1 has a bigger number, they win the round.
    player1_wins = (
        player1_wins + 1
    )  # Add 1 to Player 1's wins, in coding it is called incrementing, as the number goes up or increases by 1.
    round_winner = "Player 1"  # Remember that Player 1 won, here the variable round_winner is updated to store "Player 1"
    print("Player 1 wins this round!")  # Tell the user who won
elif player1_roll == player2_roll:  #
    # If both players rolled the same number, it is a tie.
    round_winner = "Tie"  # Remember that this round was a tie, a tie means no one wins, both players are equal in numbers like two 5's.
    print("Amaaazzinng! This round has a tie!")
else:
    # If Player 2 has a higher number, they win the round.
    player2_wins = player2_wins + 1  # Add 1 to Player 2's wins
    round_winner = "Player 2"  # Remember that Player 2 won
    print("Player 2 wins this round!")

# Print who won this round, and show the current total score after round 1.
print("This round's winner is:", round_winner)
print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)

# ------------- ROUND 2 -------------
# We do exactly the same for the next round.
# Repeat all steps for the next round. Copy-paste is used itself to show. that every round is a copy of the previous one.
# Round 2 is a copy of Round 1, just like Round 3 will be a copy of Round 1 and 2 and so on up to 10 000 000 000 if we want to scroll a lot!

input("\nPress ENTER to roll the dice for Round 2...")

player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    round_winner = "Player 1"
    print("Player 1 wins this round!")
elif player1_roll == player2_roll:
    round_winner = "Tie"
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    round_winner = "Player 2"
    print("Player 2 wins this round!")

print("This round's winner is:", round_winner)
print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)

# ------------- ROUND 3 -------------
# Repeat all steps for the next round. Copy-paste is used itself to show. that every round is a copy of the previous one.

input("\nPress ENTER to roll the dice for last Round of 3...")

player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    round_winner = "Player 1"
    print("Player 1 is the winner!")
elif player1_roll == player2_roll:
    round_winner = "Tie, please play again!"
    print("Amaaazzinng game! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    round_winner = "Player 2"
    print("Player 2 is the winner!")

print("This round's winner is:", round_winner)
print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)


# At the end of all rounds, we print the final result.
print("\n---------------------- FINAL RESULT -----------------------")
if player1_wins > player2_wins:
    print("Player 1 is the overall winner with", player1_wins, "wins!")
elif player2_wins > player1_wins:
    print("Player 2 is the overall winner with", player2_wins, "wins!")
else:
    print("The game ends in a tie with both players having", player1_wins, "wins!")

# ---------------------- EXTRA CODE BELOW, NOT PART OF TASK 7 -----------------------
