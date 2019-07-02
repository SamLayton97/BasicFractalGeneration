# Fractal-generating functions using basic, static shapes

import time
import Constants
import Vector
import Line
import Circle

from Vector import *
from Line import *
from Circle import *

# Recursively draws classic, descending cantor set
def cantorSet(surface, drawList, start, length, deltaY):
	# draw horizontal line at latest position
	drawList.append(Line(surface, start, start + VectorInt(length, 0), 1, Constants.COLOR_WHITE))

	# if next line set would be visible
	if length > 2 and start.y + deltaY < Constants.SCREEN_SIZE[1]:
		# draw next 2 lines in cantor set
		cantorSet(surface, drawList, start + VectorInt(0, deltaY), length / 3, deltaY)
		cantorSet(surface, drawList, start + VectorInt((2 * length) / 3, deltaY), length / 3, deltaY)

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