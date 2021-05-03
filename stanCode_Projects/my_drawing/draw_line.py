"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# It controls the width and height of the rect
SIZE = 10

# Global Variable
window = GWindow(title='drawline')

"""1. How to record the starting point(x1,y1) ?
        - setting variable(x1,y1)
    2. how to divide twp situation
        -if else
    3. when they finish that how can we reset?
        - give them specific number to represent
    4. But how to let circle disapperd?
        - remove(hole)?? why is the first?
        """

click_number = 0
hole = GOval(SIZE, SIZE)
hole.color = 'black'
x1 = 0
y1 = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(line)



def line(m):
    global click_number, x1, y1
    window.remove(hole)
    if click_number == 0:
        # 存位置
        x1 = m.x
        y1 = m.y
        # 如何跳到下一步
        click_number = 1
        window.add(hole, x=m.x - SIZE / 2, y=m.y - SIZE / 2)
    else:
        # 存位置 舊的箱子依然存在
        x2 = m.x
        y2 = m.y
        line_l = GLine(x1, y1, x2, y2)
        window.add(line_l)
        click_number = 0

















if __name__ == "__main__":
    main()
