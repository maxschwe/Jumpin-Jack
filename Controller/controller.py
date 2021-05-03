from Model.model import Model
from View.view import View
import pygame
from pygame.constants import *

class Controller:
    def __init__(self, width, height, fps, speed):
        self.model = Model(width, height, speed)
        self.view = View(self.model)
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.model.left_key()
            if keys[K_RIGHT]:
                self.model.right_key()
            if keys[K_UP]:
                self.model.up_key()
            if keys[K_DOWN]:
                self.model.down_key()
            if keys[K_SPACE]:
                self.model.space_key()
            self.model.update()
            self.clock.tick(self.fps)
        
    