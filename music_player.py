import pygame
import sys

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
    def __init__(self, file_name):
        self.file_name = file_name
        self.display = screen

    def play(self):
        pygame.mixer.music.load(self.file_name)
        pygame.mixer.music.play(0)

    def color_screen(self, color):
        self.display.fill(color)

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

        # print(f"x = {xm}")
        # print(f"y = {ym}")


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if txt == "Play":
                    if (250 <= xm <= 350) and (50 <= ym <= 145):
                        print("Play Button is clicked")

                if txt == "Pause":
                    if (398 <= xm <= 500) and (50 <= ym <= 145):
                        print("Pause button is clicked")

                if txt == "Exit":
                    if (250 <= xm <= 350) and (200 <= ym <= 300):
                        print("Exit button is clicked")
                        pygame.quit()
                        sys.exit()









p = Music_Player("skip.txt")

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





    pygame.display.update()
