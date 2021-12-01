# My First PyGame, Trinity Gibbs, 12/1/21 2:03pm, V0.7
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
OCEANBLUE = (148, 216, 236) 
#Setup font.
basicFont = pygame.font.SysFont(None, 48) 

#Setup text. 
text = basicFont.render('hello, world!' , True, WHITE, BLUE) 
textRect= text.get_rect() 
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill background color. 
windowSurface.fill(OCEANBLUE) 

# Draw a polygon onto the screen. 
pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291,106), (236,277), (56,277), (0,106))

# draw lines on the screen. 
Pygame.draw.line(winowSurface, RED, (60,60), (120,60), 4)
Pygame.draw.line(winowSurface, WHITE, (75,60), (60,75), 2)
Pygame.draw.line(winowSurface, BLUE, (0,150), (150,0), 1)

# Draw a circle. 
pygame.draw.circle(windowSurface, YELLOW, (224, 200), 0)
pygae,draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1) 

#draw the text rectangle.
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height+ 40))