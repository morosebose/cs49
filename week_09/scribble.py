"""
scribble.py

Draw a circle wherever the mouse pointer is on the canvas.

Programmer: Surajit A. Bose, Date: 2024.06.07
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def scribble():
    """Draw a circle in a random color wherever mouse is on the canvas."""
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # if mouse is on canvas
        if mouse_x < CANVAS_WIDTH and \
            mouse_y < CANVAS_HEIGHT and \
            mouse_x > 0 and mouse_y > 0:

            canvas.create_oval(mouse_x, mouse_y, mouse_x + CIRCLE_SIZE,
                mouse_y + CIRCLE_SIZE, random_color())
        time.sleep(DELAY)

def random_color():
    """Return a random color from list of colors."""
    colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
    return random.choice(colors)

if __name__ == "__main__":
    main()