import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 900))
background = pygame.image.load('background.png')
ground = pygame.image.load('groundpicture.png')
screen.blit(background,(0,0))

x = 0


pygame.display.set_caption('Hello World!')

while True:
   screen.blit(ground,(x,700))
   x=x-1
   if abs(x) >30:
       x = 0
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()
