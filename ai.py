from random import randint


class AIRand():

    def __init__(self, color, fir):

        self.color = color
        self.model = fir

    def reset(self):
        
        pass
        

    def run(self):

        result = 1
        n = self.model.size - 1

        while result == 1:

            x = randint(0, n)
            y = randint(0, n)
            result = self.model.move(y, x)

        return result


class AIDefender():

    def __init__(self, color, gobang):

        # u, d, l, r, ul, dr, ur, dl
        self.drcs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]

        self.color = color
        if color == 1:
            self.dcolor = 2
        else:
            self.dcolor = 1
        self.model = gobang
        self.danger = [[0 for c in range(gobang.size)] for r in range(gobang.size)]

    def reset(self):
        
        self.danger = [[0 for c in range(self.model.size)] for r in range(self.model.size)]
        

    def run(self):

        result = 1
        n = self.model.size - 1

        # update danger
        row = self.model.last_move[0]
        if row != -1:
            col = self.model.last_move[1]

            self.danger[row][col] = 0

            for i in range(0, 8, 2):
                # 1
                drc = self.drcs[i]
                y1, x1 = row, col
                y1 += drc[0]
                x1 += drc[1]
                d1 = 0
                while y1 >= 0 and y1 <= n and x1 >= 0 and x1 <= n:
                    if self.model.board[y1][x1] == self.dcolor:
                        y1 += drc[0]
                        x1 += drc[1]
                        d1 += 1
                    else:
                        break
                else:
                    y1 -= drc[0]
                    x1 -= drc[1]
                # 2
                drc = self.drcs[i+1]
                y2, x2 = row, col
                y2 += drc[0]
                x2 += drc[1]
                d2 = 0
                while y2 >= 0 and y2 <= n and x2 >= 0 and x2 <= n:
                    if self.model.board[y2][x2] == self.dcolor:
                        y2 += drc[0]
                        x2 += drc[1]
                        d2 += 1
                    else:
                        break
                else:
                    y2 -= drc[0]
                    x2 -= drc[1]

                # 3
                if self.model.board[y1][x1] == 0:
                    self.danger[y1][x1] += d2 + 1
                if self.model.board[y2][x2] == 0:
                    self.danger[y2][x2] += d1 + 1

        # get best ans
        y = int(n / 2)
        x = int(n / 2)
        maxd = 0
        for r in range(self.model.size):
            for c in range(self.model.size):
                if self.danger[r][c] > maxd:
                    maxd = self.danger[r][c]
                    y, x = r, c
        
        # move
        self.danger[y][x] = 0
        result = self.model.move(y, x)

        return result

