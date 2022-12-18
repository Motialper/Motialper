import pygame
import os
from ship import Rocket_ship
from alien import Alien
from bulets import bulet
import setting
import main
import random

def import_opject():
	ship = Rocket_ship(pygame.image.load(os.path.join('alp', 'ship.bmp')), setting.WIDTH/2, setting.HEIGHT*0.9)
	setting.screen.blit(ship.image, ship.rect)
	
	aliens_list = pygame.sprite.Group()	
	y = 100
	for i in range(3):
		x= 100
		for j in range(5):
			alien = Alien(pygame.image.load(os.path.join('alp', 'alien.bmp')), x, y)
			aliens_list.add(alien)
			x += 120
		y += 80	
		
	
	bul = bulet(pygame.image.load(os.path.join('alp', 'index.png')),  *ship.rect.center)
	#bule = bulet(pygame.image.load(os.path.join('alp', 'index.png')),  *aliens_list.rect.center)
	
	return ship, aliens_list, bul




def move(ship, aliens_list, bul):
	#move to ship
	pressing = pygame.key.get_pressed()
	if pressing[pygame.K_RIGHT]:
		ship.move_right()
	if pressing[pygame.K_LEFT]:
		ship.move_left()
	if ship.rect.left < 0:
		ship.rect[0] += 3
	if ship.rect.right > setting.WIDTH:
		ship.rect[0] -= 3
	
	#move to aliians
	for ali in aliens_list:
				if ali.rect.left < 0 or ali.rect.right > setting.WIDTH:
					for al in aliens_list:
						al.rect.center = (al.rect.center[0], al.rect.center[1] +10)
	
	#move and creat to bulets
	bulets = pygame.sprite.Group()
	if pressing[pygame.K_SPACE]:
		bul =	bulet(pygame.image.load(os.path.join('alp', 'index.png')),  *ship.rect.center)
		bulets.add(bul)
		bulets.draw(setting.screen)
		bul.shoot_up( aliens_list,setting.screen)
		setting.screen.blit(bul.image,  bul.rect)
		bulets.remove(bul)
	
	bulets.draw(setting.screen)
	
"""
	my_list = aliens_list.sprites()
	bulets_a = pygame.sprite.Group()
	if len(bulets) <5:
		ran_alian = random.choice(my_list)
		bul = bulet(pygame.image.load(os.path.join('alp', 'index.png')),  *ran_alian.rect.center)
		bulets_a.add(bul)
		bulets_a.draw(screen)
		bulets_a.shoot_down(speed)
		for bulet in bulets:
			if bulet.rect[1] > setting.WIDTH:
				bulet.kill()
	bulets_list.draw(screen)
	print(bulets)
#		return ran_alian, aliens_list, bulets
"""


#def random_alians(self, aliens_list):
	#	aliens_list = aliens_list.sprites()
	#	ran_alian = randum.chois(aliens_list)
	#	bul = bulet(pygame.image.load(os.path.join('alp', 'index.png')),  *ran_alian)
	#	ran_alian.shoot_down(self, setting.screen)
	#	aliens_list.draw(setting.screen)
		#print(ran_alian)


def crash(self):
	for bule in bulets:
		if pygame.sprite.collide_rect(self, bule) == True:
			press
			

	





















