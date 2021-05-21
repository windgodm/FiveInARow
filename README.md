# FiveInARow

## Abstract

FiveInARow(Gomoku, Gobang, 五子棋)

Build with python and pygame.

With some simple AI without machine learning.

## About project file

fir.py: (class **FIR**)FIR core logic.

pygamegui.py: (class **FirGui**)The code of UI. Based on class FIR in fir.py.

main.py: An example of using the class **FirGui** in pygamegui.py and adding robot players.

ai.py: Some simple AI.

FirDefender1.py: A class used to calculate the risk value (The opponent's possible benefit). And give the most dangerous location (The location where the opponent may benefit the most ). 

FirDefender2.py: Reference class **FirDefender1**. Optimize the calculation method of risk value.

1. Add double case.

2. Add special case judgment.

FirDefender3.py: Reference class **FirDefender2**. Optimize the calculation method of risk value.

1. Remove special case judgment.
2. Allows custom dangerous level and multiples.

## todo

Add heuristically DFS. FirDefender will be used as a reference for heuristic. Since there is currently only one heuristic reference, it may be highly coupled. 

Maybe use stochastic descent to optimize the dangerous level.

