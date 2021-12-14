# Simple Animation with the PyGame, Trinity Gibbs, 12/17/21, 2:46pm, v0.4

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

# Setup the box data.
b1 = {'rect':pygame.rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT} 
b2 = {'rect':pygame.rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT} 
b3 = {'rect':pygame.rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT} 
boxes = [b1, b2, b3] 
