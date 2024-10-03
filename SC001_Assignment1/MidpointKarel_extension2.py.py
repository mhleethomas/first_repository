"""
File: extension2_MidpointKarel.py
Name:李名翔 Thomas
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
    Karel finds the midpoint of the columns in any size of a world and put a beeper
    starts @ (1, 1)
    because we will only find the midpoint of a row, so we can simplified the world to 1 dimension
    1. Karel puts 2 beepers, one @ 1 and the other @ x
    2. check if two beepers are next to each other every time before moving any beeper
        if 2 beepers are next to each other: midpoint found ---> break while loop and mark midpoint
        if 2 beepers are NOT next to each other: midpoint NOT found ---> keep bringing 2 beepers closer to each other
    3. repeat until 2 beepers are next to each other, midpoint found ---> break while loop and mark midpoint
    """

    set_2_beepers()
    # 2 beepers set, one @ 1, another @ x
    while on_beeper():
        # keep looping until these 2 beepers got recycled
        # a function will recycle these 2 beepers when midpoint is found
        if on_beeper():
            # this if statement is to make the main scope more symmetrical
            check_left_beeper()
            # Karel will turn SOUTH if a beeper is 1 step to the left (2 beepers next to each other)
            # Karel will turn NORTH if NO beeper is 1 step to the left (2 beepers NOT next to each other)
        if facing_north():
            # NO beeper is 1 step to the left (2 beepers NOT next to each other)
            # need to bring left beepers closer
            move_to_left_beeper()
            put_beeper_plus_one()
            # brings left beeper 1 step closer (towards right)
        if facing_south():
            # a beeper is 1 step to the left (2 beepers next to each other)
            # midpoint found, clean these 2 beepers to break the while loop
            clean_right_left_beeper()

        if on_beeper():
            check_right_beeper()
            # Karel will turn SOUTH if a beeper is 1 step to the right (2 beepers next to each other)
            # Karel will turn NORTH if NO beeper is 1 step to the right (2 beepers NOT next to each other)
        if facing_north():
            # NO beeper is 1 step to the right (2 beepers NOT next to each other)
            # need to bring right beepers closer
            move_to_right_beeper()
            put_beeper_minus_one()
            # brings right beeper 1 step closer (towards left)
        if facing_south():
            # a beeper is 1 step to the right (2 beepers next to each other)
            # midpoint found, clean these 2 beepers to break the while loop
            clean_left_right_beeper()

    put_beeper()
    # since both beepers got picked up, mark the midpoint with a new beeper


def set_2_beepers():
    # put beepers, 1 on the left end (1), 1 on the right end (x)
    put_beeper()
    # put first beeper @ left end (1)
    turn_east()
    while front_is_clear():
        # moves to right end of the world
        move()
    put_beeper()
    # put second beeper @ the right end (x)


def check_left_beeper():
    # check if there is a beeper 1 step to the left
    # if there is a beeper 1 step to the left, Karel turns SOUTH
    # if there is NO beeper 1 step to the left, Karel turns NORTH
    # Karel returns to previous location
    turn_west()
    if front_is_clear():
        move()
        if on_beeper():
            # yes scope: a beeper is 1 step on the left, Karel turns SOUTH
            turn_east()
            if front_is_clear():
                # return to previous location
                move()
                turn_south()
        else:
            # no scope: no beeper is 1 step on the left, Karel turns NORTH
            turn_east()
            if front_is_clear():
                # return to previous location
                move()
                turn_north()
    else:
        # no scope: front is not clear, happens when x = 1
        # no beeper is 1 step on the left, Karel turns NORTH
        turn_north()


def check_right_beeper():
    # check if there is a beeper 1 step to the right
    # if there is a beeper 1 step to the right, Karel turns SOUTH
    # if there is NO beeper 1 step to the right, Karel turns NORTH
    # Karel returns to previous location
    turn_east()
    if front_is_clear():
        move()
        if on_beeper():
            # yes scope: a beeper is 1 step on the right, Karel turns SOUTH
            turn_west()
            if front_is_clear():
                # return to previous location
                move()
                turn_south()
        else:
            # no scope: no beeper is 1 step on the right, Karel turns NORTH
            turn_west()
            if front_is_clear():
                # return to previous location
                move()
                turn_north()
    else:
        # no scope: front is not clear, happens when x = 1
        # no beeper is 1 step on the right, Karel turns NORTH
        turn_north()


def move_to_left_beeper():
    """
    pre-condition: Karel on the RIGHT beeper, facing anywhere
    post-condition: Karel on the LEFT beeper, facing WEST
    """
    turn_west()
    # turn to -x direction, ready to go west
    if front_is_clear():
        # move 1 step in advance so that the following while loop can find the beeper on the WEST
        move()
    while not on_beeper():
        # Karel keeps moving till standing on the beeper on the west
        move()


def move_to_right_beeper():
    """
    pre-condition: Karel on the LEFT beeper, facing anywhere
    post-condition: Karel on the RIGHT beeper, facing EAST
    """
    turn_east()
    # turn to +x direction, ready to go east
    if front_is_clear():
        # move 1 step in advance so that the following while loop can find the beeper on the EAST
        move()
    while not on_beeper():
        # Karel keeps moving till standing on the beeper on the east
        move()


def put_beeper_plus_one():
    # Karel picks up a beeper and put it 1 step to the right
    pick_beeper()
    turn_east()
    if front_is_clear():
        move()
        put_beeper()


def put_beeper_minus_one():
    # Karel picks up a beeper and put it 1 step to the left
    pick_beeper()
    turn_west()
    if front_is_clear():
        move()
        put_beeper()


def clean_right_left_beeper():
    """
    pre-condition: 2 beepers are next to each other, Karel is on the RIGHT beeper
    post-condition: 2 beepers picked up, Karel returns to previous location (RIGHT)
    Karel picks up 2 beepers, from RIGHT to LEFT, and returns to RIGHT
    """
    pick_beeper()
    # pick up RIGHT beeper
    turn_west()
    if front_is_clear():
        move()
        pick_beeper()
        # pick up LEFT beeper
    else:
        # no scope: front is not clear, happens when x = 1
        pick_beeper()
    turn_east()
    if front_is_clear():
        move()
    # move 1 step toward right, return to previous location


def clean_left_right_beeper():
    """
    pre-condition: 2 beepers are next t
    pre-condition: 2 beepers are next to each other, Karel is on the LEFT beeper
    post-condition: 2 beepers picked up, Karel returns to previous location (LEFT)
    Karel picks up 2 beepers, from LEFT to RIGHT, and returns to LEFT
    """
    pick_beeper()
    # pick up LEFT beeper
    turn_east()
    if front_is_clear():
        move()
        pick_beeper()
        # pick up RIGHT beeper
    else:
        # no scope: front is not clear, happens when x = 1
        pick_beeper()
    turn_west()
    if front_is_clear():
        move()
    # move 1 step toward left, return to previous location


def turn_east():
    # Karel keeps turn left until facing east
    while not facing_east():
        turn_left()


def turn_west():
    # Karel keeps turn left until facing west
    while not facing_west():
        turn_left()


def turn_south():
    # Karel keeps turn left until facing south
    while not facing_south():
        turn_left()


def turn_north():
    # Karel keeps turn left until facing north
    while not facing_north():
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
