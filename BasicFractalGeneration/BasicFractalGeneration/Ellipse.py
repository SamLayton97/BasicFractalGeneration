import pygame
import math
import StaticShape
import Vector

from pygame.locals import *
from StaticShape import *
from Vector import *

# A basic ellipse
class Ellipse(StaticShape):

	# public variables
	boundingRect = None
	position = VectorInt(0, 0)

	# ellipse constructor
	def __init__(self, surface, position, color, width, dimensions):
		super().__init__(surface, color, width)

		# generate ellipse's bounding rect from parameters
		self.boundingRect = pygame.Rect(position.x - dimensions.x, position.y - dimensions.y,
								dimensions.x * 2, dimensions.y * 2)

	# draws ellipse onto the screen
	def draw(self):
		pygame.draw.ellipse(self.surface, self.color, self.boundingRect, self.width)