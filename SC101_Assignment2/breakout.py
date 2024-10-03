"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # Frames per second for the game animation
NUM_LIVES = 3           # Number of lives the player starts with


def main():
    """
    1. this is a breakout game
    2. there are some objects listed as below:
        (1) a paddle that moves according to user's mouse coordinate
        (2) a black ball at the center of window, it will go in a random direction after user mouseclick
        (3) certain amount of bricks (default is 10 * 10)
    3. ball will only go out of window from the bottom side of the window
    4. game over in either conditions:
        (1) ball goes out of window 3 times
        (2) all 100 bricks are removed
    """

    graphics = BreakoutGraphics()

    # Variables to keep track of game status
    out_of_window = 0  # Number of times the ball has gone out of the window
    removed_bricks = 0  # Number of bricks that have been removed

    dx = 0  # Current horizontal velocity of the ball
    dy = 0  # Current vertical velocity of the ball
    velocity_is_zero = True  # Flag to indicate if the ball's velocity is currently (0, 0)

    "##################################################################################################################"
    # Add the animation loop here!
    # Main animation loop
    while True:
        # Check if we need to set a new velocity for the ball
        if velocity_is_zero:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            # True scope: (dx, dy) is not (0, 0)
            if dx != 0 and dy != 0:
                velocity_is_zero = False
        "##############################################################################################################"
        # Update ball position and check collisions if conditions are met
        """
        True scope: ball moves if all 3 contitions been met:
            1. velocity is NOT (0, 0)
            2. still remains lives (ball goes out of window will cost 1 live)
            3. have not remove all the bricks
        """
        if not velocity_is_zero \
                and out_of_window < NUM_LIVES \
                and removed_bricks < graphics.get_bricks():
            graphics.ball.move(dx, dy)

            "##########################################################################################################"
            # Check for window boundaries collisions
            # True scope: ball hits left or right side of window
            if graphics.ball.x <= 0 \
                    or graphics.window.width <= graphics.ball.x + graphics.ball.width:
                dx *= -1

            # True scope: ball hits top side of window
            if graphics.ball.y <= 0:
                dy *= -1

            # True scope: ball encounters bottom side of window
            elif graphics.window.height <= graphics.ball.y + graphics.ball.height:
                # Ball has gone out of the window, reset its position and velocity
                graphics.window.add(graphics.ball,
                                    x=(graphics.window.width - graphics.ball.width) // 2,
                                    y=(graphics.window.height - graphics.ball.height) // 2)
                graphics.set_dx_to_0()
                graphics.set_dy_to_0()
                velocity_is_zero = True
                out_of_window += 1

            "##########################################################################################################"
            # Check object collision
            # get an object at 4 corners of the ball
            maybe_object = graphics.window.get_object_at(graphics.ball.x,
                                                         graphics.ball.y)
            if not maybe_object:
                maybe_object = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                             graphics.ball.y)
                if not maybe_object:
                    maybe_object = graphics.window.get_object_at(graphics.ball.x,
                                                                 graphics.ball.y + graphics.ball.height)
                    if not maybe_object:
                        maybe_object = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                                     graphics.ball.y + graphics.ball.height)

            # True scope: get any oject at 1 of the 4 corners of the ball
            if maybe_object:
                dy *= -1  # Reverse vertical direction upon collision

                # If the object hit is a brick, remove it and update removed_bricks count
                if maybe_object is not graphics.paddle:
                    graphics.window.remove(maybe_object)
                    removed_bricks += 1

                # If the object hit is the paddle, bounce the ball upwards (negative y direction)
                else:
                    if dy > 0:
                        dy *= -1
            "##########################################################################################################"
        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
