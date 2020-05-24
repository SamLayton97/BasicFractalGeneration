# A basic fractal generation program
import pygame
import math
import Constants
import Vector
import RecursiveShapes

from pygame import *
from Vector import *
from RecursiveShapes import *

#####################################################
# HELPER FUNCTIONS
#####################################################

# Clears board and draws a new fractal
def drawFractal(fractalID):
	# clear board of previous fractal
	screen.fill(Constants.COLOR_BLACK)
	shapes = []

	# generate appropriate fractal
	if fractalID is 1:
		RecursiveShapes.cantorSet(screen, shapes, VectorInt(30, 200), 1220, 50)
	elif fractalID is 2:
		shapes = RecursiveShapes.kochCurve(screen, VectorInt(30, 500), VectorInt(1250, 500))
	elif fractalID is 3:
		shapes.append(kochSnowflake(screen, VectorInt(640, 360), 300, False))
	elif fractalID is 4:
		shapes = RecursiveShapes.sierpinskiTriangle(screen, VectorInt(640, 400), 300, False)
	elif fractalID is 5:
		RecursiveShapes.circleDiamond(screen, shapes, VectorInt(640, 360), 175)
	elif fractalID is 6:
		RecursiveShapes.fractalTree(screen, shapes, VectorInt(640, 650), VectorInt(640, 400), math.pi / 3, 0.6)
	elif fractalID is 7:
		RecursiveShapes.dragonCurve(screen, shapes)

	# draw fractal on screen
	for currShape in shapes:
		currShape.draw()

	# double buffer
	pygame.display.flip()

#####################################################
# MAIN FUNCTIONALITY
#####################################################

# initialize pygame
pygame.init()

# set display parameters
pygame.display.set_caption(Constants.APP_NAME)
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock = pygame.time.Clock()
if Constants.FULLSCREEN:
	screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.FULLSCREEN)
screen.fill(Constants.COLOR_BLACK)

# while user has not closed application
hasQuit = False
while not hasQuit:
	# process all in-game events
	for event in pygame.event.get():
		if event.type == pygame.QUIT \
			or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):	# quit
			hasQuit = True
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_1):	# cantor set
			drawFractal(1)
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_2):	# koch curve
			drawFractal(2)
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_3):	# koch snowflake
			drawFractal(3)
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_4):	# sierpinski triangle
			drawFractal(4)
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_5):	# circle diamond
			drawFractal(5)
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_6):	# fractal tree
			drawFractal(6)
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_7):	# dragon curve
			drawFractal(7)
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_8):	# clear board
			drawFractal(8)

# quit after exiting main app loop
pygame.quit()