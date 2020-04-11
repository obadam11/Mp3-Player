import pygame
import sys
import glob
import os
import time

pygame.init()
clock = pygame.time.Clock()
fps = 20

screen_height = 400
screen_width = 600

white = (255, 255, 255)
black = (0, 0, 0)
dark_blue = (141, 226, 218)
red = (255, 0, 0)
maroon = (128, 0, 0)
pink = (244, 52, 131)
lightblue = (27, 238, 255)
grey = (129, 137, 129)
brown = (160, 82, 45)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MP3 Player")
print(f"CURRENT DIR: {os.getcwd()}")


script_dir = os.path.dirname(__file__)
rel_path = "Music"
abs_file_path = os.path.join(script_dir, rel_path)


def go_into_Music():
    os.chdir(abs_file_path)


class Music_Player(object):
    index = 0
    is_playing = True

    def __init__(self):
        self.display = screen

    def play(self):
        pygame.mixer.music.load(self.file_name)
        pygame.mixer.music.play(0)

    @classmethod
    def inc_index(cls):
        global songs
        if Music_Player.index == len(songs) - 1:
            Music_Player.index = 0
        else:
            Music_Player.index += 1
        print(Music_Player.index)

    @classmethod
    def find_mp3_files(cls):
        songs = glob.glob("./*.mp3")
        music_list = [song[2:] for song in songs]  # Comprehensive list
        return music_list

    @classmethod
    def get_num_mp3(cls):
        songs = Music_Player().find_mp3_files()
        length = len(songs)
        return length

    @classmethod
    def play_music(cls):
        global songs
        songs = Music_Player().find_mp3_files()
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play(-1)
        print(f"Playing {songs[0]}")
        Music_Player.index = 0

    @classmethod
    def pause_music(cls):
        if Music_Player.is_playing:
            pygame.mixer.music.pause()
            print("Paused...")
            Music_Player.is_playing = False
        elif not Music_Player.is_playing:
            pygame.mixer.music.unpause()
            print("Unpaused...")
            Music_Player.is_playing = True

    @classmethod
    def next_music(cls):
        global songs
        Music_Player.inc_index()
        pygame.mixer.music.load(songs[Music_Player.index])
        pygame.mixer.music.play(-1)
        print(f"Playing {songs[Music_Player.index]}")

    def current_song(self, x, y, color):
        go_into_Music()
        all_songs = Music_Player().find_mp3_files()
        playing_now = all_songs[Music_Player.index]
        playing_now = playing_now[:-4]
        on_screen = f"{Music_Player.index + 1} : {playing_now}"
        font = pygame.font.Font(None, 25)
        text = font.render(str(on_screen), 1, color)
        self.display.blit(text, (x, y))

    def text(self, x, y, color, on_screen):
        font = pygame.font.Font(None, 20)
        text = font.render(str(on_screen), 1, color)
        self.display.blit(text, (x, y))

    def get_music_sec(self):
        milli = pygame.mixer.music.get_pos()
        seconds = milli / 1000
        seconds = int(seconds)
        on_screen = seconds
        font = pygame.font.Font(None, 30)
        text = font.render(str(on_screen), 1, red)
        self.display.blit(text, (100,  200))

    def draw_button(self, xb, yb, radius, txt, colorb):

        pygame.draw.circle(self.display, colorb, (xb, yb), radius)

    def listing(self, txt):
        go_into_Music()
        # Making the button functional
        xm, ym = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Music_Player.play_music()
            if event.key == pygame.K_e:
                print("Exit button is clicked")
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_n:
                print("Next button is clicked")
                Music_Player.next_music()
            if event.key == pygame.K_SPACE:
                Music_Player.pause_music()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if txt == "Play":
                if (250 <= xm <= 350) and (50 <= ym <= 145):
                    print("Playing...")
                    Music_Player.play_music()

            if txt == "Pause":
                if (398 <= xm <= 500) and (50 <= ym <= 145):
                    Music_Player.pause_music()

            if txt == "Exit":
                if (250 <= xm <= 350) and (200 <= ym <= 300):
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()

            if txt == "Next":
                if (400 <= xm <= 500) and (200 <= ym <= 300):
                    print("Next button is clicked")
                    Music_Player.next_music()


directorty = """C:\\Users\\96650\\Documents\\Programming\\Python1\\Mp3 Player\\images\\play_button.png"""
play_b = pygame.image.load(directorty)
play_b = pygame.transform.scale(play_b, (64, 64))


def pause_logo(x1, y1, x2, y2):
    pygame.draw.line(screen, black, (x1, y1), (x2, y2))
    pygame.draw.line(screen, black, (x1 - 25, y1), (x2 - 25, y2))


def next_logo(x1, y1):
    pygame.draw.polygon(screen, (0, 0, 0), [
                        (x1, y1), (x1, y1 + 50), (x1 + 25, y1 + 25)])


p = Music_Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        p.listing("Play")
        p.listing("Next")
        p.listing("Exit")
        p.listing("Pause")

    screen.fill(white)
    p.draw_button(xb=300, yb=100, radius=50, txt="Play",
                  colorb=lightblue)
    p.draw_button(xb=450, yb=100, radius=50, txt="Pause",
                  colorb=lightblue)
    p.draw_button(xb=300, yb=250, radius=50, txt="Exit",
                  colorb=lightblue)
    p.draw_button(xb=450, yb=250, radius=50, txt="Next",
                  colorb=lightblue)

    p.text(screen_width - 500, screen_height - 50, black,
           "'P' for PLAY   'SPACE' for PAUSE   'E' for EXIT   'N' for NEXT.")

    p.text(10, 20, black,
           f'number of mp3 files : {Music_Player.get_num_mp3()}')

    p.text(20, 125, pink, "Currently playing:")
    p.current_song(20, 170, pink)

    screen.blit(play_b, (265, 70))

    pause_logo(460, 70, 460, 120)
    next_logo(440, 220)
    p.text(280, 240, black,  "EXIT")

    p.get_music_sec()

    clock.tick(fps)
    pygame.display.update()

pygame.quit()
