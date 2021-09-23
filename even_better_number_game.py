#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program is the even better number guessing game

import random


def main():
    # This function is the even better number guessing game

    random_number = random.randint(0, 10)

    # Input
    guessed_number = input("Pick a number between 0-10: ")
    print("")

    # Process and Output
    try:
        integer_as_number = int(guessed_number)
        if integer_as_number == random_number:
            print("You guessed the correct number!")
        else:
            print("Incorrect, please run again.")

    except Exception:
        print("This is an invalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
