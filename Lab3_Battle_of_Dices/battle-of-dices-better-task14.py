# Battle of Dices -Task 14
# Better version with two dice for each player
# This code uses MyDice.py for rolling dice as an external module.
#

import MyDice  # We use our own dice-rolling module from MyDice.py

# Before run  the code, make sure I have MyDice.py in the same folder as this file.
# And save the file before run it , the code will inital show it has error and after save it will be fine and work properly.


def roll_die(sides):
    # This function picks the correct die function based on the number of sides.
    if sides == 4:
        return MyDice.rollD4()  # Call the function from MyDice module
    elif sides == 6:
        return MyDice.rollD6()  # Call the function from MyDice module
    elif sides == 8:
        return MyDice.rollD8()  # Call the function from MyDice module
    elif sides == 12:
        return MyDice.rollD12()  # Call the function from MyDice module
    elif sides == 20:
        return MyDice.rollD20()  # Call the function from MyDice module
    else:
        return MyDice.rollD6()  # Default to D6 if something else


print("Welcome to Battle of Dices  two cool dice version!")

# Let the user pick which die to use for both players and both dice.
print("Which die do you want to use for the whole game you are playing?")
print("Type 4 for D4, 6 for D6, 8 for D8, 12 for D12, or 20 for D20:")

DIE_SIDES = int(input("Your choice: "))

# These variables keep the score. the score is the values. So 4 variables and every variable has a value. initially all values are 0. becouse the value is unknown.

player1_wins = 0  # How many rounds Player 1 has won
player2_wins = 0  # How many rounds Player 2 has won

round_winner = None  # Who won the current round
rounds_played = 0  # How many rounds played so far

# Main game loop, keep going until someone gets 3 wins
while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")  # Pause between rounds

    rounds_played = rounds_played + 1  # New round starts, add 1 to counter

    # Player 1 rolls two dice, add them together for the total.
    p1_die1 = roll_die(DIE_SIDES)
    p1_die2 = roll_die(DIE_SIDES)
    player1_total = p1_die1 + p1_die2

    # Player 2 rolls two dice, add them together for the total.
    p2_die1 = roll_die(DIE_SIDES)
    p2_die2 = roll_die(DIE_SIDES)
    player2_total = p2_die1 + p2_die2

    print("Round number:", rounds_played)
    # Show all dice for both players
    print("Player 1 rolled:", p1_die1, "and", p1_die2, "Total:", player1_total)
    print("Player 2 rolled:", p2_die1, "and", p2_die2, "Total:", player2_total)

    # Now I check which player has the highest total after rolling both dice.
    # If Player 1's total is bigger than Player 2's total

    if player1_total > player2_total:
        player1_wins = player1_wins + 1  # I add 1 to Player 1's win count
        round_winner = "Player 1"  # I remember that Player 1 won this round
        print("Player 1 wins this round!")  # Tell the user who won

    # If both players rolled the same total

    elif player1_total == player2_total:
        round_winner = "Tie"  # I remember that it was a tie
        print("Amaaazzinng! This round has a tie!")  # Tell the user it was a tie

    # Otherwise, Player 2's total must be higher

    else:
        player2_wins = player2_wins + 1  # I add 1 to Player 2's win count
        round_winner = "Player 2"  # I remember that Player 2 won this round
        print("Player 2 wins this round!")  # Tell the user who won

    # Show the result of this round to the user.

    print("This round's winner is:", round_winner)  # Print out who won the round
    print(
        "Total wins - Player 1:", player1_wins, "Player 2:", player2_wins
    )  # Print the current score

# When the game is finished (when someone has 3 wins), print out the final results.
print("Game over!")  # Tell the user that the game is done
print(
    "Total number of rounds played:", rounds_played
)  # Show how many rounds were played
print("Player 1 total wins:", player1_wins)  # Show me how many wins Player 1 had.
print("Player 2 total wins:", player2_wins)  # Show me how many wins Player 2 had
