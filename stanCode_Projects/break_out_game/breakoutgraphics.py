"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 2       # Maximum initial horizontal speed for the ball.


score = 0  # python不給改 講名字就死了
score_label = GLabel('Score: ' + str(score))



class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.r = ball_radius
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT, x=(self.window_width-PADDLE_WIDTH)/2,
                       y=self.window_height-PADDLE_OFFSET)
        self.paddle.color = True
        self.paddle.filled = 'black'
        self.window.add(self.paddle)

        # velocity __private
        self.__dx = 0
        self.__dy = 0

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True

        self.reset_ball()

        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED

        # onmouseclicked(self.paddle)


        #  Create a brick


        # Default initial velocity for the ball

        # Initialize our mouse listeners

        # Draw bricks
        # 迴圈外的原點
        self.position_x = 0 - brick_width - brick_spacing
        self.position_y = brick_offset
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.position_x += brick_width + brick_spacing
                self.bricks = GRect(width=brick_width, height=brick_height)
                if i <= 1:
                    self.bricks.color = 'red'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'red'
                elif 1 < i <= 3:
                    self.bricks.color = 'orange'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'orange'
                elif 3 < i <= 5:
                    self.bricks.color = 'yellow'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'yellow'
                elif 5 < i <= 7:
                    self.bricks.color = 'green'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'green'
                elif 7 < i <= 9:
                    self.bricks.color = 'blue'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, x=self.position_x, y=self.position_y)
            # 做完迴圈 控制變化量
            self.position_y += brick_height + brick_spacing
            self.position_x = 0 - brick_width - brick_spacing
        # 要怎麼固定在位置上
        onmousemoved(self.paddle_move)
        onmouseclicked(self.leave_original_position)

    def leave_original_position(self, m):
        if self.ball.x == (self.window_width - self.r * 2) / 2 and self.ball.y == (self.window_height - self.r * 2) / 2:
            self.ball.move(self.__dx, self.__dy)
        # self.__dx = random.randint(1, MAX_X_SPEED)
        # self.__dy = INITIAL_Y_SPEED
        # if random.random() > 0.5:
        #     self.__dx = - self.__dx

    def reset_ball(self):
        # self.set_ball_position()
        """while self.ball_at_brick():
            self.set_ball_position()
        self.set_ball_velocity()"""
        self.window.add(self.ball, x =(self.window_width - self.r * 2) / 2, y =(self.window_height - self.r * 2) / 2)
    #
    # def set_ball_position(self):
    #     self.ballx = (self.window_width - BALL_RADIUS * 2) / 2
    #     self.bally = (self.window_height - BALL_RADIUS * 2) / 2
    #     self.ball.x = self.ballx
    #     self.ball.y = self.bally

    def paddle_move(self, m):
        self.paddle.color = True
        self.paddle.filled = 'black'
        self.window.add(self.paddle, m.x-self.paddle.width/2, self.window_height - PADDLE_OFFSET)

    # 知道codder端的資訊 只要是private都要getter
    def getter__dx(self):
        return self.__dx

    def getter__dy(self):
        return self.__dy

    def detect_reflect(self):
        # 寫一個method 沒有在其他地方用 就放在method
        r = BALL_RADIUS
        a = self.window.get_object_at(self.ball.x, self.ball.y)
        b = self.window.get_object_at(self.ball.x+2*r, self.ball.y)
        c = self.window.get_object_at(self.ball.x+2*r, self.ball.y+2*r)
        d = self.window.get_object_at(self.ball.x, self.ball.y+2*r)
        if a is not None and a is not self.paddle and a is not score_label:
            self.window.remove(a)
            self.__dy = -self.__dy
        elif b is not None and b is not self.paddle and b is not score_label:
            self.window.remove(b)
            self.__dy = -self.__dy
        elif c is not None and c == self.paddle:
            self.__dy = -abs(self.__dy)
        elif d is not None and d == self.paddle:
            self.__dy = -abs(self.__dy)





    def meet_wall(self):
        if self.ball.x <= 0 or self.ball.x > self.window_width - self.r:
            self.__dx = -self.__dx
        elif self.ball.y <= 0:
            self.__dy = -self.__dy




























