import pygame
import math
import Constants

from Vector import *
from pygame.locals import *

# A basic circle
class Circle:

	# public variables
	position = Vector(0, 0)			# centre of circle
	radius = 0
	width = 1						# width of circle's edge
	color = Constants.COLOR_WHITE
	surface = None					# surface to draw circle on

	# constructor
	def __init__(self, surface, position, radius, width, color):
		
		# set circle's attributes
		self.surface = surface
		self.position = position
		self.radius = math.fabs(radius)
		self.width = math.fabs(width)
		self.color = color

	# called once per frame
	def update(self, surface):
		self.draw(surface)

	# draws circle onto the screen
	def draw(self, surface):
		pygame.draw.circle(surface, self.color, (self.position.x, self.position.y), int(self.radius), int(self.width))
