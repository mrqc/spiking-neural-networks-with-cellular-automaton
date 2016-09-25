import sys
import copy
import time
import random
import automaton

# custom mutation function
def gameOfLifeCell(row, column):
    area = []
    current = automaton.world[row][column]
    if current != -1:
        for sliceRow in range(row - 1, row + 2):
            for sliceColumn in range(column - 1, column + 2):
                if sliceRow >= 0 and sliceRow < automaton.worldHeight and sliceColumn >= 0 and sliceColumn < automaton.worldWidth:
                    if not (row == sliceRow and column == sliceColumn):
                        if current != -1: # do not add unliveable area to the area around the cell
                            area.append(automaton.world[sliceRow][sliceColumn])
        sumArea = sum(area)
        if current == 1:
            if sumArea < 2:
                return 0
            if sumArea >= 2 and sumArea <= 3:
                return 1
            if sumArea > 3 and current == 1:
                return 0
        elif current == 0:
            if sumArea == 3:
                return 1
            else:
                return 0
    else:
        return current

# building custom world
width = 230
height = 70
# worlds cells can have 3 values: 1 = live; 0 = dead; -1 = an unliveable area
world = [[random.choice([0, 1]) for _1 in range(0, width)] for _2 in range(0, height)]
# building an unliveable area on row 20 somewhere in the middle
world[20] = [0 for _ in range(0, int(width / 3))] + [-1 for _ in range(0, int(width / 3))] + [0 for _ in range(0, int(width / 3))] + [0, 0]
world[40] = [0 for _ in range(0, int(width / 3))] + [-1 for _ in range(0, int(width / 3))] + [0 for _ in range(0, int(width / 3))] + [0, 0]
world[60] = [0 for _ in range(0, int(width / 3))] + [-1 for _ in range(0, int(width / 3))] + [0 for _ in range(0, int(width / 3))] + [0, 0]

automaton.run(gameOfLifeCell, width, height, newWorld = world)
