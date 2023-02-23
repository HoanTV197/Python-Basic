import pygame

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x > self.position[0] and mouse_x < self.position[0] + self.text_box[2] and mouse_y > self.position[1] and mouse_y < self.position[1] + self.text_box[3]:
			return True
		else:
			return False

	def draw(self):
		font = pygame.font.SysFont('sans',30)
		text_render = font.render(self.text, True, (0,0,0))
		self.text_box = text_render.get_rect()
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
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if random_button.is_mouse_on_text():
					print("Button pressed")
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()