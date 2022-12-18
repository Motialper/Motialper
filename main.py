import pygame
import main_game
import setting
import os
#main
pygame.init() 
ship, aliens_list, bul= main_game.import_opject()
bulets = pygame.sprite.Group()
im_done = False
while not im_done:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			im_done = True
	main_game.setting.screen.blit(ship.image, ship.rect)
	aliens_list.draw(main_game.setting.screen)
	bulets = pygame.sprite.Group()
	pressing = pygame.key.get_pressed()
	
	bulets.update()
	aliens_list.update()

	m= main_game.move(ship, aliens_list, bul)
	#random_alians(aliens_list, bul)
	#random_alians.draw(setting.screen) 
	pygame.display.flip()	
	#main_game.setting.screen.fill(main_game.setting, setting.img)
	img = pygame.image.load(os.path.join('alp', '/home/motialp/Downloads/space_image(1).bmp'))
	setting.screen.blit(img, [0,0])
#screen.fill( img)
	main_game.setting.clock.tick(setting.REFRESH_RATE)









