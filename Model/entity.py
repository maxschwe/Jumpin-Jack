import pygame

class Entity:
    def __init__(self, coords, coords_hitbox=()):
        self.coords = pygame.Rect(*coords)
        if coords_hitbox == ():
            self.hitbox = pygame.Rect(*coords)
        else:  
            hitbox_x = self.coords.x + coords_hitbox[0]
            hitbox_y = self.coords.y + coords_hitbox[1]
            hitbox_width = coords_hitbox[2]
            hitbox_height = coords_hitbox[3]
            self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)
            
    def move(self, x, y):
        self.coords.move_ip(x, y)
        self.hitbox.move_ip(x, y)
        
    def check_collision(self, object_hitbox):
        return self.hitbox.colliderect(object_hitbox) #hitbox = Rechteck 1 object = Rechteck 2
          