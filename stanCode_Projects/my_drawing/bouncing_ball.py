"""
File: 
Name:
-------------------------
TODO:
1. Setting what the ball is look like?
2. Giving a condition that when the ball stars move
and setting a switch
3.hen setting a for loop and giving them condition
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
playtime = 0
moving = 0
vs = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ballshape()
    onmouseclicked(movingball)


# moving = 0 不動

def movingball(m):
    global playtime, moving, vs
    if playtime < 3 and moving == 0:
        moving = 1
        while True:
            ball.move(VX, vs)
            if ball.y >= window.height:
                vs *= REDUCE
                vs = -vs
            elif ball.x >= window.width:
                vs = 0
                moving = 0
                playtime += 1
                print(playtime)
                window.add(ball, x=START_X, y=START_Y)
                break
            vs += GRAVITY
            pause(10)




def ballshape():
    window.add(ball, x=START_X, y=START_Y)
    ball.filled = True
    ball.fill_color = 'black'



if __name__ == "__main__":
    main()
