import pygame
import os
import time

WIDTH = 1000
HEIGHT = 700
COLOR = (255, 255, 255)
REFRESH_RATE = 60
SPEED = [1, 0]

	
	
class Rocket_ship(pygame.sprite.Sprite):
	def __init__(self, image, x_loc, y_loc):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = x_loc, y_loc
		
	def move_right(self):
		self.rect.move_ip((2,0))
		#bul.rect.move_ip((2,0))
		
	def move_left(self):
		self.rect.move_ip((-2,0))
		#bul.rect.move_ip((-2,0))
		
#	def shoot_up(self, Shot):
#		shot_up(self.rect.center)	
		
		
class Alien(pygame.sprite.Sprite):
	def __init__(self, image, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = x, y
		
	def update(self, bul_a):
		self.rect.move_ip(SPEED)
		if self.rect.left < 0 or self.rect.right > WIDTH:
			SPEED[0] = -SPEED[0]		
		
	#def aliens_group(self):
		
	
		
		
class bulet(pygame.sprite.Sprite):
	def __init__(self, image,x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = x, y
	#	self.origRectCenter = x, y
		
		
	#def shoot_reCenter(self,x):
	#	self.rect.center = (x,self.origRectCenter[1]) 
			
	#def bulet_group(self, bulets):
	#	self.bulets = pygame.sprite.Group()
			
		
	def shoot_up(self, aliens_list, screen):
		self.rect.move_ip((0, 10))
		for i in range(10):
			self.rect[1] -= 80
			if self.crash(aliens_list) is True:
				return
		screen.blit(self.image,  self.rect)
			#time.sleep(1)
			
		
	def shoot_down(self, aliens_list, screen):
		for i in range(20):
			self.rect[1] += 3
			if self.crash(aliens_list) is True:
				return
		screen.blit(self.image,  self.rect)
     		
			
	def crash(self,aliens_list):
		for alien in aliens_list:
			if alien.rect.center[1] < self.rect.center[1] + 40 and alien.rect.center[1] > self.rect.center[1] - 40:
				if alien.rect.center[0] < self.rect.center[0] + 60 and alien.rect.center[0] > self.rect.center[0] - 60:
						aliens_list.remove(alien)  
						return True
		return False
def main():
	
	pygame.init()
	clock = pygame.time.Clock()
	size = (WIDTH, HEIGHT)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Game")
	
	
	ship = Rocket_ship(pygame.image.load(os.path.join('alp', 'ship.bmp')), WIDTH/2, HEIGHT*0.9)
	
	#bul =	bulet(pygame.image.load(os.path.join('alp', 'index.png')), WIDTH/2 ,  HEIGHT*0.8)
	#bul.bulet_group()
	bul_a =	bulet(pygame.image.load(os.path.join('alp', 'index.png')), WIDTH/2 ,  100)
	
	
	aliens_list = pygame.sprite.Group()
		
	y = 100
	for i in range(3):
		x= 100
		for j in range(7):
			alien = Alien(pygame.image.load(os.path.join('alp', 'alien.bmp')), x, y)
			aliens_list.add(alien)
			x += 120
		y += 80	

	bulets = pygame.sprite.Group()
	
	
	
	
	im_done = False
	while not im_done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				im_done = True
				
		screen.fill(COLOR)
		
		screen.blit(ship.image, ship.rect)

		screen.blit(bul_a.image,  bul_a.rect)
		aliens_list.update(bul_a)
		#aliens_group()
		for ali in aliens_list:
			if ali.rect.left < 0 or ali.rect.right > WIDTH:
				for al in aliens_list:
					al.rect.center = (al.rect.center[0], al.rect.center[1] +10)
		
		#aliens_list.update_down()
		#if aliens_list < 0 or aliens_list > WIDTH:
		#	aliens_list[1] -= 20
		

		aliens_list.draw(screen)	
		pressing = pygame.key.get_pressed()
		#print(pressing)
		if pressing[pygame.K_RIGHT]:
			ship.move_right()
		if pressing[pygame.K_LEFT]:
			ship.move_left()
		if ship.rect.left < 0:
			ship.rect[0] += 3
		if ship.rect.right > WIDTH:
			ship.rect[0] -= 3
		if pressing[pygame.K_SPACE]:
			bul =	bulet(pygame.image.load(os.path.join('alp', 'index.png')),  *ship.rect.center)
			bulets.add(bul)
			screen.blit(bul.image,  bul.rect)
			bulets.draw(screen)
			
			#bulets.remove(bul)
			#print(bul.rect.center)
			bul.shoot_up(aliens_list,screen)
			#bul.shoot_reCenter(ship.rect.center[0])
		if pressing[pygame.K_DOWN]:
			bul_a.shoot_down(aliens_list,screen)
				
		
		
		
				
		pygame.display.flip()			
		clock.tick(REFRESH_RATE)

	pygame.quit()		

		
    
    
if __name__== '__main__':
    main()
		
	
	



	 
		
