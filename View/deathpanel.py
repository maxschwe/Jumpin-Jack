from .panel import Panel
import pygame

class DeathPanel(Panel):
    def __init__(self, window, dimensions):
        self.game_over_text = pygame.font.SysFont("Segoe", 80)
        self.highscore_text = pygame.font.SysFont("Segoe", 60)
        self.restart_text = pygame.font.SysFont("Segoe", 70)
        self.window = window
        self.dimensions = dimensions
        
        self.score = 0
        self.updated = False
    
    def draw(self):
        heading = self.game_over_text.render('Game over!', True, (219, 101, 55))
        self.window.blit(heading, ((self.dimensions[0]/2 - heading.get_rect().width/2,self.dimensions[1]/2-heading.get_rect().height/2 - 60)))
         
        if self.updated:
            text_score = 'New Highscore! Score: ' + str(self.score)
        else:
            text_score = 'Score: ' + str(self.score)

        scoreField = self.highscore_text.render(text_score, True, (219, 101, 55))
        
        self.window.blit(scoreField, ((self.dimensions[0]/2 - scoreField.get_rect().width/2,self.dimensions[1]/2-scoreField.get_rect().height/2 +20)))

        restartField = self.restart_text.render("Press Enter to restart!", True, (255, 255, 255))
        
        self.window.blit(restartField, ((self.dimensions[0]/2 - restartField.get_rect().width/2,self.dimensions[1]/2-restartField.get_rect().height/2 +320)))

    def set_score(self, score, updated):
        self.score = score
        self.updated = updated