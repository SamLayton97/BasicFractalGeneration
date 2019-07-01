import pygame
import Constants
import Vector

from pygame.locals import *
from Vector import VectorInt

# A straight line connected by 2 points
class Line:

	# basic line parameters
	surface = None					# surface to draw line on
	start = VectorInt(0, 0)			# end point A of line
	end = VectorInt(0, 0)			# end point B of line
	width = 1
	color = Constants.COLOR_WHITE

	# line constructor
	def __init__(self, surface, start, end, width, color):
		# set basic parameters of line
		self.surface = surface
		self.start = start
		self.end = end
		self.width = max(1, int(round(width)))
		self.color = color

	# draws line onto the screen
	def draw(self):
		pygame.draw.line(self.surface, self.color, (self.start.x, self.start.y), (self.end.x, self.end.y), self.width)