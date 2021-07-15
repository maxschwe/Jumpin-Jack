from Model.model import Model
from View.view import View
import pygame
from pygame.constants import *

class Controller:
    def __init__(self, width, height, fps, speed, jump_force, gravity, player_left, player_bottom):
        self.model = Model(width, height, speed, jump_force, gravity)
        self.view = View(self.model, player_left, player_bottom)
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        
    def run(self):
        self.view.repaint()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                self.running = False
                continue

            if pygame.mouse.get_pressed()[0]:
                clicked = True
                click_pos = pygame.mouse.get_pos()
            else:
                clicked = False

            if self.model.alive:
                if keys[K_LEFT]:
                    self.model.left_key()
                if keys[K_RIGHT]:
                    self.model.right_key()     
                if keys[K_SPACE]:
                    self.model.space_key()
            
            elif self.model.start:
                if clicked:
                    if self.view.panel.startButton.check_if_clicked(*click_pos):
                        self.model.restart_game()
                    elif self.view.panel.exitButton.check_if_clicked(*click_pos):
                        exit()
                
                if keys[K_UP]:
                    self.view.update_start_screen(K_UP)
                if keys[K_DOWN]:
                    self.view.update_start_screen(K_DOWN)
                if keys[K_RETURN]:
                    if self.view.panel.selected == 0:
                        self.model.restart_game()
                    elif self.view.panel.selected == 1:
                        exit()
            elif not self.model.alive:
                if keys[K_RETURN]:
                    self.model.restart_game()

            if self.model.alive:
                self.model.update_game()
            self.clock.tick(self.fps)
