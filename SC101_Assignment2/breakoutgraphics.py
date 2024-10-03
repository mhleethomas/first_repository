"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    # construstor
    def __init__(self, ball_radius=BALL_RADIUS,
                 paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle,
                        x=(self.window.width - self.paddle.width) // 2,
                        y=self.window.height - self.paddle.height - PADDLE_OFFSET)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.window.add(self.ball,
                        x=(self.window.width - self.ball.width) // 2,
                        y=(self.window.height - self.ball.height) // 2)

        # Default iinitial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.move_paddle)

        # Draw bricks with different colors for each row
        brick_color = ""
        brick_y_coordinate = BRICK_OFFSET
        for row in range(BRICK_ROWS):
            brick_x_coordinate = 0
            # calaulate the reminder (divided by 10) in case user wants more than 10 BRICK_ROWS
            row = row % 10
            if row == 0 or row == 1:
                brick_color = "red"
            elif row == 2 or row == 3:
                brick_color = "orange"
            elif row == 4 or row == 5:
                brick_color = "yellow"
            elif row == 6 or row == 7:
                brick_color = "green"
            elif row == 8 or row == 9:
                brick_color = "blue"

            for _ in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                self.brick.fill_color = brick_color
                self.brick.color = brick_color
                self.window.add(self.brick, x=brick_x_coordinate, y=brick_y_coordinate)
                brick_x_coordinate += (BRICK_SPACING + BRICK_WIDTH)
            brick_y_coordinate += (BRICK_SPACING + BRICK_HEIGHT)

    # Method
    def move_paddle(self, event):
        # Move paddle's midpoint to follow mouse's x coordinate
        self.paddle.x = event.x - self.paddle.width // 2

        # Keep paddle within window bounds
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.window.width - self.paddle.width < self.paddle.x:
            self.paddle.x = self.window.width - self.paddle.width

    def set_ball_velocity(self, _):
        """
        Set ball velocity when clicked:
        - If ball is stationary at center, give it a random non-zero x velocity and fixed y velocity.
        """
        if self.__dx == 0 \
                and self.__dy == 0 \
                and self.ball.x == (self.window.width - self.ball.width) // 2 \
                and self.ball.y == (self.window.height - self.ball.height) // 2:
            # set x-direction velocity
            self.__dx = random.randint(1, MAX_X_SPEED)

            # True scope: randomly assign +/- value to x-direction velocity
            if random.random() > 0.5:
                self.__dx *= -1

            # set y-direction velocity
            self.__dy = INITIAL_Y_SPEED

    # Getter method
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    @classmethod
    def get_bricks(cls):
        return BRICK_ROWS * BRICK_COLS

    # Setter method
    def set_dx_to_0(self):
        self.__dx = 0

    def set_dy_to_0(self):
        self.__dy = 0
