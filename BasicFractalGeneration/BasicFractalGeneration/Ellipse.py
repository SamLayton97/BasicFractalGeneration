import pygame
import math
import StaticShape

from pygame.locals import *
from StaticShape import *

# A basic ellipse
class Ellipse(StaticShape):

	# public variables
	xRadius = 0
	yRadius = 0
	rotation = 0

	def draw(self, surface):
		print("DRAW")