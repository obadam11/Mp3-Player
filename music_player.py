import pygame
import os

pygame.init()

screen_height = 400
screen_width = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")




class Music_Player(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.display = screen

    def play(self):
        pygame.mixer.music.load(self.file_name)
        pygame.mixer.music.play(0)




p = Music_Player("skip.txt")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






    pygame.display.update()
