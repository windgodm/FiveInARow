from fir import FIR
from pygamegui import FirGui
from ai import AIRand, AIDefender1, AIDefender2, AIDefender3

def main():

    # init model and gui
    size = 15

    s1 = ['B', 'W']
    s2 = ['Black win!', 'White win!']

    fir = FIR(size)
    gui = FirGui(size, fir)

    # read
    with open('config.txt', 'r') as f:
        s = [int(x) for x in f.read().split()]

    # ready init ai
    ai_init = [AIRand, AIDefender1, AIDefender2, AIDefender3]

    # init players list
    player = []
    ais = []
    for i in range(2):
        x = s[i]
        if x == -1:
            player.append(gui.run)
        else:
            ai = ai_init[x](i+1, fir)
            player.append(ai.run)
            ais.append(ai)
    
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
