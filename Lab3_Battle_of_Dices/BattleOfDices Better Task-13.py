# Battle of Dices - Task 13
# Better version with a function for rolling
# This code is shorter, easier to change, and still uses MyDice.py for rolling dice as an extern ck+.
# The comments explain every step!

import MyDice  # We use our own dice-rolling functions


# This function rolls the correct type of die, based on sides (4, 6, 8, 12, 20).
# It takes the number of sides as input and returns a random number from the right function.
def roll_die(sides):
    # Depending on sides, we call the right function from MyDice.py. it returns the result.
    if sides == 4:
        return MyDice.rollD4()
    elif sides == 6:
        return MyDice.rollD6()
    elif sides == 8:
        return MyDice.rollD8()
    elif sides == 12:
        return MyDice.rollD12()
    elif sides == 20:
        return MyDice.rollD20()
    else:
        # If something else is typed, use a six-sided die as default.
        return MyDice.rollD6()


# Start of the game:
print("Welcome to Battle of Dices (better version)!")

# Ask the user which die to use, just like before.
print("Which die do you want to use for the whole game?")
print("Type 4 for D4, 6 for D6, 8 for D8, 12 for D12, or 20 for D20:")

DIE_SIDES = int(input("Your choice: "))

player1_wins = 0  # Start at 0 wins for Player 1
player2_wins = 0  # Start at 0 wins for Player 2

round_winner = None  # To remember who won this round

rounds_played = 0  # To count how many rounds we've played

# The while-loop will keep going until one player gets 3 wins.
while player1_wins < 3 and player2_wins < 3:
    # Wait for the user before each round.
    input("\nPress ENTER to roll the dice...")

    # Add 1 to the number of rounds played, because a new round starts now.
    rounds_played = rounds_played + 1

    # Use the roll_die function to get a random number for each player.
    player1_roll = roll_die(DIE_SIDES)
    player2_roll = roll_die(DIE_SIDES)

    # Print which round this is.
    print("Round number:", rounds_played)

    # Show what each player rolled.
    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    # Now check who won the round and update the right counters, and save the winner to round_winner.
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

    # Print who won the round and the total score so far.
    print("This round's winner is:", round_winner)
    print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)

# When a player reaches 3 wins, the game comes to an end.
print("Game over!")
print("Total number of rounds played:", rounds_played)
print("Player 1 total wins:", player1_wins)
print("Player 2 total wins:", player2_wins)
