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
	isFilled = False				# is circle 'filled in'
	surface = None					# surface to draw circle on

	# constructor
	def __init__(self, surface, position, radius, width, color, isFilled):
		
		# set circle's attributes
		self.surface = surface
		self.position = position
		self.radius = math.fabs(radius)
		self.width = math.fabs(width)
		self.color = color
		self.isFilled = isFilled