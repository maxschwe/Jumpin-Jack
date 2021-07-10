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

        self.startButton = Button(self.dimensions[0]/2 - WIDTH_BTN/2, self.dimensions[1]/2-HEIGHT_BTN/2 + 50, WIDTH_BTN, HEIGHT_BTN, "green")
        self.settingsButton = Button(self.dimensions[0]/2 - WIDTH_BTN/2, self.dimensions[1]/2-HEIGHT_BTN/2+120, WIDTH_BTN, HEIGHT_BTN, "red")

        self.select(0)
        self.draw()
        pygame.display.update()
        

    def draw(self):
        self.window.blit(self.startscreen, (0, 0))

        self.startButton.draw(self.window)
        self.settingsButton.draw(self.window)

    def on_keypress(self, key):
        if key == K_UP:
            self.select(0)
        elif key == K_DOWN:
            self.select(1)

    def select(self, index):
        if index == 0:
            self.selected = 0
            self.startButton.setBorder(True)
            self.settingsButton.setBorder(False)
        else:
            self.selected = 1
            self.startButton.setBorder(False)
            self.settingsButton.setBorder(True)
