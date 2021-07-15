from Model.Entity.entity import Entity
import pygame

class Obstacle(Entity):
    def __init__(self, hitbox_coords, object_img_path, death=False):
        Entity.__init__(self, hitbox_coords)
        self.object_img = pygame.image.load(object_img_path)
        self.death = death
