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

def clearWorld():
    sys.stdout.write("\033[F" * (worldHeight + 1))
    sys.stdout.flush()

def printCellAndGetIncrementCounts(row, column, liveCells, deadCells):
    global world, worldWidth, worldHeight, step, liveCellsAtStart
    current = world[row][column]
    if current == 1:
        sys.stdout.write("*")
        liveCells += 1
    elif current == 0:
        sys.stdout.write(" ")
        deadCells += 1
    elif current == -1:
        sys.stdout.write("+")
    return (liveCells, deadCells)

def mutateAndPrintWorld(mutationFunction):
    global world, worldWidth, worldHeight, step, liveCellsAtStart
    deadCells = liveCells = 0
    step += 1
    newWorld = copy.deepcopy(world)
    for row in range(0, worldHeight):
        for column in range(0, worldWidth):
            newWorld[row][column] = mutationFunction(row, column)
            (liveCells, deadCells) = printCellAndGetIncrementCounts(row, column, liveCells, deadCells)
        sys.stdout.write("\n")
    world = newWorld
    sys.stdout.write(" " * worldWidth + "\n\033[F")
    sys.stdout.write("Step: " + str(step) + " Dead Cells: " + str(deadCells) + " Live Cells: " + str(liveCells) + " Live Cells at Start: " + str(liveCellsAtStart) + "\n")
    sys.stdout.flush()

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
        mutateAndPrintWorld(mutationFunction)
        clearWorld()

