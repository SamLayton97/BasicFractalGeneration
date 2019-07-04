# Fractal-generating functions using basic, static shapes

import time
import math
import Constants
import Vector
import Line
import Circle
import Polygon

from Vector import *
from Line import *
from Circle import *
from Polygon import *

# Recursively draws classic Cantor Ternary Set
def cantorSet(surface, drawList, start, length, deltaY):
	# draw horizontal line at latest position
	drawList.append(Line(surface, start, start + VectorInt(length, 0), 1, Constants.COLOR_WHITE))

	# if next set of lines would be visible
	if length > 2 and start.y + deltaY < Constants.SCREEN_SIZE[1]:
		# draw next 2 lines in cantor set
		cantorSet(surface, drawList, start + VectorInt(0, deltaY), length / 3, deltaY)
		cantorSet(surface, drawList, start + VectorInt((2 * length) / 3, deltaY), length / 3, deltaY)

# Draws classic Koch curve
def kochCurve(surface, curveStart, curveEnd):
	# create lists storing current and next sets of lines
	toCurve = []
	curvedLines = []

	# add first line to a list of lines to generate curves from
	toCurve.append(Line(surface, curveStart, curveEnd, 1, Constants.COLOR_WHITE))

	# continue to generate Koch curves until break case is reached
	generate = True
	while generate:
		# for each segment of curve
		for line in toCurve:
			# get vector defined by current line
			lineVector = line.end - line.start
			
			# if next curve would be indistinguishable, break from generation
			if lineVector.length() < 6:
				generate = False
				break

			# otherwise, using current line, find points of next Koch curve
			scaledVector = lineVector.scale(1/3)
			ascendingPoint = line.start + scaledVector
			descendingPoint = line.end - scaledVector
			risingVector = Vector((scaledVector.x * Constants.COS_60) - (scaledVector.y * Constants.SIN_60), 
						 (scaledVector.x * Constants.SIN_60) + (scaledVector.y * Constants.COS_60))
			peakPoint = descendingPoint - risingVector

			# create / rescale lines using points of curve
			curvedLines.append(Line(surface, ascendingPoint, peakPoint, 1, Constants.COLOR_WHITE))
			curvedLines.append(Line(surface, peakPoint, descendingPoint, 1, Constants.COLOR_WHITE))
			curvedLines.append(Line(surface, descendingPoint, line.end, 1, Constants.COLOR_WHITE))
			line.end = ascendingPoint
			curvedLines.append(line)

		# set next loop to generate curves from next set
		toCurve = curvedLines
		
	# return list of curved lines to draw
	return curvedLines

# Draws the classic sierpinski triangle using polygons
def sierpinskiTriangle(surface, centre, size, isFilled):
	print("draw sierpinski triangle")

	# create lists storing current and next set of triangles
	toBreak = []
	brokenTriangles = []

	# set width/fill of triangles
	width = 1
	if isFilled:
		width = 0

	# add first equilateral triangle to list of triangles to 'break down'
	pointA = centre - VectorInt(0, size)
	pointB = centre - VectorInt(size * Constants.SIN_120, size * Constants.COS_120)
	pointC = centre - VectorInt(-1 * size * Constants.SIN_120, size * Constants.COS_120)
	toBreak.append(Polygon(surface, [pointA, pointB, pointC], Constants.COLOR_WHITE, width))

	# TESTING: return first triangle
	return toBreak

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