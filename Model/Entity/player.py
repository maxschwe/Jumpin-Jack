import pygame
from Model.Entity.entity import Entity

AMOUNT_PICTURES = 12
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
            self.walk_pos = 0
        self.update_current_animation()
            
    def left(self): # animation
        if not self.jumping:
            if self.walk_dir == "right":
                self.walk_pos = 0
            if self.walk_pos < AMOUNT_PICTURES - 1:
                self.walk_pos += 1
            else:
                self.walk_pos = 0
        else:
            self.walk_pos = 12

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
        else:
            self.walk_pos = 12
        
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
        predicted_rect = self.hitbox.copy()
        predicted_rect.x += x_screen + dx_screen
        predicted_rect.y += self.dy

        # check if player is on bottom
        if predicted_rect.bottom > y_screen:
            self.hitbox.bottom = y_screen
            self.coords.bottom = y_screen
            self.dy = 0
            self.jumping = False
            is_on_bottom = True
        else:
            is_on_bottom = False

        collided = False
        death = False
        for obstacle in current_obstacles:
            predicted_rect = self.hitbox.copy()
            predicted_rect.x += x_screen + dx_screen
            predicted_rect.y += self.dy
            
            if obstacle.check_collision(predicted_rect):
                if obstacle.death:
                    death = True
                if self.hitbox.bottom <= obstacle.hitbox.top and predicted_rect.bottom > obstacle.hitbox.top: #previous above, now collided (jumps from above)
                    collided = True
                    self.dy = obstacle.hitbox.top - self.hitbox.bottom
                elif self.hitbox.top >= obstacle.hitbox.bottom and predicted_rect.top < obstacle.hitbox.bottom: #previous below, now collided
                    self.vel_y = 0
                    self.dy = obstacle.hitbox.bottom - self.hitbox.top
                    
                elif (self.hitbox.right + x_screen) <= obstacle.hitbox.left and predicted_rect.right > obstacle.hitbox.left: # move right
                    dx_screen = obstacle.hitbox.left - (self.hitbox.right + x_screen)
            
                elif (self.hitbox.left + x_screen) >= obstacle.hitbox.right and predicted_rect.left < obstacle.hitbox.right: # move left
                    dx_screen = obstacle.hitbox.right - (self.hitbox.left + x_screen)
        old_jumping = self.jumping
        if collided:
            self.jumping = False
        elif not is_on_bottom:
            self.jumping = True
        if not self.jumping and old_jumping:
            self.walk_pos = 0
            self.update_current_animation()
        
            
        if predicted_rect.left < 0:
            dx_screen = - self.hitbox.left
        
        return dx_screen, death
            
    def update(self, x_screen, dx_screen, y_screen, current_obstacles):
        self.dy = 0
        self.physics()
        dx_screen, death = self.adjust_collision_values(x_screen, dx_screen, y_screen, current_obstacles)
        self.move(0, self.dy)
        return dx_screen, death
    
    def load_animation_img(self):
        for key, img_list in {"L":self.facing_left_img, "R":self.facing_right_img}.items():
            for i in range(1, AMOUNT_PICTURES + 2):
                img = pygame.image.load(f"{PATH_IMAGES}{key}{str(i)}.png")
                img = pygame.transform.scale(img, (self.coords.width, self.coords.height))
                img_list.append(img)
