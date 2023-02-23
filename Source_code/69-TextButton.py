import pygame

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def is_mouse_on_text(self):
		pass

	def draw(self):
		pass

random_button = TextButton("Random", (50,50))
random_button.is_mouse_on_text() 
random_button.draw()



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