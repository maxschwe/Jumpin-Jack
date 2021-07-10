import pygame
from Model.Entity.entity import Entity

PATH_IMAGES_AIR = "Images/Enemy/flying"
PATH_IMAGES_GROUND = "Images/Enemy/ground"
AMOUNT_IMAGES_AIR = 1
AMOUNT_IMAGES_GROUND = 1

class Enemy(Entity):
    def __init__(self, coords, hitbox, flying):
        Entity.__init__(self, coords, hitbox)
        # self.flying = flying
        self.flying = True
        if self.flying:
            self.amount_img = AMOUNT_IMAGES_AIR
        else:
            self.amount_img = AMOUNT_IMAGES_GROUND
        self.walk_pos = 0
        self.walk_dir = "right"
        self.facing_left_img = []
        self.facing_right_img = []
        # self.load_animation_img()
        # self.update_current_animation()
            
    def left(self): # animation
        if not self.jumping:
            if self.walk_dir == "right":
                self.walk_pos = 0
            if self.walk_pos < self.amount_img - 1:
                self.walk_pos += 1
            else:
                self.walk_pos = 0
        else:
            self.walk_pos = 0

        if self.walk_dir == "right":
            self.walk_dir = "left"
        self.update_current_animation()
        
    def right(self):
        if not self.jumping:
            if self.walk_dir == "left":
                self.walk_pos = 0
            if self.walk_pos < self.amount_img - 1:
                self.walk_pos += 1
            else:
                self.walk_pos = 0
        else:
            self.walk_pos = 0
        
        if self.walk_dir == "left":
            self.walk_dir = "right"
            
        self.update_current_animation()
                
    def update_current_animation(self):
        if self.walk_dir == "left":
            self.current_animation = self.facing_left_img[self.walk_pos]
        else:
            self.current_animation = self.facing_right_img[self.walk_pos]
            
    def update(self):
        pass
        # self.left()
    
    def load_animation_img(self):
        for key, img_list in {"L":self.facing_left_img, "R":self.facing_right_img}.items():
            for i in range(1, self.amount_img + 1):
                img = pygame.image.load(f"{self.amount_img}{key}{str(i)}.png")
                img = pygame.transform.scale(img, (self.coords.width, self.coords.height))
                img_list.append(img)
