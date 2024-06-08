from cell import Cell
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            row = list()
            for j in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)       

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False    

    def _draw_cell(self, i, j):
        if self._win == None: 
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win == None: 
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # find possible directions
            top = self._get_top_direction(i,j)
            if top is not None and not top[0].visited:
                to_visit.append(top)

            left = self._get_left_direction(i,j)
            if left is not None and not left[0].visited:
                to_visit.append(left)

            bottom = self._get_bottom_direction(i,j)
            if bottom is not None and not bottom[0].visited:
                to_visit.append(bottom)

            right = self._get_right_direction(i,j)
            if right is not None and not right[0].visited:
                to_visit.append(right)
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            random_direction = random.choice(to_visit)

            if random_direction[1] == 't':
                #break down my top and its bottom
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)

            if random_direction[1] == 'b':
                #break down my top and its bottom
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j + 1)

            if random_direction[1] == 'l':
                #break down my top and its bottom
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)

            if random_direction[1] == 'r':
                #break down my top and its bottom
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)

    def _get_top_direction(self, i, j):
        if j > 0:
            return self._cells[i][j-1], 't'
        else:
            return None

    def _get_bottom_direction(self, i, j):
        if j < self._num_rows - 1:
            return self._cells[i][j+1], 'b'
        else:
            return None

    def _get_left_direction(self, i, j):
        if i > 0:
            return self._cells[i-1][j], 'l'
        else:
            return None

    def _get_right_direction(self, i, j):
        if i < self._num_cols - 1:
            return self._cells[i+1][j], 'r'
        else:
            return None

    def solve(self):
        self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i < 0 or j < 0:
            print("waagh")
            return False

        # Test for end cell (could there be another exit?)
        print(f"i: {i}, num_cols -1 {self._num_cols-1}, j: {j}, num_rows -1 {self._num_rows-1}")
        if i == self._num_cols - 1 and j == self._num_rows -1:
            return True

        # Test all 4 directions
        if not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            solved = self._solve_r(i+1,j)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        if not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            solved = self._solve_r(i,j+1)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        if not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            solved = self._solve_r(i-1,j)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        if not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            solved = self._solve_r(i,j-1)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        return False
