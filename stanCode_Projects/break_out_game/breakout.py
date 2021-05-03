"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    while True:
        if graphics.ball.x != (graphics.window_width - graphics.r * 2) / 2 and graphics.ball.y != (graphics.window_height - graphics.r * 2) / 2:
            vx = graphics.getter__dx()
            vy = graphics.getter__dy()
            graphics.ball.move(vx, vy)
            # graphics.detect_reflect()
            graphics.meet_wall()
            graphics.detect_reflect()
            pause(FRAME_RATE)



    # Add animation loop here!


if __name__ == '__main__':
    main()
