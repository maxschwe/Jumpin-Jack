from .panel import Panel
import pygame

HITBOXES_ON = False

class GamePanel(Panel):
    def __init__(self, window, dimensions, player_left, player_bottom, model):
        self.window = window
        self.dimensions = dimensions

        self.player_left = player_left
        self.player_bottom = player_bottom
        self.model = model

    def repaint_background(self):
        self.window.blit(self.model.background, (- (self.model.x % self.model.width), 0))
        self.window.blit(self.model.background, (self.model.width - (self.model.x % self.model.width), 0))
        
    def repaint_player(self):
        rect = self.reposition(self.model.player.coords, False)
        self.window.blit(self.model.player.current_animation, rect)
        if HITBOXES_ON:
            rect = self.reposition(self.model.player.hitbox, False)
            pygame.draw.rect(self.window, (255, 0, 0), rect, 2)
            
    def repaint_obstacles(self):
        for obstacle in self.model.get_obstacles_view():
            rect = self.reposition(obstacle.coords)
            if obstacle.enemy is not None:
                rect = self.reposition(obstacle.enemy.coords, False)
                self.window.blit(obstacle.enemy.current_animation, rect)
            self.window.blit(obstacle.object_img, (rect[0], rect[1]), (0, 0, rect[2], rect[3]), 0)
            if HITBOXES_ON:
                rect = self.reposition(obstacle.hitbox)
                pygame.draw.rect(self.window, (255, 0, 0), rect, 2)
        
    def reposition(self, rect, relative=True):
        if relative:
            return rect.move(self.player_left - self.model.x, self.player_bottom)
        else:
            return rect.move(self.player_left, self.player_bottom)

    def draw(self):
        self.repaint_background()
        self.repaint_obstacles()
        self.repaint_player()
