import pygame
from Model.entity import Entity

AMOUNT_PICTURES = 9
PATH_IMAGES = "Images/Player/"

class Player(Entity):
    def __init__(self, coords, hitbox, jump_force, gravity):
        Entity.__init__(self, coords, hitbox)
        self.jumping = False
        self.jump_force = jump_force
        self.gravity = gravity
        self.vel_y = 0
        self.dy = 0
        self.walk_pos = 0
        self.walk_dir = "right"
        self.facing_left_img = []
        self.facing_right_img = []
        self.load_animation_img()
        self.update_current_animation()
        
    def space(self):
        if not self.jumping: # if not in air
            self.jumping = True
            self.vel_y = -self.jump_force
            
    def left(self): # animation
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
        
    def physics(self):
        if not self.jumping:
            self.vel_y = 0
            
        self.vel_y += self.gravity
        
        self.dy += self.vel_y
        
    def adjust_collision_values(self, x_screen, y_screen, dx_screen, current_obstacles):
        # check if player collides with objects by y-direction
        for obstacle in current_obstacles:
            predicted_rect = self.hitbox.copy()
            predicted_rect.x += x_screen + dx_screen
            predicted_rect.y += self.dy
            if obstacle.check_collision(predicted_rect):
                # wenns in y-richtung überschneidet
                if self.dy > 0: # moves down
                    self.dy = obstacle.hitbox.top - self.hitbox.bottom
                    
                elif self.dy < 0: # moves up 
                    self.dy = obstacle.hitbox.bottom - self.hitbox.top
                self.jumping = False
            else:
                self.jumping = True
        # check if player is on bottom
        if predicted_rect.bottom > y_screen:
            self.hitbox.bottom = y_screen
            self.coords.bottom = y_screen
            self.dy = 0
            self.jumping = False

                        
    def update(self, x_screen, dx_screen, y_screen, current_obstacles):
        self.dy = 0
        self.physics()
        self.adjust_collision_values(x_screen, dx_screen, y_screen, current_obstacles)
        self.move(0, self.dy)
        # self.check_collision_horizontal(x_pos_player)
    
    def load_animation_img(self):
        for key, img_list in {"L":self.facing_left_img, "R":self.facing_right_img}.items():
            for i in range(1, AMOUNT_PICTURES + 1):
                img = pygame.image.load(f"{PATH_IMAGES}{key}{str(i)}.png")
                img = pygame.transform.scale(img, (self.coords.width, self.coords.height))
                img_list.append(img)
        