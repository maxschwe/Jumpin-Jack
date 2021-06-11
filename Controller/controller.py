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
        self.start = True
        self.alive = False
        
    def run(self):
        self.view.show_start_screen()
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
            if keys[K_RETURN]:
                self.model.restart()
                self.start = False
                self.alive = True
            elif keys[K_ESCAPE]:
                self.running = False
                continue

            if self.alive:
                self.model.update_game()
            self.clock.tick(self.fps)
        

    
    