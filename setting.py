#setting:
import pygame
import os
WIDTH = 900
HEIGHT = 600
#COLOR = (255, 255, 255)
REFRESH_RATE = 60
SPEED = [1, 0]
speed = [1,0]
clock = pygame.time.Clock()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
img = pygame.image.load(os.path.join('alp', '/home/motialp/Downloads/space_image(1).bmp'))
screen.blit(img, [0,0])
#screen.fill( img)












