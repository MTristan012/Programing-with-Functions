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
    draw_window(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height, dt)
    draw_sun(canvas, scene_width, scene_height, dt)
    draw_cloud(canvas)
    draw_grass(canvas, scene_width, scene_height)
    draw_path(canvas, scene_width, scene_height)
    draw_temple(canvas)
    draw_tree(canvas, scene_width, scene_height)
    draw_a_chat(canvas)
    draw_out_my_window(canvas)
    draw_lantern(canvas, dt)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_wall(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, width=0, fill="snow1")

def draw_window(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 90, 90, scene_width, scene_height, width=2, fill="wheat4")

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
    if dt >= 7 and dt <= 19:
        draw_rectangle(canvas, 140, 320, 180, 350, width=0, fill="ivory1")
    else:
        draw_rectangle(canvas, 140, 320, 180, 350, width=0, fill="yellow1")
    x0 = 140
    y0 = 330
    x1 = 180
    y1 = 370
    draw_arc(canvas, x0, y0, x1, y1, start=0, extent=180, width=1, outline="black", fill="black")

def draw_sun(canvas, scene_width, scene_height, dt):
    if dt >= 8 and dt <= 18:
        for i in range(200,600):
            x = random.randint(350, scene_width - 400)
            y = random.randint(350, scene_height - 100)
            diameter = 100
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="gold1")
    elif dt >= 6 and dt < 8:
        x0 = 0
        y0 = 100
        x1 = 200
        y1 = 280
        draw_arc(canvas, x0, y0, x1, y1, start=0, extent=90, width=1, outline="gold4", fill="white")
    elif dt >= 18 and dt < 20:
        x0 = 900
        y0 = 100
        x1 = 700
        y1 = 280
        draw_arc(canvas, x0, y0, x1, y1, start=90, extent=90, width=1, outline="white", fill="gold2")
    else:
        for i in range(200, 600):
            x = random.randint(350, scene_width - 400)
            y = random.randint(350, scene_height - 100)
            diameter = 100
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="white")


def draw_temple(canvas):
    x0 = 100
    y0 = 140
    x1 = 800
    y1 = 250
    draw_arc(canvas, x0, y0, x1, y1, start=0, extent=180, width=1, outline="grey31", fill="aquamarine4")
    draw_rectangle(canvas, 390, 250, 420, 370, width=1, outline="black", fill="lightCyan1")
    x0 = 390
    y0 = 370
    x1 = 405
    y1 = 390
    x2 = 420
    y2 = 370
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, outline="black", fill="lightCyan1")
    draw_rectangle(canvas, 420, 250, 440, 330, width=1, outline="black", fill="lightCyan1")
    draw_rectangle(canvas, 440, 250, 470, 400, width=1, outline="black", fill="lightCyan1")
    x0 = 440
    y0 = 400
    x1 = 455
    y1 = 430
    x2 = 470
    y2 = 400
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, outline="black", fill="lightCyan1")
    draw_rectangle(canvas, 470, 250, 490, 330, width=1, outline="black", fill="lightCyan1")
    draw_rectangle(canvas, 490, 250, 520, 370, width=1, outline="black", fill="lightCyan1")
    x0 = 490
    y0 = 370
    x1 = 505
    y1 = 390
    x2 = 520
    y2 = 370
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, outline="black", fill="lightCyan1")

def draw_a_chat(canvas):
    x0 = 505 - 10
    y0 = 159 - 10
    x1 = 500 - 10
    y1 = 185 - 10
    x2 = 520 - 10
    y2 = 155 - 10
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, outline="black", fill="black")
    x0 = 535 - 10
    y0 = 159 - 10
    x1 = 540 - 10
    y1 = 185 - 10
    x2 = 520 - 10
    y2 = 155 - 10
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=1, outline="black", fill="black")
    x0 = 505 - 10
    y0 = 140 - 10
    x1 = 535 - 10
    y1 = 170 - 10
    draw_oval(canvas, x0, y0, x1, y1, width=1, outline="black", fill="gray50")
    x0 = 500 - 10
    y0 = 110 - 10
    x1 = 540 - 10
    y1 = 150 - 10
    draw_oval(canvas, x0, y0, x1, y1, width=1, outline="black", fill="gray50")
    x0 = 490
    y0 = 95
    x1 = 535
    y1 = 105
    draw_arc(canvas, x0, y0, x1, y1, start=0, extent=90, width=1, outline="black", fill="gray50")

def draw_cloud(canvas):
    x0 = 200
    y0 = 400
    x1 = 240
    y1 = 450
    r = random.randint(1, 30)
    draw_oval(canvas, x0, y0, x1, y1, width=5, fill="snow2")
    x0 = 200 + r
    y0 = 400 + r
    x1 = 240 + r
    y1 = 450 + r
    draw_oval(canvas, x0, y0, x1, y1, width=3, fill="snow2")
    x0 = 200 - r
    y0 = 400 - r
    x1 = 240 - r
    y1 = 450 - r
    draw_oval(canvas, x0, y0, x1, y1, width=3, fill="snow2")
    x0 = 220 - r
    y0 = 400 - r
    x1 = 260 - r
    y1 = 450 - r
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="snow2")
    x0 = 220 + r
    y0 = 400 + r
    x1 = 260 + r
    y1 = 450 + r
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="snow2")

def draw_out_my_window(canvas):
    center_x = 400
    center_y = 50
    text = "Outside the Window by MTristan"
    draw_text(canvas, center_x, center_y, text, fill="black")
# Call the main function so that
# this program will start executing.
main()
