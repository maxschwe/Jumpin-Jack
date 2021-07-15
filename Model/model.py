import pygame
import json
import random
import time

from Model.Entity.player import Player
from Model.Entity.obstacle import Obstacle
from Model.world.world import World

class Model:
    def __init__(self, width, height, speed, jump_force, gravity):
        self.width = width
        self.height = height
        self.load_data()
        self.observers = []
        background_unscaled = pygame.image.load("Images/hintergrund.png")
        startscreen_unscaled = pygame.image.load("Images/startscreen/startscreen.png")
        self.background = pygame.transform.scale(background_unscaled, (self.width, self.height))
        self.start_screen = pygame.transform.scale(startscreen_unscaled, (self.width, self.height))
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.speed = speed
        self.jumping = False
        self.player = Player((0, 0, 120, 120), (27, 0, 66, 120), jump_force=jump_force, gravity=gravity)
        self.world = World()
        self.start = True
        self.alive = False
        
    def add_observer(self, observer): 
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)
        
    def update_observers(self):
        for observer in self.observers:
            observer.update()

    def get_dimension(self):
        return (self.width, self.height)
    
    def left_key(self):
        self.dx -= self.speed
        self.player.left()
        self.update_observers()
        self.alive = True
        return self.alive
    
    def right_key(self):
        self.dx += self.speed
        self.player.right()
        self.update_observers()
        self.alive = True
        return self.alive
    
    def space_key(self):
        self.player.space()
        
    def get_obstacles_view(self):
        return self.world.get_current_obstacles_view()

    def update_game(self):
        self.dx, death = self.player.update(self.x, self.y, self.dx, self.world.get_current_obstacles(self.x + self.dx, self.player.hitbox.width))
        self.x += self.dx
        self.y += self.dy
        self.world.update(self.x)
        
        if death:
            self.alive = False
            self.onDeath()
        if self.alive:
            self.update_observers()
        self.dx = 0
        self.dy = 0

    def onDeath(self):
        updated = self.updateHighscore()
        for observer in self.observers:
            observer.panel.draw()
            observer.change_panel(2)
            observer.panel.set_score(self.score, updated)
            observer.panel.draw()
            pygame.display.update()

    def restart_game(self):
        self.start = False
        self.alive = True
        self.world.reset()

        self.x = 0
        for observer in self.observers:
            observer.change_panel(1)

    def load_data(self):
        try:
            with open("model/data/scores.json") as f:
                data = json.load(f)
            self.highscore = data["highscore"]
        except:
            self.highscore = 0
            self.save_data()

    def updateHighscore(self):
        updated = False
        score = int(self.x/10) * 10
        if score > self.highscore:
            updated = True
            self.highscore = score
        self.score = score
        self.save_data()
        return updated

    def save_data(self):
        data = {}
        data["highscore"] = self.highscore
        with open("model/data/scores.json", "w") as f:
            json.dump(data, f, indent=4)
