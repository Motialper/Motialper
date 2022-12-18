import pygame
import os
import setting
 	 	
from alien import Alien

class bulet(pygame.sprite.Sprite):
	def __init__(self, image,x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = x, y
	
	#def bulet_group(self, bulets):
	#	self.bulets = pygame.sprite.Group()
			
		
	def shoot_up(self,aliens_list, screen, ):
		self.rect.move_ip((0, 1))
		for i in range(10):
			self.rect[1] -= 80
			if self.crash(aliens_list) is True:
				return
			screen.blit(self.image,  self.rect)
			#time.sleep(1)
			
		
	def shoot_down(self, screen):
		self.rect.move_ip((-10, 0 ))
		for i in range(20):
					self.rect[1] += 3
#			if self.crash(aliens_list) is True:
#				return
		screen.blit(self.image,  self.rect)
		
	
     		
			
	def crash(self,aliens_list):
		for alien in aliens_list:
			if alien.rect.center[1] < self.rect.center[1] + 40 and alien.rect.center[1] > self.rect.center[1] - 40:
				if alien.rect.center[0] < self.rect.center[0] + 60 and alien.rect.center[0] > self.rect.center[0] - 60:
						aliens_list.remove(alien)  
						return True
		return False


















