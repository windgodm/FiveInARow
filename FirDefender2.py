class FirDefender2():

    def __init__(self, color, fir):

        self.drcs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]

        self.color = color
        if color == 1:
            self.dcolor = 2
        else:
            self.dcolor = 1

        self.model = fir
        self.dangers = [[0 for c in range(fir.size)] for r in range(fir.size)]

    def reset(self):
        
        # wa
        self.dangers = [[0 for c in range(self.model.size)] for r in range(self.model.size)]

    def update_op(self):

        n = self.model.size - 1
        row = self.model.last_move[0]
        col = self.model.last_move[1]

        self.dangers[row][col] = 0

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

            a1 = self.model.board[y1][x1]
            a2 = self.model.board[y2][x2]

            # 3 special case
            d = d1 + d2 + 1
            if d == 3: # case 1
                if a1 == 0 and a2 == 0:
                    self.dangers[y1][x1] += 1100
                    self.dangers[y2][x2] += 1100
                    continue
            elif d == 4: # case 2
                if a1 == 0:
                    self.dangers[y1][x1] += 2100
                if a2 == 0:
                    self.dangers[y2][x2] += 2100
                continue

            # 4
            if a1 == 0:
                if a2 == 0:
                    self.dangers[y1][x1] += (d2 + 1) * 2
                else:
                    self.dangers[y1][x1] = self.dangers[y1][x1] // 2 + (d2 + 1)
            if a2 == 0:
                if a1 == 0:
                    self.dangers[y2][x2] += (d1 + 1) * 2
                else:
                    self.dangers[y2][x2] = self.dangers[y2][x2] // 2 + (d1 + 1)

    def update_my(self):

        n = self.model.size - 1
        r = self.model.last_move[0]
        c = self.model.last_move[1]
        self.dangers[r][c] = 0

        for drc in self.drcs:
            y, x = r, c
            y += drc[0]
            x += drc[1]
            d = 0
            while y >= 0 and y <= n and x >= 0 and x <= n:
                if self.model.board[y][x] == self.dcolor:
                    y += drc[0]
                    x += drc[1]
                    d += 1
                else:
                    break
            else:
                y -= drc[0]
                x -= drc[1]

            # special case
            danger = self.dangers[y][x]
            if danger >= 1000:
                if danger < 2000: # case 1
                    self.dangers[y][x] -= 1100
                else: # case 2
                    self.dangers[y][x] -= 2100

            self.dangers[y][x] -= d


    def suggest(self):

        n = self.model.size - 1
        y = int(n / 2)
        x = int(n / 2)
        maxd = 0
        for r in range(self.model.size):
            for c in range(self.model.size):
                if self.dangers[r][c] > maxd:
                    maxd = self.dangers[r][c]
                    y, x = r, c
        
        return y, x
