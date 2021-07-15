from .panel import Panel
import pygame

# Variable: Hitboxen on/off
HITBOXES_ON = False
class GamePanel(Panel):
    # Konstruktor
    def __init__(self, window, dimensions, player_left, player_bottom, model):
        self.window = window
        self.dimensions = dimensions

        self.player_left = player_left
        self.player_bottom = player_bottom
        self.model = model

    # die Methode zeichnet den Hintergrund im Fenster
    def repaint_background(self):
        # linker Teil des Hintergrunds
        self.window.blit(self.model.background, (- (self.model.x % self.model.width), 0))

        # rechter Teil des Hintergrunds
        self.window.blit(self.model.background, (self.model.width - (self.model.x % self.model.width), 0))
    
    # die Methode zeichnet den Spieler im Fenster
    def repaint_player(self):
        rect = self.reposition(self.model.player.coords, False)
        self.window.blit(self.model.player.current_animation, rect)
        if HITBOXES_ON:
            rect = self.reposition(self.model.player.hitbox, False)
            pygame.draw.rect(self.window, (255, 0, 0), rect, 2)

    # die Methode zeichnet die Objekte im Fenster      
    def repaint_obstacles(self):
        for obstacle in self.model.get_obstacles_view():
            rect = self.reposition(obstacle.coords, True)
            self.window.blit(obstacle.object_img, (rect[0], rect[1]), (0, 0, rect[2], rect[3]), 0)
            if HITBOXES_ON:
                rect = self.reposition(obstacle.hitbox)
                pygame.draw.rect(self.window, (255, 0, 0), rect, 2)

    # die Koordinaten werden so angepasst, dass sie relativ zu dem gelaufenen Weg sind, wenn relative=True
    # und den in main.pyw festgelegten Abstand zum linken Rand und zum Boden haben
    def reposition(self, rect, relative=True):
        if relative:
            return rect.move(self.player_left - self.model.x, self.player_bottom)
        else:
            return rect.move(self.player_left, self.player_bottom)

    # die Methode wird 60 mal in der Sekunde von View aufgerufen, um alles zu zeichnen
    def draw(self):
        self.repaint_background()
        self.repaint_obstacles()
        self.repaint_player()
