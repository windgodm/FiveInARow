from random import randint
from FirDefender1 import FirDefender1
from FirDefender2 import FirDefender2


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


class AIDefender1():

    def __init__(self, color, fir):

        # u, d, l, r, ul, dr, ur, dl
        self.drcs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]

        self.color = color
        if color == 1:
            self.dcolor = 2
        else:
            self.dcolor = 1
        self.model = fir
        
        self.fir_defender = FirDefender1(color, fir)

    def reset(self):
        
        self.fir_defender.reset()
        

    def run(self):

        result = 1

        # update defender
        row = self.model.last_move[0]
        if row != -1:
            self.fir_defender.update_op()

        # get best ans
        y, x = self.fir_defender.suggest()
        
        # move
        result = self.model.move(y, x)

        # update defender
        if result == 0:
            self.fir_defender.update_my()

        return result


class AIDefender2():

    def __init__(self, color, fir):

        # u, d, l, r, ul, dr, ur, dl
        self.drcs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]

        self.color = color
        if color == 1:
            self.dcolor = 2
        else:
            self.dcolor = 1
        self.model = fir
        
        self.fir_defender = FirDefender2(color, fir)

    def reset(self):
        
        self.fir_defender.reset()
        

    def run(self):

        result = 1

        # update defender
        row = self.model.last_move[0]
        if row != -1:
            self.fir_defender.update_op()

        # get best ans
        y, x = self.fir_defender.suggest()
        
        # move
        result = self.model.move(y, x)

        # update defender
        if result == 0:
            self.fir_defender.update_my()

        return result
