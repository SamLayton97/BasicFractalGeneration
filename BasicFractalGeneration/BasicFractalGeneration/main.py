# A basic fractal generation program
import pygame
import Constants
import Vector
import RecursiveShapes
import Line

from pygame import *
from Vector import *
from RecursiveShapes import *
from Line import *

# initialize pygame
pygame.init()

# set display parameters
pygame.display.set_caption(Constants.APP_NAME)
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock = pygame.time.Clock()

# container for each shape in fractal
shapes = []

# test drawing a cantor set
RecursiveShapes.cantorSet(screen, shapes, VectorInt(60, 60), 680, 60)

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