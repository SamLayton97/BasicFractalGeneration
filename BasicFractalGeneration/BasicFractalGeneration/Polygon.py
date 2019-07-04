import pygame
import StaticShape

from pygame.locals import *
from StaticShape import *

# A shape with any number of straight sides
class Polygon(StaticShape):

	# public variables
	coordinates = []

	# polygon constructor
	def __init__(self, surface, pointVectors, color, width):
		print("new polygon")