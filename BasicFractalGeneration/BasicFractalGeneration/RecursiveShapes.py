# Fractal-generating functions using basic, static shapes

import time
import math
import Constants
import Vector
import Line
import Circle

from Vector import *
from Line import *
from Circle import *

# Recursively draws classic Cantor Ternary Set
def cantorSet(surface, drawList, start, length, deltaY):
	# draw horizontal line at latest position
	drawList.append(Line(surface, start, start + VectorInt(length, 0), 1, Constants.COLOR_WHITE))

	# if next set of lines would be visible
	if length > 2 and start.y + deltaY < Constants.SCREEN_SIZE[1]:
		# draw next 2 lines in cantor set
		cantorSet(surface, drawList, start + VectorInt(0, deltaY), length / 3, deltaY)
		cantorSet(surface, drawList, start + VectorInt((2 * length) / 3, deltaY), length / 3, deltaY)

def kochCurve(surface, curveStart, curveEnd):
	# create lists storing current set of lines and all lines to draw
	currSet = []
	drawList = []

	# add first line to a list of lines to generate curves from
	currSet.append(Line(surface, curveStart, curveEnd, 1, Constants.COLOR_WHITE))

	# continue to generate Koch curves until break case is reached
	generate = True
	while generate:
		# for each segment of curve
		for line in currSet:
			# get vector defined by line
			lineVector = line.end - line.start
			nextSet = []

			# if next curve would be indiscernable, break from generation
			if lineVector.length() < 6:
				generate = False
				break

			# otherwise, using current line, find points of next Koch curve
			scaledVector = lineVector.scale(1/3)
			point2 = line.start + scaledVector
			point4 = line.end - scaledVector
			point5 = line.end
			cos60 = math.cos(math.pi / 3)
			sin60 = math.sin(math.pi / 3)
			risingVector = Vector((scaledVector.x * Constants.COS_60) - (scaledVector.y * Constants.SIN_60), 
						 (scaledVector.x * Constants.SIN_60) + (scaledVector.y * Constants.COS_60))
			point3 = point4 - risingVector

			# rescale / create lines using points of curve
			line.end = point2
			nextSet.append(line)
			nextSet.append(Line(surface, point2, point3, 1, Constants.COLOR_WHITE))
			nextSet.append(Line(surface, point3, point4, 1, Constants.COLOR_WHITE))
			nextSet.append(Line(surface, point4, point5, 1, Constants.COLOR_WHITE))
			drawList = nextSet

		# TESTING: print points and break after 1 generation
		for kochLine in drawList:
			print(str(kochLine.start) + " " + str(kochLine.end))
		generate = False
		
	return drawList

# Recursively draws circles in horizontal line
def circleHLine(surface, drawList, position, radius):
	# create circle
	drawList.append(Circle(surface, position, radius, 1, Constants.COLOR_WHITE))

	# if next circles would be visible, draw next set
	if radius >= 2:
		circleHLine(surface, drawList, position + VectorInt(radius, 0), radius / 2)
		circleHLine(surface, drawList, position - VectorInt(radius, 0), radius / 2)

# Recursively draws circles in diamond
def circleDiamond(surface, drawList, position, radius):
	# create circle
	drawList.append(Circle(surface, position, radius, 1, Constants.COLOR_WHITE))

	# if next circles would be visible, draw next set
	if radius >= 2:
		circleDiamond(surface, drawList, position + VectorInt(radius, 0), radius / 2)
		circleDiamond(surface, drawList, position - VectorInt(radius, 0), radius / 2)
		circleDiamond(surface, drawList, position + VectorInt(0, radius), radius / 2)
		circleDiamond(surface, drawList, position - VectorInt(0, radius), radius / 2)