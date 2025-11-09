# BOD Task 8.
# Let the user pick which die to use (D4, D6, D8, D12, or D20)
# The rest of the code is the same as before, but now the user can choose the die type.


import random  # Needed to roll dice

print("Welcome to Battle of Dices!")

# Here we ask the user which die they want to use.
# We tell them the allowed options.
print("Which die do you want to use for the whole game?")
print("Type 4 for D4, 6 for D6, 8 for D8, 12 for D12, or 20 for D20:")

# input() lets the user type a number, but input always gives us a string.
# We use int() to change it into a number we can use.
DIE_SIDES = int(input("Your choice: "))

# Now we set up everything else for the game.
player1_wins = 0  # Count Player 1's wins
player2_wins = 0  # Count Player 2's wins
round_winner = None  # Remember who won each round

# --------- ROUND 1 ---------
input("\nPress ENTER to roll the dice for Round 1...")

player1_roll = random.randint(1, DIE_SIDES)  # Player 1 rolls the chosen die
player2_roll = random.randint(1, DIE_SIDES)  # Player 2 rolls the chosen die

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

# --------- ROUND 2 ---------
input("\nPress ENTER to roll the dice for Round 2...")

player1_roll = random.randint(1, DIE_SIDES)
player2_roll = random.randint(1, DIE_SIDES)

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

# --------- ROUND 3 ---------
input("\nPress ENTER to roll the dice for Round 3...")

player1_roll = random.randint(1, DIE_SIDES)
player2_roll = random.randint(1, DIE_SIDES)

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

# If you want more rounds, copy the block above and change the round number!
# Remember: without loops, the file gets longer and longer for every new round.
# This is why loops are better for bigger games, which make the code shorter and easier to read and understand for a beginner like me!
