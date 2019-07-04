import pygame
import Vector
import StaticShape

from pygame.locals import *
from Vector import *
from StaticShape import *

# A shape with any number of straight sides
class Polygon(StaticShape):

	# Public variables
	coordinates = []

	# Polygon constructor
	def __init__(self, surface, pointVectors, color, width):
		super().__init__(surface, color, width)
		
		# convert point vectors to drawable coordinate tuples
		for vector in pointVectors:
			coordinates.append(self.vectorToCoord(vector))

	# Displays polygon on the screen
	def draw(self):
		pygame.draw.polygon(self.surface, self.color, self.coordinates, self.width)

	# Converts a point vector to a drawable coordinate tuple
	def pointVectorToCoord(self, vector):
		return (vector.x, vector.y)

	# Converts a coordinate to an easily-to-manipulate point vector
	def coordToPointVector(self, coordinate):
		return VectorInt(coordinate[0], coordinate[1])