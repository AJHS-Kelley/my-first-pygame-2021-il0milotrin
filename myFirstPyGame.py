# My First PyGame, Trinity Gibbs, 11/29/21 2:77pm, V0.2

import pygame, sys 
from pygame.locals import *

# Start Pygame
pygame.init() 

#Setup our window. 1 
windowSurface = pygame.display.set_mode((500, 400), 0, 32) 
pygame.display.set_caption('hello, world!')

#setup colors
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 

#Setup font.
basicFont = pygame.font.SysFont(None, 48) 

#Setup text. 
text = basicFont.render('hello, world!' , True, WHITE, BLUE) 
textRect= text.get_rect() 
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

