import sys
import copy
import time
import random
def gameOfLifeCell(row, column):
    global world, worldWidth, worldHeight
    area = []
    current = world[row][column]
    if current != -1:
        for sliceRow in range(row - 1, row + 2):
            for sliceColumn in range(column - 1, column + 2):
                if sliceRow >= 0 and sliceRow < worldHeight and sliceColumn >= 0 and sliceColumn < worldWidth:
                    if not (row == sliceRow and column == sliceColumn):
                        if current != -1:
                            area.append(world[sliceRow][sliceColumn])
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

def countOfCellsWithValue(value):
    count = 0
    for row in range(0, worldHeight):
        for column in range(0, worldWidth):
            if world[row][column] == value:
                count += 1
    return count

def printWorld():
    global world, worldWidth, worldHeight, liveCellsAtStart
    for row in range(0, worldHeight):
        for column in range(0, worldWidth):
            current = world[row][column]
            if current == 1:
                sys.stdout.write("*")
            elif current == 0:
                sys.stdout.write(" ")
            elif current == -1:
                sys.stdout.write("+")
        sys.stdout.write("\n")
    deadCells = countOfCellsWithValue(0)
    liveCells = countOfCellsWithValue(1)
    sys.stdout.write(" " * worldWidth + "\n\033[F")
    sys.stdout.write("Step: " + str(step) + " Dead Cells: " + str(deadCells) + " Live Cells: " + str(liveCells) + " Live Cells at Start: " + str(liveCellsAtStart) + "\n")
    sys.stdout.flush()

def clearWorld():
    sys.stdout.write("\033[F" * (worldHeight + 1))
    sys.stdout.flush()

def mutateWorld():
    global world, worldHeight, worldWidth, step
    step += 1
    newWorld = copy.deepcopy(world)
    for row in range(0, worldHeight):
        for column in range(0, worldWidth):
            newWorld[row][column] = gameOfLifeCell(row, column)
    world = newWorld

def pause():
    time.sleep(0.005)

step = 0
worldWidth = 230
worldHeight = 70
world = [[random.choice([0, 1]) for _1 in range(0, worldWidth)] for _2 in range(0, worldHeight)]
#world[20] = [0 for _ in range(0, int(worldWidth / 3))] + [-1 for _ in range(0, int(worldWidth / 3))] + [0 for _ in range(0, int(worldWidth / 3))] + [0, 0]
liveCellsAtStart = countOfCellsWithValue(1)

while True:
    printWorld()
    mutateWorld()
    pause()
    clearWorld()


