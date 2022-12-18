import pygame
import os
import setting
import random




class Alien(pygame.sprite.Sprite):
	def __init__(self,image, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = x, y	
		
	def update(self):
		self.rect.move_ip(setting.SPEED)
		if self.rect.left < 0 or self.rect.right > setting.WIDTH:
			setting.SPEED[0] = -setting.SPEED[0]		
		
	def aliens_group(self,aliens_list):
		y = 100
		for i in range(3):
			x= 100
			for j in range(7):
				alien = Alien(pygame.image.load(os.path.join('alp', 'alien.bmp')), x, y)
				aliens_list.add(alien)
				x += 120
			y += 80	
		return aliens_list
	
	
		





































