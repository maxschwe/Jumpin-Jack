from .panel import Panel
from .button import Button
from pygame.constants import *
import pygame

WIDTH_BTN = 200
HEIGHT_BTN = 50

class StartPanel(Panel):
    def __init__(self, window, dimensions, startscreen):
        self.window = window
        self.dimensions = dimensions
        self.startscreen = startscreen

        start_btn_unscaled = pygame.image.load("Images/startscreen/start.png")
        start_btn = pygame.transform.scale(start_btn_unscaled, (WIDTH_BTN, HEIGHT_BTN))

        exit_btn_unscaled = pygame.image.load("Images/startscreen/exit.png")
        exit_btn = pygame.transform.scale(exit_btn_unscaled, (WIDTH_BTN, HEIGHT_BTN))

        self.startButton = Button(self.dimensions[0]/2 - WIDTH_BTN/2, self.dimensions[1]/2-HEIGHT_BTN/2 + 50, WIDTH_BTN, HEIGHT_BTN, start_btn)
        self.exitButton = Button(self.dimensions[0]/2 - WIDTH_BTN/2, self.dimensions[1]/2-HEIGHT_BTN/2+120, WIDTH_BTN, HEIGHT_BTN, exit_btn)

        self.select(0)
        self.draw()
        pygame.display.update()
        

    def draw(self):
        self.window.blit(self.startscreen, (0, 0))

        self.startButton.draw(self.window)
        self.exitButton.draw(self.window)

    def on_keypress(self, key):
        if key == K_UP:
            self.select(0)
        elif key == K_DOWN:
            self.select(1)

    def select(self, index):
        if index == 0:
            self.selected = 0
            self.startButton.setBorder(True)
            self.exitButton.setBorder(False)
        else:
            self.selected = 1
            self.startButton.setBorder(False)
            self.exitButton.setBorder(True)
