import pygame
import math
import StaticShape

from pygame.locals import *
from StaticShape import *

# A basic circle
class Circle(StaticShape):

	# public variables
	radius = 0

	# circle constructor
	def __init__(self, surface, position, radius, width, color):
		super().__init__(surface, position, color, width)

		# set circle's attributes
		self.radius = int(math.fabs(radius))

	# draws circle onto the screen
	def draw(self, surface):
		pygame.draw.circle(surface, self.color, (int(self.position.x), int(self.position.y)), self.radius, self.width)
