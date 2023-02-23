import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame App')
running = True
BLACK = (0,0,0)
clock = pygame.time.Clock()

while running:		
	clock.tick(60)
	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()