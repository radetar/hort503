class cell:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        return str(self.state)

    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state

def test_cell(x,y,state):
    tcell = cell(x,y,state)
    print(tcell.get_state())
    tcell.set_state(X)
    print(tcell.get_state())
