# ------------------------- Battle of dices better Task 10 -------------------------#
#
# This is an improved version of the "Battle of Dices" game whit a while-loop.
# The game continues until one player wins 3 rounds.
# This code will keep playing new rounds until one player has 3 wins.

import random  # We use this to roll dice

# Print a welcome message at the start of the game.
print("Welcome to Battle of Dices!")

# We use these variables to count how many rounds each player has won.
player1_wins = 0  # Start at 0 for Player 1
player2_wins = 0  # Start at 0 for Player 2

# This variable will keep track of who won the latest round.
round_winner = None

# Here comes the while-loop dancing in from the deepest library section
# The while-loop keeps repeating everything inside it as long as the condition is true. when it is false, it stops and prints the final results.
# The condition is: "player1_wins < 3 and player2_wins < 3"
# This means: Keep going until either player1_wins or player2_wins reaches 3.

while player1_wins < 3 and player2_wins < 3:

    # The code below will run again and again (for each round).

    # Pause the program and wait for the user to press ENTER before each round.
    input("\nPress ENTER to roll the dice...")

    # Both players roll their dice: a random number between 1 and 6.
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)

    # Print what both players rolled so we can see the numbers.
    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    # Now we check who won this round with if/elif/else.
    if player1_roll > player2_roll:
        # If Player 1's number is higher, they win the round.
        player1_wins = player1_wins + 1  # Add 1 to Player 1's wins
        round_winner = "Player 1"
        print("Player 1 wins this round!")
    elif player1_roll == player2_roll:
        # If both numbers are the same, it is a tie.
        round_winner = "Tie"
        print("Amaaazzinng! This round has a tie!")
    else:
        # If Player 2's number is higher, they win the round.
        player2_wins = player2_wins + 1  # Add 1 to Player 2's wins
        round_winner = "Player 2"
        print("Player 2 wins this round!")

    # Print who won this round.
    print("This round's winner is:", round_winner)

    # Print the current total number of wins for both players.
    print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)

# When the loop is finished, that means someone has reached 3 wins.
# The program will move on to this part.
print("Game over!")

# Print out the final number of wins for both players.
print("Player 1 total wins:", player1_wins)
print("Player 2 total wins:", player2_wins)
