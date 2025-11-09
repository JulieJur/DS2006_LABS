# my_dice.py is a module for rolling various types of dice.
# This module provides functions to roll different types of dice under controlled conditions.
# This file has functions to roll different types of dice.
# Each function returns a random number between 1 and the highest number on the die.

# I will use the random module to generate random numbers.
# Die = singular of dice
# In this module, I will create functions to roll D4, D6, D8, D12, and D20. Dices from 4 - 20 sides.. Fantastic Beasts!

import random  # Needed for random numbers


def rollD4():
    # This function simulates a D4 (4-sided die)
    return random.randint(1, 4)


def rollD6():
    # This function simulates a D6 (6-sided die)
    return random.randint(1, 6)


def rollD8():
    # This function simulates a D8 (8-sided die)
    return random.randint(1, 8)


def rollD12():
    # This function simulates a D12 (12-sided die)
    return random.randint(1, 12)


def rollD20():
    # This function simulates a D20 (20-sided die)
    return random.randint(1, 20)
