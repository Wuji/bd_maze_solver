from tkinter import Tk, BOTH, Canvas
from tkinter import ttk

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2 ):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Window:
    def __init__(self, width, heigth):
        self.root_widget = Tk()
        self.root_widget.title("A Maze Solver")
        # self.mainframe = ttk.Frame(self.root_widget)
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root_widget, bg="white", height=heigth, width=width)
        # TODO change for more modern approach
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()


    def wait_for_close(self):
        self.window_running = True

        while self.window_running:
            self.redraw()


    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

