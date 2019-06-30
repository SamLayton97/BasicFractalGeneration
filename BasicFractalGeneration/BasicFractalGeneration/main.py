# A basic fractal generation program

import pygame
import Constants
import Vector
import Circle

from pygame import *
from Vector import *
from Circle import *

# initialize pygame
pygame.init()

# set display parameters
pygame.display.set_caption(Constants.APP_NAME)
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock = pygame.time.Clock()

# container for each shape in fractal
shapes = []

# Recursively draws circles in horizontal line
def circleLine(position, radius):
	# create circle
	shapes.append(Circle(screen, position, radius, 1, Constants.COLOR_WHITE))
	print(position)

	# if next circles would be visible, draw next set
	if radius >= 2:
		circleLine(position + Vector(radius, 0), radius / 2)
		circleLine(position - Vector(radius, 0), radius / 2)

# draw horizontal line of circles starting centre screen
circleLine(Vector(Constants.SCREEN_SIZE[0] / 2, Constants.SCREEN_SIZE[1] / 2), 300)

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
		currShape.draw(screen)

	# double buffer
	pygame.display.flip()

	# limit screen-refresh to 60 fps
	clock.tick(Constants.FRAME_RATE)

# quit after exiting main app loop
pygame.quit()