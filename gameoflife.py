import sys
import copy
import time
import random
import automaton

def gameOfLifeCell(row, column):
    area = []
    current = automaton.world[row][column]
    if current != -1:
        for sliceRow in range(row - 1, row + 2):
            for sliceColumn in range(column - 1, column + 2):
                if sliceRow >= 0 and sliceRow < automaton.worldHeight and sliceColumn >= 0 and sliceColumn < automaton.worldWidth:
                    if not (row == sliceRow and column == sliceColumn):
                        if current != -1: # do not add walls to the area around the cell
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

#world[20] = [0 for _ in range(0, int(worldWidth / 3))] + [-1 for _ in range(0, int(worldWidth / 3))] + [0 for _ in range(0, int(worldWidth / 3))] + [0, 0]
automaton.worldWidth = 230
automaton.worldHeight = 70
automaton.run(gameOfLifeCell)
