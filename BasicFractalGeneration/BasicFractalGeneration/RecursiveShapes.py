import Vector
import Circle

from Vector import *
from Circle import *

# Fractal-generating functions using basic, static shapes

# Recursively draws circles in horizontal line
def circleHLine(surface, drawList, position, radius):
	# create circle
	drawList.append(Circle(surface, position, radius, 1, Constants.COLOR_WHITE))

	# if next circles would be visible, draw next set
	if radius >= 2:
		circleLine(surface, drawList, position + Vector(radius, 0), radius / 2)
		circleLine(surface, drawList, position - Vector(radius, 0), radius / 2)

# Recursively draws circles in diamond
def circleDiamond(surface, drawList, position, radius):
	# create circle
	drawList.append(Circle(surface, position, radius, 1, Constants.COLOR_WHITE))

	# if next circles would be visible, draw next set
	if radius >= 2:
		circleDiamond(surface, drawList, position + Vector(radius, 0), radius / 2)
		circleDiamond(surface, drawList, position - Vector(radius, 0), radius / 2)
		circleDiamond(surface, drawList, position + Vector(0, radius), radius / 2)
		circleDiamond(surface, drawList, position - Vector(0, radius), radius / 2)