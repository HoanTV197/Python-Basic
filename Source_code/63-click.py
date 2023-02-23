import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
RED = (255,0,0)
clock = pygame.time.Clock()


while running:		
	clock.tick(60)
	screen.fill(GREEN)

	mouse = pygame.mouse.get_pos()	
	mouse_x = mouse[0]	
	mouse_y = mouse[1]	
	print("Mouse X: ", mouse_x)
	print("Mouse Y: ", mouse_y)

	pygame.draw.rect(screen,RED,(50,50,50,50))

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("Right click")

		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()
