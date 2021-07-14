from tkinter import Tk, Canvas
from geom2d import Point, Circle, AffineTransform
from graphic.simulation.draw import CanvasDrawing
from graphic.simulation.loop import main_loop
tk=Tk()
tk.title('Hello Motion')

canvas = Canvas(tk, width= 600, height=600)
canvas.grid(row=0, column=0)

max_frames=100

transform = AffineTransform(sx=1, sy=1, tx=0, ty=0, shx=0, shy=0)
drawing = CanvasDrawing(canvas, transform)
circle= Circle(Point(300,300), 0)

def update_sys(delta_time, time, frame):
    circle.radius = (circle.radius+15)%450
    tk.update()

def redraw():
    drawing.clear()
    drawing.draw_circle(circle, 50)

def should_continue(frame, time):
    return frame <= max_frames

main_loop(update_sys, redraw, should_continue)
tk.mainloop()