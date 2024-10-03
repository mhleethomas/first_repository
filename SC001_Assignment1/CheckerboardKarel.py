"""
File: CheckerboardKarel.py
Name: 李名翔 Thomas
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel uses beepers to form a checkerboard in any size of a world
    Filling from the bottom left corner (1,1) to the right (X,1).
    Filling row by row, from bottom to top.
    1. fill the first row
    2. check the last position of the first row
        if there is NO beeper @ last position, it is a EVEN number world, DO NOT skip 1 step for next row
        if there is a beeper @ last position, it is a ODD number world, skip 1 step for next row
    3. check if this row is the last row
        if this is the last row, DO NOT fill the next row
        if this is NOT the last row, fill the next row
    """

    while front_is_clear():
        fill_a_row()
        if not on_beeper():
            # yes scope: even number world
            # go to next row, then fill it as usual
            move_up_a_row()
        else:
            # no scope: odd number world
            # go to next row, skip 1 step, then fill it
            move_up_a_row()
            if front_is_clear():
                move()

    if not front_is_clear():
        # True scope: 1 * x world
        if not left_is_clear():
            # True scope: 1 * 1 world
            put_beeper()
        else:
            fill_a_col()

    """
    2024/ 04/ 25 revised
    """


def fill_a_row():
    """
    pre-condition: Karel @ start of any row
        (could be facing either east or west)
        0 beeper in this row
    post-condition: Karel @ end of any row, facing the same direction as pre-condition
        (could be either on or not on a beeper depends on the amount of columns of the world)
        skip fills beepers in a single row, and checks beeper status at the last position of a row
    """
    while front_is_clear():
        # Karel keeps filling beeper till the end of a row
        put_beeper()
        for i in range(2):
            # moves 2 step everytime Karel puts a beeper
            if front_is_clear():
                move()
    # Karel at the end of a row
    turn_around()
    move()
    turn_around()
    # moves to the second last position to check if there is a beeper
    # turn around 2 times to maintain the same direction
    if on_beeper():
        # yes scope: even number world
        move()
    else:
        # no scope: odd number world
        move()
        put_beeper()
        # put this beeper to solve OBOB


def move_up_a_row():
    """
    pre-condition: Karel @ row y, could be facing east or west.
    post-condition: Karel @ row y + 1, facing WEST or EAST (opposite direction of pre-condition)
    """
    if facing_east():
        # yes scope: Karel facing east, means Karel is on a ODD number row (1st, 3rd... row)
        turn_left()
        if front_is_clear():
            move()
            turn_left()
    # Karel facing opposite direction of pre-condition (WEST)
    else:
        # no scope: Karel facing west, means Karel is on a EVEN number row (2nd, 4th... row)
        turn_right()
        if front_is_clear():
            move()
            turn_right()
    # Karel facing opposite direction of pre-condition (EAST)


def fill_a_col():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()



def turn_right():
    # Karel turns left 3 times
    for i in range(3):
        turn_left()


def turn_around():
    # Karel turns left 2 times
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
