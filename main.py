import time
from fir import FIR
from pygamegui import firGui
from ai import AIRand, AIDefender

def main():

    # init model and gui
    size = 7

    s1 = ['B', 'W']
    s2 = ['Black win!', 'White win!']

    fir = FIR(size)
    gui = firGui(size, fir)

    # init ai
    ai1 = AIDefender(2, fir)

    # init players list
    player = [gui.run, ai1.run]
    ais = [ai1]
    
    # main loop
    while True:

        gui.draw_board()

        while True:

            index = fir.turn - 1

            print(s1[index])

            result = player[index]()
            gui.draw_board()

            if result == 2:
                print(s2[index])
                gui.draw_win()
                break

            time.sleep(0.05)

        gui.run()

        # re start
        fir.clear()
        for a in ais:
            a.reset()
        print('New')


if __name__ == "__main__":

    main()
