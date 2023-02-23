class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

def read_video():
	title = input("Enter title: ")
	link = input("Enter link: ")
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: ", video.title, end="")
	print("Video link: ", video.link, end="")

def read_videos():
	videos = []
	total_video = int(input("Enter how many videos: "))
	for i in range(total_video):
		print("Enter video ", i+1)
		vid = read_video()
		videos.append(vid)
	return videos

def print_videos(videos):
	for i in range(len(videos)):
		print_video(videos[i])

def write_video_txt(video, file):
	file.write(video.title + "\n")
	file.write(video.link + "\n")

def write_videos_txt(videos, file):
	total = len(videos)
	file.write(str(total) + "\n")
	for i in range(total):
		write_video_txt(videos[i], file)

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

def read_playlist():
	playlist_name = input("Enter playlist name: ")
	playlist_description = input("Enter playlist description: ")
	playlist_rating = input("Enter rating (1-5): ")
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name + "\n")
		file.write(playlist.description + "\n")
		file.write(playlist.rating + "\n")
		write_videos_txt(playlist.videos, file)
	print("Successfully write playlist to txt")

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("-------")
	print("Playlist name: " +  playlist.name, end="")
	print("Playlist description: " +  playlist.description, end="")
	print("Playlist rating: " +  playlist.rating, end="")
	print_videos(playlist.videos)

def show_menu():
	print("-----------")
	print("Option 1: Create playlist")
	print("Option 2: Show playlist")
	print("Option 3: Play a video")
	print("Option 7: Save and Exit")
	print("-----------")


def menu_option_1():
	print("You enter option 1")

def menu_option_2():
	print("You enter option 2")

def menu_option_3():
	print("You enter option 3")

def main():
	# playlist = read_playlist()
	# write_playlist_txt(playlist)
	# playlist = read_playlist_from_txt()
	# print_playlist(playlist)

	while True:
		show_menu()
		choice = int(input("Select an option (1-7):"))
		if choice == 1:
			menu_option_1()			
		elif choice == 2:
			menu_option_2()
		elif choice == 3:
			menu_option_3()
		elif choice == 7:
			break
		else:
			print("Wrong Input, Exist.")
			break
main()