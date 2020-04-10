import pygame
import sys
import glob

pygame.init()


screen_height = 400
screen_width = 600

lightblue = (27, 238, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")




class Music_Player(object):
    index = 0
    is_playing = True

    def __init__(self):
        self.display = screen

    def play(self):
        pygame.mixer.music.load(self.file_name)
        pygame.mixer.music.play(0)

    def color_screen(self, color):
        self.display.fill(color)

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
        music_list = [song[2:] for song in songs] # Comprehensive list.
        # print(music_list)
        return music_list

    @classmethod
    def play_music(cls):
        global songs
        songs = Music_Player().find_mp3_files()
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()
        print(f"Playing {songs[0]}")

    @classmethod
    def pause_music(cls):
        print(Music_Player.is_playing)
        if Music_Player.is_playing:
            pygame.mixer.music.pause()
            Music_Player.is_playing = False
        elif not  Music_Player.is_playing:
            pygame.mixer.music.unpause()
            Music_Player.is_playing = True


    @classmethod
    def next_music(cls):
        global songs
        Music_Player.inc_index()
        pygame.mixer.music.load(songs[Music_Player.index])
        pygame.mixer.music.play()
        print(f"Playing {songs[Music_Player.index]}")


    def txt_on_screen(self, x, y, color):
        all_songs = Music_Player().find_mp3_files()
        playing_now = all_songs[Music_Player.index]
        playing_now = playing_now[:-4]
        on_screen = f"{Music_Player.index + 1} : {playing_now}"
        font = pygame.font.Font(None, 30)
        text = font.render(str(on_screen), 1, color)
        self.display.blit(text, (x,y))



    def button(self, xb, yb, radius, txt, colorb, colort, xt, yt):
        # Drawing the rectangle (button)
        pygame.draw.circle(self.display, colorb, (xb, yb), radius)
        # Writing in the button
        on_screen = str(txt)
        font = pygame.font.Font(None, 18)
        text = font.render(str(on_screen), 1, colort)
        self.display.blit(text, (xt,yt))
        # Making the button functional
        xm, ym = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("Playing...")
                    Music_Player.play_music()
                if event.key == pygame.K_e:
                    print("Exit button is clicked")
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_n:
                    print("Next button is clicked")
                    Music_Player.next_music()
                if event.key == pygame.K_SPACE:
                    print("Paused...")
                    Music_Player.pause_music()




        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if txt == "Play":
                    if (250 <= xm <= 350) and (50 <= ym <= 145):
                        print("Playing...")
                        Music_Player.play_music()

                if txt == "Pause":
                    if (398 <= xm <= 500) and (50 <= ym <= 145):
                        print("Paused...")
                        Music_Player.pause_music()

                if txt == "Exit":
                    if (250 <= xm <= 350) and (200 <= ym <= 300):
                        print("Exit button is clicked")
                        pygame.quit()
                        sys.exit()

                if txt == "Next":
                    if (400 <= xm <= 500) and (200 <= ym <= 300):
                        print("Next button is clicked")
                        Music_Player.next_music()



p = Music_Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    p.color_screen(lightblue)

    p.button(xb=300, yb=100, radius=50, txt="Play",
            colorb=red, colort=white, xt=290, yt=95)

    p.button(xb=450, yb=100, radius=50, txt="Pause",
             colorb=red, colort=white, xt=430, yt=95)

    p.button(xb=300, yb=250, radius=50, txt="Exit",
             colorb=red, colort=white, xt=290, yt=240)

    p.button(xb=450, yb=250, radius=50, txt="Next",
             colorb=red, colort=white, xt=435, yt=240)

    p.txt_on_screen(20, 150, black)





    pygame.display.update()
