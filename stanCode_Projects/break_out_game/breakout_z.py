"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_z import BreakoutGraphics
from campy.graphics.gobjects import GLabel
from campy.graphics.gwindow import GWindow


FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts



def main():
    live = NUM_LIVES
    graphics = BreakoutGraphics()
    graphics.set_ball_position()
    while live > 0:
        #if graphics.ball.x != (graphics.window_width - graphics.r * 2) / 2 or graphics.ball.y != (graphics.window_height - graphics.r * 2) / 2:
        vx = graphics.getter__dx()
        vy = graphics.getter__dy()
        graphics.ball.move(vx, vy)
        graphics.meet_wall()
        graphics.detect_reflect()
        if graphics.ball.y >= graphics.window_height:
            graphics.reset_ball()
            live -= 1
        pause(FRAME_RATE)
    graphics.back_home()




    # Add animation loop here!


if __name__ == '__main__':
    main()
