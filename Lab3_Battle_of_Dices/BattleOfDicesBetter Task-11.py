# ------------------------- Battle of dices better Task 11 -------------------------#
# Add a round counter
# This version counts how many rounds have been played.

import random  # Needed to roll dice

print("Welcome to Battle of Dices!")

player1_wins = 0  # Counts how many rounds Player 1 has won
player2_wins = 0  # Counts how many rounds Player 2 has won
round_winner = None  # Remembers who won the current round

# New: We use this variable to count how many rounds have been played.
rounds_played = 0  # We start at 0, and add 1 for every round

# The game keeps running until one player has 3 wins. The while-loop does the magic.
while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")  # Wait for the user before each round

    # We are about to play a new round, so we add 1 to the counter.
    rounds_played = rounds_played + 1

    # Each player rolls a number between 1 and 6.
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)

    # Print out which round this is. We need this to keep track.
    print("Round number:", rounds_played)

    # Show what each player rolled. # We need this to see who wins.
    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    # Find out who won the round and update the right counter. # We also remember who won this round.
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

    # Print out who won this round and the score.
    print("This round's winner is:", round_winner)
    print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)

# When the loop ends, someone has reached 3 wins. # The program continues here.
# We print out the final results, including how many rounds were played. The winner wins a big cheerio!
print("Game over!")
print("Total number of rounds played:", rounds_played)
print("Player 1 total wins:", player1_wins)
print("Player 2 total wins:", player2_wins)
