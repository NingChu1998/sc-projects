"""
File: sierpinski.py
Name: Julie
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6          # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
w = 0.5
h = 0.866

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)



def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order:
	:param length:
	:param upper_left_x:
	:param upper_left_y:
	:return:

	1. Construct the base line which is Order 1
	2. Recurring the Order 2 (*Follow the pattern of upper left triangle-- What is its length?, any similar point?)
	3.
	"""
	if order == 0:
		pass
	else:

		tri_left = GLine(upper_left_x, upper_left_y, upper_left_x + w*length, upper_left_y+h*length)
		tri_mid = GLine(upper_left_x + w*length, upper_left_y+h*length, upper_left_x+length, upper_left_y)
		tri_right = GLine(upper_left_x+length, upper_left_y, upper_left_x, upper_left_y)
		window.add(tri_left)
		window.add(tri_mid)
		window.add(tri_right)
		pause(1000)

		# upper left
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# middle
		sierpinski_triangle(order - 1, length / 2, upper_left_x + w * length/2, upper_left_y + h * length/2)
		# upper right
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length/2, upper_left_y)







if __name__ == '__main__':
	main()
