import sys
import copy
import time
import random

step = 0
worldWidth = 0
worldHeight = 0

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

def mutateWorld(mutationFunction):
    global world, worldHeight, worldWidth, step
    step += 1
    newWorld = copy.deepcopy(world)
    for row in range(0, worldHeight):
        for column in range(0, worldWidth):
            newWorld[row][column] = mutationFunction(row, column)
    world = newWorld

def pause():
    time.sleep(0.005)

def initWorld(newWorld):
    global world, worldWidth, worldHeight, liveCellsAtStart
    if newWorld == None:
        world = [[random.choice([0, 1]) for _1 in range(0, worldWidth)] for _2 in range(0, worldHeight)]
    else:
        world = newWorld
    liveCellsAtStart = countOfCellsWithValue(1)

def run(mutationFunction, newWorldWidth, newWorldHeight, newWorld = None):
    global worldWidth, worldHeight
    worldWidth = newWorldWidth
    worldHeight = newWorldHeight
    initWorld(newWorld)
    while True:
        printWorld()
        mutateWorld(mutationFunction)
        pause()
        clearWorld()

