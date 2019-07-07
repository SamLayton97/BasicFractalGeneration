# A basic fractal generation program
import pygame
import math
import Constants
import Vector
import RecursiveShapes
import Polygon

from pygame import *
from Vector import *
from RecursiveShapes import *
from Polygon import *

# initialize pygame
pygame.init()

# set display parameters
pygame.display.set_caption(Constants.APP_NAME)
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock = pygame.time.Clock()
if Constants.FULLSCREEN:
	screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.FULLSCREEN)

# container for each shape in fractal
shapes = []

# test drawing a koch snowflake
shapes.append(RecursiveShapes.kochSnowflake(screen, VectorInt(Constants.SCREEN_SIZE[0] / 2, Constants.SCREEN_SIZE[1] / 2), 450, True))

# while user has not closed application
hasQuit = False
while not hasQuit:
	# wipe screen of previous frame
	screen.fill(Constants.COLOR_BLACK)
	
	# process all in-game events
	for event in pygame.event.get():
		if event.type == pygame.QUIT \
			or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			hasQuit = True

	# draw each shape onto screen
	for currShape in shapes:
		currShape.draw()

	# double buffer
	pygame.display.flip()

	# limit screen-refresh to 60 fps
	clock.tick(Constants.FRAME_RATE)

# quit after exiting main app loop
pygame.quit()