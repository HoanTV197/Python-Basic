import pygame
import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

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
		text_render = font.render(self.text, True, (0,0,255))
		self.text_box = text_render.get_rect()
		if self.is_mouse_on_text():
			text_render = font.render(self.text, True, (0,0,255))
			pygame.draw.line(screen, (0,0,255), (self.position[0], self.position[1] + self.text_box[3]), (self.position[0]+self.text_box[2], self.position[1] + self.text_box[3]))
		else:
			text_render = font.render(self.text, True, (0,0,0))

		screen.blit(text_render,self.position)

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()		
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame App')
running = True
clock = pygame.time.Clock()

# Load data
playlist = read_playlist_from_txt()

playlist_name_btn = TextButton(playlist.name.rstrip(), (50,50))

videos_btn_list = []
margin = 50
for i in range(len(playlist.videos)):
	video_btn = TextButton(str(i+1) + ". " +playlist.videos[i].title.rstrip(), (250,50+margin*i))
	videos_btn_list.append(video_btn)

while running:		
	clock.tick(60)
	screen.fill((255,255,255))

	playlist_name_btn.draw()
	for i in range(len(videos_btn_list)):
		videos_btn_list[i].draw()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if playlist_name_btn.is_mouse_on_text():
					print("Choose playlist")
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()