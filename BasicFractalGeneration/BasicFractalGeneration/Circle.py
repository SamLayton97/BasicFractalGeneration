import pygame
import math
import StaticShape
import Vector

from pygame.locals import *
from StaticShape import *
from Vector import *

# A basic circle
class Circle(StaticShape):

	# public variables
	radius = 0
	position = VectorInt(0, 0)	# centre of circle

	# circle constructor
	def __init__(self, surface, position, radius, width, color):
		super().__init__(surface, color, width)

		# set circle's attributes
		self.position = position
		self.radius = int(math.fabs(radius))

	# draws circle onto the screen
	def draw(self):
		pygame.draw.circle(self.surface, self.color, (self.position.x, self.position.y), self.radius, self.width)
		