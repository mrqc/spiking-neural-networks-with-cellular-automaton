import sys
import copy
from time import sleep
import random
worldWidth = 20
worldHeight = 20
world = [[random.choice([0, 1]) for _1 in range(0, worldWidth)] for _2 in range(0, worldHeight)]

def gameOfLifeCell(row, column):
	global world, worldWidth, worldHeight
	area = []
	current = world[row][column]
	for sliceRow in range(row - 1, row + 2):
		for sliceColumn in range(column - 1, column + 2):
#			if row == 1 and column == 3:
#				print sliceRow, sliceColumn, "=", world[sliceRow][sliceColumn]
			if sliceRow >= 0 and sliceRow < worldHeight and sliceColumn >= 0 and sliceColumn < worldWidth and (row != sliceRow or column != sliceColumn):
				area.append(world[sliceRow][sliceColumn])
	sumArea = sum(area)
#	if row == 1 and column == 3:
#		print sumArea
	if sumArea == 3 and current == 0:
		return 1
	if sumArea < 2 and current == 1:
		return 0
	if sumArea >= 2 and sumArea <= 3 and current == 1:
		return 1
	if sumArea > 3 and current == 1:
		return 0
	return current

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
	sys.stdout.write("\033[F" * worldHeight)
	sys.stdout.flush()

def mutate():
	global world
	newWorld = copy.deepcopy(world)
	for row in range(0, worldHeight):
		for column in range(0, worldWidth):
			newWorld[row][column] = gameOfLifeCell(row, column)
			gameOfLifeCell(row, column)
	world = newWorld
			
while True:
	printWorld()
	mutate()
	sleep(1)
	repaint()
