# Simple Animation with the PyGame, Trinity Gibbs, 12/9/21, 2:40pm, v0.3

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init() 

# Setup the window
WINDOWWIDTH = 400
WINDOWWEIGHT == 400
windowSurface = pygame.display.set_mode(WINDOWWIDTH, WINDOWHHEIGHT), 0,32)
pygame.display.set_caption('Animation Example!') 

# Setup the direction variables. 
DOWNLEFT =  'downleft'
DOWNRIGHT = 'downright' 
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Setup color values.
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0,  255)