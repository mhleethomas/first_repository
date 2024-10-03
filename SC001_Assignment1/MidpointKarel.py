"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel finds the midpoint of the columns in any size of a world
    starts @ (1, 1)
    1. fills a row with beepers
    2. deal with the 2 beepers at the end of a row (because they are at the end, may cause problem)
    3. collects the left beepers from one side to the other side
    4. the last beeper collects would be around the midpoint
    5. add last adjustment, involving move one step (if necessary)
    6. mark the midpoint with a beeper
    """

    put_beeper_row()
    while on_beeper():
        # moves to (1, 1)
        move()
    if not front_is_clear():
        turn_around()
        if front_is_clear():
            # moves to (1, 2)
            move()
    # Karel is @ (1, 2), facing east, with 1 beeper underneath
    # first row (y = 1) is now full of beepers EXCEPT first and last position (1, 1) , (X, 1)

    while on_beeper():
        # ask if there exists any beeper (in this row)
        find_end_beeper()
        # find the beeper which is located at the end of the beeper row
        turn_around()
        move()
        pick_beeper()
        # after finding that END-BEEPER, pick it up
        move()
        # move 1 step forward to keep the while loop looping
    # while loop ends when no beepers exist in this row
    turn_around()
    if front_is_clear():
        move()
    # to solve OBOB, needs to go back 1 step
    # Karel finds midpoint in a row of the world
    put_beeper()
    # mark the midpoint with a beeper


def put_beeper_row():
    """
    pre-condition: Karel @ (1, 1), facing east
    post-condition: Karel @ (X, 1), facing east
        first row (y = 1) filled with beepers, EXCEPT the first and last position
    """
    if front_is_clear():
        # skip first position
        move()
    while front_is_clear():
        put_beeper()
        move()
    # while loop breaks when hitting the wall
    # will not put a beeper at the last position


def find_end_beeper():
    # Karel moves until stands on an "end-beeper" (of the row)
    while on_beeper():
        if front_is_clear():
            move()


def turn_around():
    # Karel turns left 2 times
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
