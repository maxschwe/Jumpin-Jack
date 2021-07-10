from Model.Entity.entity import Entity
from Model.Entity.enemy import Enemy
import pygame

class Obstacle(Entity):
    def __init__(self, hitbox_coords, object_img_path, death=False):
        Entity.__init__(self, hitbox_coords)
        self.object_img = pygame.image.load(object_img_path)
        self.death = death
        self.enemy = None

    def spawn_enemy(self):
        self.enemy = Enemy((self.coords.x, self.coords.y-self.coords.height, 120, 120), (0, 20, 120, 80), True)
        self.enemy = None