import time
from fir import FIR
from pygamegui import FirGui
from ai import AIRand, AIDefender1, AIDefender2

def main():

    # init model and gui
    size = 7

    s1 = ['B', 'W']
    s2 = ['Black win!', 'White win!']

    fir = FIR(size)
    gui = FirGui(size, fir)

    # init ai
    # ai1 = AIDefender1(1, fir)
    ai2 = AIDefender2(2, fir)

    # init players list
    player = [gui.run, ai2.run]
    ais = [ai2]
    
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

            # time.sleep(0.5)

        gui.run()

        # re start
        fir.clear()
        for a in ais:
            a.reset()
        print('New')


if __name__ == "__main__":

    main()
