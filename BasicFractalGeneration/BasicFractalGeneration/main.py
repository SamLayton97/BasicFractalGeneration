# A basic fractal generation program
import pygame
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

# container for each shape in fractal
shapes = []

# test drawing a koch curve
#shapes = RecursiveShapes.kochCurve(screen, VectorInt(0, Constants.SCREEN_SIZE[1] - 200), 
						  #VectorInt(Constants.SCREEN_SIZE[0], Constants.SCREEN_SIZE[1] - 200))

# test drawing a triangle
pointList = []
pointList.append(VectorInt(50, 100))
pointList.append(VectorInt(70, 180))
pointList.append(VectorInt(200, 200))

shapes.append(Polygon(screen, pointList, Constants.COLOR_WHITE, 0))

for point in shapes[0].coordinates:
	print(point)
	print(shapes[0].coordToPointVector(point))

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