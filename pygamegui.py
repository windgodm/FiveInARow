import pygame
import sys

class FirGui():

    def __init__(self, size, gobang):

        pygame.init()

        self.border = 60
        self.cell_size = 40
        self.chess_size = 16
        self.size = size
        self.grid_size = self.cell_size * (size - 1) + self.border * 2
        self.bottom = self.cell_size*(size-1)+self.border

        self.background_color = (0x80, 0x80, 0xc0)
        self.background_color2 = (0x90, 0x90, 0xd0)
        self.line_color = (0xc0, 0xc0, 0xc0)
        self.black_color = (0x20, 0x20, 0x20)
        self.white_color = (0xe0, 0xe0, 0xe0)

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.screencaption = pygame.display.set_caption('Gobang by yssf')
        self.screen = pygame.display.set_mode((self.grid_size, self.grid_size))
        self.clock = pygame.time.Clock()

        self.model = gobang


    def draw_board(self):

        # draw board
        self.screen.fill(self.background_color)
        for x in range(0, self.cell_size * self.size, self.cell_size):
            pygame.draw.line(self.screen, self.line_color, (x+self.border, self.border), (x+self.border, self.bottom))
        for y in range(0, self.cell_size * self.size, self.cell_size):
            pygame.draw.line(self.screen, self.line_color, (self.border, y+self.border), (self.bottom, y+self.border))

        # draw cell
        y = self.border
        for row in self.model.board:
            x = self.border
            for color in row:
                if color == 0:
                    pass
                elif color == 1:
                    pygame.draw.circle(self.screen, self.black_color, [x, y], self.chess_size, self.chess_size)
                else:
                    pygame.draw.circle(self.screen, self.white_color, [x, y], self.chess_size, self.chess_size)
                x += self.cell_size
            y += self.cell_size

        pygame.display.update()


    def draw_win(self):

        if self.model.winner == 1:
            s = 'Black win!'
        else:
            s = 'White win!'
        textsurface = self.myfont.render(s, False, (0, 0, 0))
        pygame.draw.rect(self.screen, self.background_color2, (5, 5, 165, 45))
        self.screen.blit(textsurface, (10, 5))

        pygame.display.update()


    def game_loop(self):

            # message

            result = 1

            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    x = int((x - self.border) / self.cell_size + 0.5)
                    y = int((y - self.border) / self.cell_size + 0.5)
                    result = self.model.move(y, x)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # return

            return result


    def after_loop(self):

        click_win = False

        # message

        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if x >= 5 and x <= 165 and y >= 5 and y <= 45:
                    click_win = True

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #

        if not click_win:
            return 1

        return 0


    def run(self):

        result = 1

        while True:

            self.clock.tick(20)

            if self.model.winner:
                result = self.after_loop()
            else:
                result = self.game_loop()

            # if move or win, break and wait
            if result != 1:
                return result
