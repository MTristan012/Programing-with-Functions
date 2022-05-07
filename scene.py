# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random

from datetime import datetime

from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    dt = datetime.now()
    dt = dt.hour
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_wall(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height, dt)
    draw_grass(canvas, scene_width, scene_height)
    draw_path(canvas, scene_width, scene_height)
    draw_tree(canvas, scene_width, scene_height)
    draw_out_my_window(canvas)
    draw_lantern(canvas, dt)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_wall(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, width=0, fill="snow1")

def draw_sky(canvas, scene_width, scene_height, dt):
    if dt >= 8 and dt <= 18:
        draw_rectangle(canvas, 100, 100, scene_width, scene_height, width=0, fill="dodgerBlue1")
    elif dt >= 6 and dt < 8:
        draw_rectangle(canvas, 100, 100, scene_width, scene_height, width=0, fill="goldenrod1")
    elif dt >= 18 and dt < 20:
        draw_rectangle(canvas, 100, 100, scene_width, scene_height, width=0, fill="red2")
    else:
        draw_rectangle(canvas, 100, 100, scene_width, scene_height, width=0, fill="grey20")

def draw_grass(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 100, 100, scene_width, scene_height / 4, width=0, fill="springGreen1")
    draw_rectangle(canvas, 100, 140, scene_width, scene_height / 2.5, width=0, fill="springGreen1")

def draw_path(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 100, 120, scene_width, scene_height / 3, width=0, fill="seashell")

def draw_tree(canvas, scene_width, scene_height):
   draw_rectangle(canvas, 650, 180, 700, 320, width = 0, fill = "maroon")
   half_height = round(scene_height/.20)
   min_diam = 15
   max_diam = 30
   for i in range(5000):
       x = random.randint(600, scene_width - 75)
       y = random.randint(300, half_height)
       diameter = random.randint(min_diam, max_diam)
       draw_oval(canvas, x, y, x + diameter, y + diameter, fill="darkGreen")

def draw_lantern(canvas, dt):
    draw_rectangle(canvas, 150, 110, 170, 320, width=0, fill="black")
    if dt >= 8 and dt <= 20:
        draw_rectangle(canvas, 140, 320, 180, 350, width=0, fill="ivory1")
    else:
        draw_rectangle(canvas, 140, 320, 180, 350, width=0, fill="yellow1")
    x0 = 140
    y0 = 330
    x1 = 180
    y1 = 370
    draw_arc(canvas, x0, y0, x1, y1, start=0, extent=180, width=1, outline="black", fill="black")

def draw_sun(canvas, scene_width, scene_height):
    print()

def draw_out_my_window(canvas):
    center_x = 400
    center_y = 50
    text = "Out of my Window"
    draw_text(canvas, center_x, center_y, text, fill="black")
# Call the main function so that
# this program will start executing.
main()
