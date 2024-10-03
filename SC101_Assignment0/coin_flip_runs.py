"""
File: coin_flip_runs.py
Name: Ming-Hsiang (Thomas), Lee
-----------------------
This program should simulate coin flip(s) with the number of runs input by users.
A 'run' is defined as consecutive results on either 'H' or 'T'.
For example, 'HHHHHTHTT' is regarded as a 2-run result.
Program should stop immediately after your coin flip results reach the number of runs!
"""

import random as r


def main():
    """
    1. Print a welcome message
    2. Get number of runs (integer)
    3. Keep flipping coins until reaching the number of runs
    """
    # Initialize variables
    display = ""
    run_counter = 0
    running = False

    # Print welcome message
    print("Let's flip a coin")
    # Get number of runs
    number_of_runs = int(input("Number of runs: "))

    # Flip 2 coins initially
    coin1 = r.randrange(1, 3)
    coin2 = r.randrange(1, 3)

    # While loop scope: keep flipping coins until the number of runs is met
    while run_counter < number_of_runs:
        # True scope: 2 coins show the same side, running
        if coin1 == coin2:
            # True scope: currently not running. Start running, and add 1 to counter
            if not running:
                run_counter += 1
            running = True
        # False scope: 2 coins do NOT show the same side, stop running
        else:
            running = False

        # Concatenation of the results of flipping coins
        if coin1 == 1:
            display += "H"
        elif coin1 == 2:
            display += "T"

        # Store the 2nd coin result into the 1st coin
        coin1 = coin2
        # Flip next coin
        coin2 = r.randrange(1, 3)

    # Concatenation of the LAST result of flipping coins, avoiding off-by-one bug
    if coin1 == 1:
        display += "H"
    elif coin1 == 2:
        display += "T"

    # Print the result
    print(display)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
    main()
