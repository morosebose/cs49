"""
highlight_mouse.py

Draw a highlight box wherever the mouse pointer is on the canvas.

Programmer: Surajit A. Bose, Date: 2024.06.07
"""
from graphics import Canvas

CANVAS_SIZE = 500
SQUARE_SIZE = 40
DELAY = 0.01

def highlight_mouse():
    """"Surround mouse pointer with a highlighted box when it is on canvas"""
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    square = canvas.create_rectangle(0, 0, SQUARE_SIZE,
 		SQUARE_SIZE, 'pink')
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(square, mouse_x - SQUARE_SIZE / 2, 
            mouse_y - SQUARE_SIZE / 2)
        time.sleep(DELAY)

if __name__ == '__main__':
    highlight_mouse()
