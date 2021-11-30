# My First PyGame, Lamar Camp Jr, 11/30/21, 2:14PM, v0.3

import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup the game window.
WindowSuface = pygame.display.set_mode((500,400),0,32)
pygame.display,set_caption('Hello, world')

# Setup color Values.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINKISHPURPLE = (191, 15, 180)

