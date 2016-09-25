import sys
import copy
import time
import random
step = 0
worldWidth = 230
worldHeight = 70
world = [[random.choice([0, 1]) for _1 in range(0, worldWidth)] for _2 in range(0, worldHeight)]
#world[20] = [0 for _ in range(0, int(worldWidth / 3))] + [-1 for _ in range(0, int(worldWidth / 3))] + [0 for _ in range(0, int(worldWidth / 3))] + [0, 0]
#world = [[0 for _1 in range(0, worldWidth)] for _2 in range(0, worldHeight)]
#world[0][0] = world[0][1] = world[0][2] = world[1][0] = world[1][2] = world[2][0] = world[2][2] = 1

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

def printWorld():
    global world, worldWidth, worldHeight
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
    sys.stdout.write(str(step) + "\n")
    sys.stdout.flush()

def repaint():
    sys.stdout.write("\033[F" * (worldHeight + 1))
    sys.stdout.flush()

def mutate():
    global world, worldHeight, worldWidth, step
    step += 1
    newWorld = copy.deepcopy(world)
    for row in range(0, worldHeight):
        for column in range(0, worldWidth):
            newWorld[row][column] = gameOfLifeCell(row, column)
    world = newWorld
            
while True:
    printWorld()
    mutate()
    time.sleep(0.005)
    repaint()
