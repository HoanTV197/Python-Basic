import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
RED = (255,0,0)
clock = pygame.time.Clock()

rect_x = 100
rect_y = 200

while running:		
	clock.tick(60)
	screen.fill(GREEN)

	rect_x += 1
	rect_y += 1
	pygame.draw.rect(screen,RED,(rect_x,rect_y,50,50))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()