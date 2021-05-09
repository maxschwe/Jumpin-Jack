from Model.model import Model
from View.view import View
import pygame
from pygame.constants import *

class Controller:
    def __init__(self, width, height, fps, speed, player_left, player_bottom):
        self.model = Model(width, height, speed)
        self.view = View(self.model, player_left, player_bottom)
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.alive = True
        
    def run(self):
        while self.running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if self.alive:
                if keys[K_LEFT]:
                    self.alive = self.model.left_key()
                if keys[K_RIGHT]:
                    self.alive = self.model.right_key()         
                if keys[K_SPACE]:
                    self.model.space_key()
                if not self.alive:
                    self.view.show_death_screen()
            
            if keys[K_RETURN]:
                self.model.restart()
                self.alive = True

            self.model.update()
            self.clock.tick(self.fps)
        
    