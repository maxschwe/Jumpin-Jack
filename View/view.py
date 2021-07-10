
import sys
import os
import pygame
# sys.path.append(os.path.realpath('../JumpingJack'))
from View.modelbeobachter import ModelBeobachter
from pygame.constants import *
from View.startpanel import StartPanel
from View.deathpanel import DeathPanel
from View.gamepanel import GamePanel


class View(ModelBeobachter):
    def __init__(self, model, player_left, player_bottom):
        self.model = model
        
        self.model.add_observer(self)
        self.dimensions = self.model.get_dimension()
        self.window = pygame.display.set_mode(self.dimensions)
        startpanel = StartPanel(self.window, self.dimensions, self.model.start_screen)
        deathpanel = DeathPanel(self.window, self.dimensions)
        gamepanel = GamePanel(self.window, self.dimensions, player_left, player_bottom, model)
        self.panels = [startpanel, gamepanel, deathpanel]
        self.change_panel(0)

        pygame.display.set_caption("Jumpin' Jack")
        pygame.init()

    def repaint(self):
        self.window.fill((0, 0, 0))
        self.panel.draw()
        pygame.display.update()

    def update(self):
        self.repaint()

    def update_start_screen(self,key):
        self.panel.on_keypress(key)
        self.repaint()

    def change_panel(self, i):
        self.panel = self.panels[i]
