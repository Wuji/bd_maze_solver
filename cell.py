from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True 
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window
        self.visited = False

    def get_center(self):
        return Point((self._x1+self._x2) / 2, (self._y1+self._y2) / 2)

    def draw(self, x1, y1, x2, y2): 

        if self._window == None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        no_wall_color = "white"

        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(left_wall)
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(left_wall, no_wall_color)

        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(top_wall)
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(top_wall, no_wall_color)

        if self.has_right_wall:
            right_wall = Line(Point(x2,y1), Point(x2, y2))
            self._window.draw_line(right_wall)
        else:
            right_wall = Line(Point(x2,y1), Point(x2, y2))
            self._window.draw_line(right_wall, no_wall_color)

        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2,y2))
            self._window.draw_line(bottom_wall)
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2,y2))
            self._window.draw_line(bottom_wall, no_wall_color)

    def draw_move(self, to_cell, undo=False):
        if not undo:
            color = "red"
        else:
            color = "grey"


        my_center_x = abs(self._x2 - self._x1) // 2 + self._x1
        my_center_y = abs(self._y2 - self._y1) // 2 + self._y1

        to_center_x = abs(to_cell._x2 - to_cell._x1) // 2 + to_cell._x1
        to_center_y = abs(to_cell._y2 - to_cell._y1) // 2 + to_cell._y1

        line = Line(Point(my_center_x, my_center_y), Point(to_center_x, to_center_y))
        self._window.draw_line(line, color)
     
