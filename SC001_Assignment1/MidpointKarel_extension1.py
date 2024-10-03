"""
File: extension1_MidpointKarel.py
Name: 李名翔 Thomas
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
    1. fill a row with beepers, using the same amount of beepers as the size of the world
        5 beepers for a 5-column world, 8 beepers for a 8-column world
    2. put all the beepers placed to a certain location (x) to serve as a counter
    3. divide the counter by 2 (makes a new counter next to the old counter, and counts x/2)
    4. reallocate the new counter (x /2) from east to west, 1 after 1
        if x/2 equals to 3, then reallocate them as (1, 1, 1) from east to west
        if x/2 equals to 4, then reallocate them as (1, 1, 1, 1) from east to west
    5. when finished reallocating the new counter, last beeper will be 1 step west of the midpoint
    6. collect all the reallocated beepers, and Karel will be 1 step west of the midpoint
    7. move towards east for 1 step, and put a beeper to mark the midpoint
    """

    put_beeper_row()
    # fill a row with beepers, EXCEPT last position x
    # Karel @ x, facing west
    # counter @ x, counts: 1
    measure_world_size()
    # counter @ x, counts: x (size of the world)
    counter_divided_by_2()
    # Karel @ x, facing west
    # counter counts: x/2
    reallocate_beeper_according_to_counter()
    collect_reallocated_beepers()
    if front_is_clear():
        # move towards east for 1 step
        move()
    put_beeper()
    # put a beeper to mark the midpoint


def put_beeper_row():
    """
    pre-condition: Karel @ 1, facing east
    post-condition: Karel @ x, facing WEST
        first row filled with beepers
    """
    while front_is_clear():
        # puts a row of beepers
        put_beeper()
        move()
    turn_west()
    put_beeper()
    # put 1 more beeper due to OBOB


def measure_world_size():
    """
    pre-condition: Karel @ x, facing west
        counter @ x, counts: 1
    post-condition: Karel @ x, facing west
        counter @ x, counts: x
    """
    while front_is_clear():
        # keep moving till hitting the wall (on the west)
        move()
        if on_beeper():
            # yes scope: finds a beeper in the beeper row
            # pick up that beeper and put it to the counter @ x
            # so the counter adds 1 whenever finds a beeper
            pick_beeper()
            put_beeper_to_counter()
        # picks up all beepers in the row and put them all to a counter @ x
    move_to_counter()


def put_beeper_to_counter():
    # Karel puts 1 beeper to a counter @ x, and stays @ x, facing west
    turn_east()
    while front_is_clear():
        # keep moving till hitting the wall (on the east) (where the counter is set)
        move()
    put_beeper()
    # counter @ x, count adds 1
    turn_west()


def move_to_counter():
    # Karel moves to the counter which is located @ x
    turn_east()
    while front_is_clear():
        move()
    turn_west()


def counter_divided_by_2():
    """
    pre-condition: Karel @ x, facing west
        counter counts x
    post-condition: Karel @ x, facing west
        old counter counts 0
        new counter counts x/2 (or (x + 1)/2 for x is odd number)
    """
    while on_beeper():
        """
        pre-condition: counter @ location x, counts x
        post-condition: old counter (X) replaced by a new counter (@ location x - 1)
            x is a odd number: new counter counts (x + 1)/2
            x is a even number: new counter counts x/2
        """
        turn_west()
        pick_beeper()
        # old counter @ x, count minus 1
        if on_beeper():
            # if statement to prevent error
            # error will happen when old counter originally counts an odd number
            pick_beeper()
            # old counter @ x, count minus 1 again
            turn_west()
        if front_is_clear():
            # if statement to prevent error
            # error will happen in a 1*1 world
            move()
            # Karel @ x - 1, ready to set a new counter
            put_beeper()
            # new counter @ X-1, counts 1
            turn_east()
            move()
            # Karel returns to x, where the old counter is located
            # if the old counter still remains at least 1 beeper, while loop will keep looping
            # while loop breaks when the old counter counts to 0
    turn_west()
    if front_is_clear():
        move()
    while on_beeper():
        """
        pre-condition: new counter @ location x - 1
            x is odd number: counter counts (x + 1)/2
            x is even number: counter counts x/2
        post-condition: new counter @ location x
            x is odd number: counter counts (x + 1)/2
            x is even number: counter counts x/2
        This block of code is to move the new counter from x - 1 to x
        """
        pick_beeper()
        move_to_counter()
        # move to counter @ x
        # move_to_counter() will make Karel turn WEST
        put_beeper()
        move()
        # move toward west 1 step to x - 1
    move_to_counter()


def reallocate_beeper_according_to_counter():
    """
    pre-condition: Karel @ x, facing west
        x is a even number: new counter @ x, counts x/2
        x is a odd number: new counter @ x counts (x + 1)/2
    post-condition: Karel @ x-1, facing west
        new counter reallocated. locating @ x-1, x-2, x-3..., all counting 1s
    """
    while on_beeper():
        # keep reallocating the new counter into 1s @ different locations (x - 1, x - 2, x - 3...)
        move()
        # Karel moves to x-1
        while on_beeper():
            # keep Karel moving until Karel @ left end of the beeper row
            move()
        put_beeper()
        # put a beeper at the left end of the beeper row
        move_to_counter()
        if on_beeper():
            # ask if there is any beepers left @ x
            pick_beeper()
    # Karel @ x when the while loop breaks
    if front_is_clear():
        move()
    # Karel @ x-1 (right end of the reallocated beepers)


def collect_reallocated_beepers():
    """
    pre-condition: Karel @ right end of beeper row (x - 1), facing west
    post-condition: Karel @ left end of beeper row, facing west
        x is odd number: Karel @ (x + 1)/2 - 1
        x is even number: Karel @ x/2
    """
    while on_beeper():
        # Karel keeps picking up beepers towards west
        # while loop breaks when all beeper been collected
        pick_beeper()
        if front_is_clear():
            move()
    turn_east()
    if front_is_clear():
        move()
    # move toward east for 1 step to solve OBOB


def turn_around():
    # Karel turns left 2 times
    for i in range(2):
        turn_left()


def turn_east():
    # Karel keeps turn left until facing east
    while not facing_east():
        turn_left()


def turn_west():
    # Karel keeps turn left until facing west
    while not facing_west():
        turn_left()


if __name__ == '__main__':
    execute_karel_task(main)
