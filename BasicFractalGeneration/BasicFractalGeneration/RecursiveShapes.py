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

# Draws the more complicated Koch Snowflake
def kochSnowflake(surface, centre, distFromCentre, isFilled):
	print("koch snowflake")

	# set fill of snowflake
	width = 1
	if isFilled:
		width = 0

	# create equilateral triangle defined by points A, B, and C
	pointA = centre - VectorInt(distFromCentre * Constants.SIN_120, distFromCentre * Constants.COS_120)
	pointB = centre - VectorInt(0, distFromCentre)
	pointC = centre - VectorInt(-1 * distFromCentre * Constants.SIN_120, distFromCentre * Constants.COS_120)

	# TESTING: return initial polygon
	return Polygon(surface, [pointA, pointB, pointC], Constants.COLOR_WHITE, width)

# Draws the classic sierpinski triangle using polygon objects
def sierpinskiTriangle(surface, centre, distFromCentre, isFilled):
	# create lists storing current and next set of triangles
	toBreak = []
	brokenTriangles = []

	# set width/fill of triangles
	width = 1
	if isFilled:
		width = 0

	# add first equilateral triangle defined by points A, B, and C
	pointA = centre - VectorInt(distFromCentre * Constants.SIN_120, distFromCentre * Constants.COS_120)
	pointB = centre - VectorInt(0, distFromCentre)
	pointC = centre - VectorInt(-1 * distFromCentre * Constants.SIN_120, distFromCentre * Constants.COS_120)
	toBreak.append(Polygon(surface, [pointA, pointB, pointC], Constants.COLOR_WHITE, width))

	# continue to generate sierpinski triangles until break case is reached
	generate = True
	while generate:
		# for each sub-triangle in whole
		for triangle in toBreak:
			# get vector defined between two points
			vectorAB = triangle.coordToPointVector(triangle.coordinates[1]) - triangle.coordToPointVector(triangle.coordinates[0])

			# if next set of triangles would be indistinguishable, stop generating
			if vectorAB.length() < 4:
				generate = False
				break

			# otherwise, get vertices of current triangle
			vertexA = triangle.coordToPointVector(triangle.coordinates[0])
			vertexB = triangle.coordToPointVector(triangle.coordinates[1])
			vertexC = triangle.coordToPointVector(triangle.coordinates[2])

			# get vectors defined by other 2 sides of triangle
			vectorBC = vertexC - vertexB
			vectorAC = vertexC - vertexA

			# find bisecting points (x, y, z) of each side
			bisectorX = vertexA + vectorAB.scale(0.5)
			bisectorY = vertexB + vectorBC.scale(0.5)
			bisectorZ = vertexA + vectorAC.scale(0.5)

			# create / rescale triangles using vertices and bisectors
			brokenTriangles.append(Polygon(surface, [bisectorX, vertexB, bisectorY], Constants.COLOR_WHITE, width))
			brokenTriangles.append(Polygon(surface, [bisectorZ, bisectorY, vertexC], Constants.COLOR_WHITE, width))
			triangle.coordinates[1] = triangle.pointVectorToCoord(bisectorX)
			triangle.coordinates[2] = triangle.pointVectorToCoord(bisectorZ)
			brokenTriangles.append(triangle)
			
		# set next loop to generate sierpinski's triangle from new triangles
		toBreak = brokenTriangles

	# return list of 'broken' triangles to draw
	return brokenTriangles

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

# Recursively generate a tree with two main branches.
# NOTE: Branch rotation parameter is measured in radians.
def fractalTree(surface, drawList, trunkStart, trunkEnd, branchRotation, branchDecay):
	# create a line defined by trunk's points
	drawList.append(Line(surface, trunkStart, trunkEnd, 1, Constants.COLOR_WHITE))

	# if next branch generation would be visible
	branchVector = (trunkEnd - trunkStart).scale(branchDecay)
	if branchVector.length() > 2:
		# find end points of next branch set
		rightRotation = VectorInt(branchVector.x * math.cos(branchRotation) - branchVector.y * math.sin(branchRotation),
						 branchVector.x * math.sin(branchRotation) + branchVector.y * math.cos(branchRotation))
		leftRotation = VectorInt(branchVector.x * math.cos(-1 * branchRotation) - branchVector.y * math.sin(-1 * branchRotation),
						 branchVector.x * math.sin(-1 * branchRotation) + branchVector.y * math.cos(-1 * branchRotation))
		rightBranchTip = trunkEnd + rightRotation
		leftBranchTip = trunkEnd + leftRotation

		# recursively generate trees from resulting branches
		fractalTree(surface, drawList, trunkEnd, rightBranchTip, branchRotation, branchDecay)
		fractalTree(surface, drawList, trunkEnd, leftBranchTip, branchRotation, branchDecay)