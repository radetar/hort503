# This script is a solution for the in-class assignment for
# weeks 4 and 5.
#
import numpy as np
class cell(object):


class grid(object):
    # The grid class serves as the grid for the conway game of life. It
    # consists of an nxm matrix of cells.


    def __init__(self, rows, cols):
        # Intialize the grid to the size requested by the end-user.
        # Fill each cell of the grid with a a cell object and
        # set its default tate to off.
        self.rows = rows
        self.cols = cols
        self.grid = []
        for i in range(0, rows):
            col_list = []
            for j in range(0, cols):
                col_list.append(cell(i, j, 0))
            self.grid.append(col_list)
        self = np.zeros((self.rows, self.cols))
        self.rows = rows
        self.cols = cols
    def print(self):
        # Print the grid to the screen.
        print(self.grid)


    def set_cell(self, x, y, state):
        # Sets any cell within the grid, using an x,y coordinate, to the
        # state requested by the caller.
        self.grid[x][y] = state

    def get_cell(self,x,y):
        return self.grid[x][y]

    def next_move(self):

        curr_state = np.copy(self.grid)

            for i in range(1, self.rows - 1):
                for j in range(1, self.cols - 1):
                    # Get the state of this cell and it's 8 neighbors.
                    nw = curr_state[i-1][j-1]
                    n = curr_state[i-1][j]
                    ne = curr_state[i-1][j+1]
                    w = curr_state[i][j-1]
                    me = curr_state[i][j]
                    e = curr_state[i][j+1]
                    sw = curr_state[i+1][j-1]
                    s = curr_state[i+1][j]
                    se = curr_state[i+1][j+1]

                # Calculate the number of neighbors that are live.
                num_neighbors = ne + n + nw + e + w + se + s + sw

                # Any live cell with fewer than two live neighbours dies, as if
                # caused by underpopulation.
                if num_neighbors < 2 and me == 1:
                    self.grid[i][j].set_state(0)
                # Any live cell with two or three live neighbours lives on to
                # the next generation.
                elif (num_neighbors == 2 or num_neighbors == 3) and me == 1:
                    self.grid[i][j].set_state(1)
                # Any live cell with more than three live neighbours dies, as
                # if by overpopulation.
                elif num_neighbors > 3 and me == 1:
                    self.grid[i][j].set_state(0)
                # Any dead cell with exactly three live neighbours becomes a
                # live cell, as if by reproduction.
                elif num_neighbors == 3 and me == 0:
                    self.grid[i][j].set_state(1)

    def play(self, ticks = 100):
        for i in range(0, ticks):
            print(f"Step {i+1}")
            self.next_move()
            self.print()

    def demo1(self, ticks = 100):
        # Provides an initial set of cells.
        self.set_cell(14, 40, 1)
        self.set_cell(15, 42, 1)
        self.set_cell(16, 39, 1)
        self.set_cell(16, 40, 1)
        self.set_cell(16, 43, 1)
        self.set_cell(16, 44, 1)
        self.set_cell(16, 45, 1)
        self.play(ticks)

def test_grid():
    # A unit test to make sure our grid is working.
    temp_grid = grid(30, 80)
    temp_grid.set_cell(29, 79, 1)
    temp_grid.print()
    # TODO: add a test for the grid.


#test_cell()
#test_grid()

# Intialize our grid, add some cells that are turned on and then
# play
gofl = grid(30, 80)
gofl.demo1()
