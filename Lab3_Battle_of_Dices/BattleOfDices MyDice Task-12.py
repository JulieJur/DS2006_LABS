# BOD Task 12 — Use dice functions from my_dice.py
# This game uses a special module (my_dice.py) to roll dice of different sizes.
# The user can choose which die to use for the whole game.

import MyDice  # We import our own file called MyDice from our Lab3 folder with dice-rolling functions.

# if the name of the file is not correct, this will give an error, and the code will not run.

# This lets us use the functions defined in that file. # We will use MyDice.rollD4(), MyDice.rollD6(), etc.

# Print a welcome message at the start of the game.
print("Welcome to Battle of Dices!")

# Now we want the player to choose what kind of die to use.
print("Which die do you want to use for the whole game?")
# lets the user know what to type and choices available
print("Type 4 for D4, 6 for D6, 8 for D8, 12 for D12, or 20 for D20:")

# input() lets the user type something.
# input() always gives us a string (text), so we use int() to turn it into a number.
DIE_SIDES = int(input("Your choice: "))

# We set up variables to count how many rounds each player has won.
player1_wins = 0  # Start at 0 wins for Player 1
player2_wins = 0  # Start at 0 wins for Player 2

# This variable will remember who won the latest round.
round_winner = None

# This variable counts how many rounds have been played.
rounds_played = 0  # Start at 0

# Now we start the main game loop.
# The loop keeps going until one of the players has won 3 times.
while player1_wins < 3 and player2_wins < 3:
    # We wait for the user to press ENTER before each round starts.
    input("\nPress ENTER to roll the dice...")

    # We are about to play a new round, so add 1 to the rounds_played counter.
    rounds_played = rounds_played + 1

    # We have to roll the kind of die that the user chose.
    # If the player chose 4, we call the rollD4 function in my_dice.py.
    # If they chose 6, we call rollD6, etc.
    if DIE_SIDES == 4:
        player1_roll = (
            MyDice.rollD4()
        )  # Call the function to roll a D4 die for Player 1
        player2_roll = (
            MyDice.rollD4()
        )  # Call the function to roll a D4 die for Player 2
    elif DIE_SIDES == 6:
        player1_roll = (
            MyDice.rollD6()
        )  # Call the function to roll a D6 die for Player 1
        player2_roll = (
            MyDice.rollD6()
        )  # Call the function to roll a D6 die for Player 2
    elif DIE_SIDES == 8:
        player1_roll = (
            MyDice.rollD8()
        )  # Call the function to roll an D8 die for Player 1
        player2_roll = (
            MyDice.rollD8()
        )  # Call the function to roll an D8 die for Player 2
    elif DIE_SIDES == 12:
        player1_roll = (
            MyDice.rollD12()
        )  # Call the function to roll a D12 die for Player 1
        player2_roll = (
            MyDice.rollD12()
        )  # Call the function to roll a D12 die for Player 2
    elif DIE_SIDES == 20:
        player1_roll = (
            MyDice.rollD20()
        )  # Call the function to roll a D20 die for Player 1
        player2_roll = (
            MyDice.rollD20()
        )  # Call the function to roll a D20 die for Player 2
    else:
        # If the player types something else, we use D6 by default.
        player1_roll = (
            MyDice.rollD6()
        )  # Call the function to roll a D6 die for Player 1
        player2_roll = (
            MyDice.rollD6()
        )  # Call the function to roll a D6 die for Player 2

    # Print which round this is.
    print("Round number:", rounds_played)  # Print the round number.

    # Print the result for both players.
    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    # Now we check who won this round.
    # If Player 1's number is higher, add 1 to their win count and print a message.
    if player1_roll > player2_roll:
        player1_wins = player1_wins + 1
        round_winner = "Player 1"
        print("Player 1 wins this round!")
    # If both rolled the same number, it's a tie.
    elif player1_roll == player2_roll:
        round_winner = "Tie"
        print("Amaaazzinng! This round has a tie!")
    # If Player 2's number is higher, add 1 to their win count and print a message.
    else:
        player2_wins = player2_wins + 1
        round_winner = "Player 2"
        print("Player 2 wins this round!")

    # Print who won this round.
    print("This round's winner is:", round_winner)

    # Print the total number of wins for both players so far.
    print("Total wins - Player 1:", player1_wins, "Player 2:", player2_wins)

# When the while-loop ends, it means someone has reached 3 wins and the game is over.
print("Game over!")
print("Total number of rounds played:", rounds_played)
print("Player 1 total wins:", player1_wins)
print("Player 2 total wins:", player2_wins)
