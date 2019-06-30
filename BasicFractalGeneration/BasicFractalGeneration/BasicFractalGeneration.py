
# A basic fractal generation program

import pygame

from pygame import *

# initialize pygame
pygame.init()

screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

# while user has not closed application
hasQuit = False
while not hasQuit:
	# wipe screen of previous frame
	screen.fill((0, 0, 0))
	
	# process all in-game events
	for event in pygame.event.get():
		if event.type == pygame.QUIT \
			or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			hasQuit = True

	# double buffer
	pygame.display.flip()

	# limit screen-refresh to 60 fps
	clock.tick(60)

# quit after exiting main app loop
pygame.quit()