import pygame
import sys
import glob

pygame.init()


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
brown = (160,82,45)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MP3 Player")




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
        music_list = [song[2:] for song in songs] # Comprehensive list
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
        pygame.mixer.music.play()
        print(f"Playing {songs[0]}")

    @classmethod
    def pause_music(cls):
        # print(Music_Player.is_playing)
        if Music_Player.is_playing:
            pygame.mixer.music.pause()
            print("Paused...")
            Music_Player.is_playing = False
        elif not  Music_Player.is_playing:
            pygame.mixer.music.unpause()
            print("Unpaused...")
            Music_Player.is_playing = True


    @classmethod
    def next_music(cls):
        global songs
        Music_Player.inc_index()
        pygame.mixer.music.load(songs[Music_Player.index])
        pygame.mixer.music.play()
        print(f"Playing {songs[Music_Player.index]}")


    def current_song(self, x, y, color):
        all_songs = Music_Player().find_mp3_files()
        playing_now = all_songs[Music_Player.index]
        playing_now = playing_now[:-4]
        on_screen = f"{Music_Player.index + 1} : {playing_now}"
        font = pygame.font.Font(None, 25)
        text = font.render(str(on_screen), 1, color)
        self.display.blit(text, (x,y))


    def text(self, x, y, color, on_screen):
        font = pygame.font.Font(None, 20)
        text = font.render(str(on_screen), 1, color)
        self.display.blit(text, (x,y))





    def button(self, xb, yb, radius, txt, colorb, colort, xt, yt):
        # Drawing the rectangle (button)
        pygame.draw.circle(self.display, colorb, (xb, yb), radius)
        # Writing in the button

        # on_screen = str(txt)
        # font = pygame.font.Font(None, 18)
        # text = font.render(str(on_screen), 1, colort)
        # self.display.blit(text, (xt,yt))

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


play_b = pygame.image.load("C:\\Users\\96650\\Documents\\Programming\\Python1\\Mp3 Player\\images\\play_button.png")
play_b = pygame.transform.scale(play_b, (64, 64))
p = Music_Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    p.color_screen(white)

    p.button(xb=300, yb=100, radius=50, txt="Play",
            colorb=lightblue, colort=white, xt=290, yt=95)

    p.button(xb=450, yb=100, radius=50, txt="Pause",
             colorb=lightblue, colort=white, xt=430, yt=95)

    p.button(xb=300, yb=250, radius=50, txt="Exit",
             colorb=lightblue, colort=white, xt=290, yt=240)

    p.button(xb=450, yb=250, radius=50, txt="Next",
             colorb=lightblue, colort=white, xt=435, yt=240)


    p.text(screen_width - 500, screen_height - 50, black,
            "'P' for PLAY   'SPACE' for PAUSE   'E' for EXIT   'N' for NEXT.")

    p.text(10, 20, black, f'number of mp3 files : {Music_Player.get_num_mp3()}')


    p.text(20, 125, pink, "Currently playing:")
    p.current_song(20, 170, pink)

    screen.blit(play_b, (265, 70))




    pygame.display.update()
