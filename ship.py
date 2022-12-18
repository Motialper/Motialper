import pygame
import os



class Rocket_ship(pygame.sprite.Sprite):
	def __init__(self, image, x_loc, y_loc):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = x_loc, y_loc
		
	def move_right(self):
		self.rect.move_ip((2,0))

		
	def move_left(self):
		self.rect.move_ip((-2,0))




























