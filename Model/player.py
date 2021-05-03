import pygame

AMOUNT_PICTURES = 9
PATH_IMAGES = "Images/Player/"

class Player:
    def __init__(self, x_pos, y_pos, width, height):
        self.x = x_pos
        self.y = y_pos - height
        self.width = width
        self.height = height
        self.jumping = False
        self.jump_pos = -10
        self.walk_pos = 0
        self.walk_dir = "right"
        self.facing_left_img = []
        self.facing_right_img = []
        self.load_animation_img()
        self.update_current_animation()
        
        
    def space(self):
        if not self.jumping:
            self.jumping = True 
            
    def left(self):
        if not self.jumping:
            if self.walk_dir == "right":
                self.walk_pos = 0
            if self.walk_pos < AMOUNT_PICTURES - 1:
                self.walk_pos += 1
            else:
                self.walk_pos = 0
        if self.walk_dir == "right":
            self.walk_dir = "left"
        self.update_current_animation()
        
    def right(self):
        if not self.jumping:
            if self.walk_dir == "left":
                self.walk_pos = 0
            if self.walk_pos < AMOUNT_PICTURES - 1:
                self.walk_pos += 1
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
        
    def update_jump(self):        
        if self.jumping:
            if self.jump_pos > 10:
                self.jumping = False
                self.jump_pos = -10
                pass
            else: # kleiner als 1
                faktor = 0.25 * round(self.jump_pos ** 2, 2)
                if self.jump_pos < 0:
                    faktor = -faktor
                self.y = self.y + faktor
                self.jump_pos += 0.5
                self.jump_pos = round(self.jump_pos, 1)
                
    def update(self):
        self.update_jump()
        
    def get_properties(self):
        return (self.x, self.y)
    
    def load_animation_img(self):
        for key, img_list in {"L":self.facing_left_img, "R":self.facing_right_img}.items():
            for i in range(1, AMOUNT_PICTURES + 1):
                img = pygame.image.load(f"{PATH_IMAGES}{key}{str(i)}.png")
                img = pygame.transform.scale(img, (self.width, self.height))
                img_list.append(img)
        