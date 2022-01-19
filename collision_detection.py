# PyGame Collision Detection Practice, Trinity Gibbs, January 19, 2022, 1:55PM, v0.3

import pygame, sys, random 
from pygame.locals  import *

# Setup PyGame 
pygame.init()
mainClock = pygame.time.Clock() 

# Setup the PyGame Window 
WINDOWWIDTH = 400 
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
pygame.display.set_caption('Collision Detection 2022')

# Setup colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
