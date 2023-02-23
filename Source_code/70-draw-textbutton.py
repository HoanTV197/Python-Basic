import pygame

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def is_mouse_on_text(self):
		pass

	def draw(self):
		font = pygame.font.SysFont('sans',30)
		text_render = font.render(self.text, True, (0,0,0))
		text_box = text_render.get_rect()
		pygame.draw.rect(screen,(100,100,100), (self.position[0],self.position[1],text_box[2],text_box[3]))
		screen.blit(text_render,self.position)

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame App')
running = True
clock = pygame.time.Clock()

random_button = TextButton("Random", (50,50))

while running:		
	clock.tick(60)
	screen.fill((255,255,255))

	random_button.draw()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()