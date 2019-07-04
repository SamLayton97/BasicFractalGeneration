import pygame
import math
import Constants

from pygame.locals import *
from Vector import *

# Base class which all static shapes inherit from.
class StaticShape:

	# shape parameters
	surface = None					# surface to draw shape on
	color = Constants.COLOR_WHITE	# color of shape
	width = 1						# width of shape's edge, 0 denotes shape is 'filled in'

	# shape constructor
	def __init__(self, surface, color, width):
		# set base parameters used by all static shapes
		self.surface = surface
		self.color = color
		self.width = int(math.fabs(width))

	# Draws shape onto specified surface.
	# NOTE: All child classes must override this method.
	def draw(self):
		pass