
import sys
import os
import pygame
# sys.path.append(os.path.realpath('../JumpingJack'))
from Model.modelbeobachter import ModelBeobachter


HITBOXES_ON = False


class View(ModelBeobachter):
    def __init__(self, model):
        self.model = model
        self.model.add_observer(self)
        dimensions = self.model.get_dimension()
        self.window = pygame.display.set_mode(dimensions)
        pygame.display.set_caption("Jumpin' Jack")
        self.repaint()

    def repaint(self):
        self.window.fill((0, 0, 0))
        self.repaint_background()
        self.repaint_player()
        self.repaint_obstacle()
        if HITBOXES_ON:
            self.repaint_hitboxes()
            
        pygame.display.update()
        
    def repaint_background(self):
        self.window.blit(self.model.background, (self.model.background_x - self.model.width, 0))
        self.window.blit(self.model.background, (self.model.background_x, 0))
        self.window.blit(self.model.background, (self.model.background_x + self.model.width, 0))
        
    def repaint_hitboxes(self):
        pygame.draw.rect(self.window, (255, 0, 0), self.model.player.hitbox, 2)
        
    def repaint_player(self):
        self.window.blit(self.model.player.current_animation, self.model.player.coords)
        
    def repaint_obstacle(self):
        pygame.draw.rect(self.window, (0, 255, 0), self.model.obstacle.coords)
        

    def update(self):
        self.repaint()