import sys
import copy
from time import sleep
import random
worldWidth = 20
worldHeight = 20
world = [[random.choice([0, 1]) for _1 in range(0, worldWidth)] for _2 in range(0, worldHeight)]
#world = [[0 for _1 in range(0, worldWidth)] for _2 in range(0, worldHeight)]
#world[0][0] = world[0][1] = world[0][2] = world[1][0] = world[1][2] = world[2][0] = world[2][2] = 1

def gameOfLifeCell(row, column):
	global world, worldWidth, worldHeight
	area = []
	current = world[row][column]
	for sliceRow in range(row - 1, row + 2):
		for sliceColumn in range(column - 1, column + 2):
			if sliceRow >= 0 and sliceRow < worldHeight and sliceColumn >= 0 and sliceColumn < worldWidth:
				if not (row == sliceRow and column == sliceColumn):
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

def printWorld():
	global world, worldWidth, worldHeight
	for row in range(0, worldHeight):
		for column in range(0, worldWidth):
			if world[row][column] == 1:
				sys.stdout.write("*")
			else:
				sys.stdout.write(" ")
		sys.stdout.write("\n")
	sys.stdout.flush()

def repaint():
	sys.stdout.write("\033[F" * (worldHeight))
	sys.stdout.flush()

def mutate():
	global world
	newWorld = copy.deepcopy(world)
	for row in range(0, worldHeight):
		for column in range(0, worldWidth):
			newWorld[row][column] = gameOfLifeCell(row, column)
	world = newWorld
			
while True:
	printWorld()
	mutate()
	sleep(0.2)
	repaint()
