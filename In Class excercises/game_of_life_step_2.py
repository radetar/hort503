from game_of_life_step_1 import cell

class grid:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.grid_list = list()

        for r in range(rows):
            row_list= list()
            for c in range(cols) :
                col_list = cell(r,c, 'X')
                row_list.append(col_list)
            self.grid_list.append(row_list)

    def print_thingy(self):
        for x in self.grid_list:
            # print(x, "\n")
            for blah in x:
                print(blah)
        # print(self.grid_list)

    #def next_move(self):

    #def play(self,ticks):

test = grid(10,10)
test.print_thingy()
