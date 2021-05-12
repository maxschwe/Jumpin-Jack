
import sys
import os
import pygame
# sys.path.append(os.path.realpath('../JumpingJack'))
from Model.modelbeobachter import ModelBeobachter


HITBOXES_ON = True


class View(ModelBeobachter):
    def __init__(self, model, player_left, player_bottom):
        self.model = model
        self.player_left = player_left
        self.player_bottom = player_bottom
        self.model.add_observer(self)
        self.dimensions = self.model.get_dimension()
        self.window = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption("Jumpin' Jack")
        pygame.init()
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
        self.window.blit(self.model.background, (- (self.model.x % self.model.width), 0))
        self.window.blit(self.model.background, (self.model.width - (self.model.x % self.model.width), 0))
        
    def repaint_player(self):
        rect = self.reposition(self.model.player.coords, False)
        self.window.blit(self.model.player.current_animation, rect)
        
    def reposition(self, rect, relative=True):
        if relative:
            return rect.move(self.player_left - self.model.x, self.player_bottom)
        else:
            return rect.move(self.player_left, self.player_bottom)
        
    def repaint_obstacle(self):
        rect = self.reposition(self.model.obstacle.coords)
        pygame.draw.rect(self.window, (0, 255, 0), rect) # coords von objekt bleibt konstant

    def repaint_hitboxes(self):
        rect = self.reposition(self.model.player.hitbox, False)
        pygame.draw.rect(self.window, (255, 0, 0), rect, 2)
        rect = self.reposition(self.model.obstacle.hitbox)
        pygame.draw.rect(self.window, (255, 0, 0), rect, 2)
        
    def show_death_screen(self):
        game_over_text = pygame.font.SysFont(None, 80)
        textsurface = game_over_text.render('Game over!', True, (255,255,255))
        self.window.blit(textsurface, ((self.dimensions[0]/2 - textsurface.get_rect().width/2,self.dimensions[1]/2-textsurface.get_rect().height/2 - 40)))
        pygame.display.update()


        print("Pure death baby")


    def update(self):
        self.repaint()
            