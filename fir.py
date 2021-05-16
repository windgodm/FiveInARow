class FIR():

    def __init__(self, size):

        self.size = size
        self.board = [[0 for col in range(size)] for raw in range(size)]
        self.turn = 1
        self.winner = 0
        self.last_move = [-1, -1] # row, col

    def clear(self):

        
        self.board = [[0 for col in range(self.size)] for raw in range(self.size)]
        self.turn = 1
        self.winner = 0

    def subcheck(self, color, raw, col, drc):

        dr = drc[0]
        dc = drc[1]
        for i in range(5):
            if raw < 0 or raw == self.size:
                break
            if col < 0 or col == self.size:
                break
            if self.board[raw][col] != color:
                break

            raw += dr
            col += dc
        else:
            return True

        return False

    def check(self, color, raw, col):

        # up, down, left, right, ul, ur, dl, dr
        drcs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        for drc in drcs:
            if self.subcheck(color, raw, col, drc):
                return True

        return False

    '''
    return:
    0: move success
    1: move fail
    2: move success and win
    '''
    def move(self, raw, col):

        # move
        if self.board[raw][col] == 0:
            self.board[raw][col] = self.turn
            self.last_move[0] = raw
            self.last_move[1] = col
        else:
            return 1

        # check
        if(self.check(self.turn, raw, col)):
            self.winner = self.turn
            return 2

        # switch
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

        return 0
