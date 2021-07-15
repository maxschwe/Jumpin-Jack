import pygame
from Model.Entity.entity import Entity

# Anzahl Spieler Animationsbilder, eine Richtung
AMOUNT_PICTURES = 12

# Pfad zu Spieler Animationsbildern
PATH_IMAGES = "Images/Player/"

class Player(Entity):
    def __init__(self, coords, hitbox, jump_force, gravity):
        # setup with specified values
        Entity.__init__(self, coords, hitbox)

        # jump_force and gravity can be changed in main.pyw
        self.jump_force = jump_force
        self.gravity = gravity

        # initializes with starting values
        self.jumping = False
        self.vel_y = 0
        self.dy = 0
        self.walk_pos = 0
        self.walk_dir = "right"
        self.facing_left_img = []
        self.facing_right_img = []

        self.load_animation_img()
        self.update_current_animation()
    
    # Leertaste gedrückt
    def space(self):
        # wenn er nicht bereits springt (vermeidet Doppel-Jump)
        if not self.jumping:
            self.jumping = True

            # vel_y = Änderung der y-Position pro Update (wird durch Gravitation verringert)
            self.vel_y = -self.jump_force
            
            # setzt walk_pos zu Sprungbild (ist das letzte der geladenen Bilder)
            self.walk_pos = AMOUNT_PICTURES
        
        # updatet aktuelles Animationsbild
        self.update_current_animation()
    
    # Linke Pfeiltaste gedrückt
    def left(self):
        # wenn er nicht gerade springt
        if not self.jumping:

            # wenn er die Richtung geändert hat
            if self.walk_dir == "right":
                # reset walk_pos
                self.walk_pos = 0

            # wenn das es noch ein Animationsbild nach dem Aktuellen gibt
            elif self.walk_pos < AMOUNT_PICTURES - 1:
                # Zähler erhöhen
                self.walk_pos += 1
            
            # ansonsten
            else:
                # reset auf 0
                self.walk_pos = 0
        # wenn er springt
        else:
            # setzt walk_pos zu Sprungbild (ist das letzte der geladenen Bilder)
            self.walk_pos = AMOUNT_PICTURES

        # wenn sich die Richtung geändert hat updated er die Variable walk_dir
        if self.walk_dir == "right":
            self.walk_dir = "left"

        # # updatet aktuelles Animationsbild 
        self.update_current_animation()

    # Rechte Pfeiltaste gedrückt
    def right(self):
        # wenn er nicht gerade springt
        if not self.jumping:

            # wenn er die Richtung geändert hat
            if self.walk_dir == "left":
                # reset walk_pos
                self.walk_pos = 0

            # wenn das es noch ein Animationsbild nach dem Aktuellen gibt
            elif self.walk_pos < AMOUNT_PICTURES - 1:
                # Zähler erhöhen
                self.walk_pos += 1
            
            # ansonsten
            else:
                # reset auf 0
                self.walk_pos = 0
        # wenn er springt
        else:
            # setzt walk_pos zu Sprungbild (ist das letzte der geladenen Bilder)
            self.walk_pos = AMOUNT_PICTURES

        # wenn sich die Richtung geändert hat updated er die Variable walk_dir
        if self.walk_dir == "left":
            self.walk_dir = "right"

        # updatet aktuelles Animationsbild 
        self.update_current_animation()

    # updatet current_animation (wird gebraucht von GamePanel)      
    def update_current_animation(self):
        # je nach Bewegungsrichtung wird facing_left oder facing_right verwendet
        if self.walk_dir == "left":
            self.current_animation = self.facing_left_img[self.walk_pos]
        else:
            self.current_animation = self.facing_right_img[self.walk_pos]
    
    # Berechnet Einfluss der Gravitation
    def physics(self):
        # wenn er nicht mehr springt: aktuelle y-Änderung (Beschleunigung) = 0
        if not self.jumping:
            self.vel_y = 0
        
        # Beschleunigung wird durch Gravitation erhöht
        self.vel_y += self.gravity
        
        # y-Änderung im Vergleich zum letzten Update
        self.dy += self.vel_y
        
    def adjust_collision_values(self, x_screen, y_screen, dx_screen, current_obstacles):
        
        # Berechnet die Hitbox mit absoluten Koordinaten des Spielers, 
        # nachdem er sich für diesen Durchlauf bewegt hat
        # x_screen: gelaufene Strecke, dx_screen: x-Änderung im Vergleich zum letzten Update, 
        # self.dy: y-Änderung im Vergleich zum letzten Update

        predicted_rect = self.hitbox.copy()
        predicted_rect.x += x_screen + dx_screen
        predicted_rect.y += self.dy

        # überprüft, ob sich der Spieler niedriger als der Boden befindet
        if predicted_rect.bottom > y_screen:
            # setzt Spieler auf die Höhe des Bodens
            self.hitbox.bottom = y_screen
            self.coords.bottom = y_screen
            self.dy = 0

            # setzt jumping auf Falsch, weil der den Boden berührt
            self.jumping = False
            is_on_bottom = True
        else:
            is_on_bottom = False

        stopped_jumping = False
        death = False

        # iteriert über alle Obstacles, die von aktueller Bedeutung sind, 
        # von den Chunks, in denen sich der Spieler befindet (erhalten von Model)
        for obstacle in current_obstacles:
            # berechnet absolute Position der Obstacle nachdem es sich für diesen Durchlauf bewegt hat
            predicted_rect = self.hitbox.copy()
            predicted_rect.x += x_screen + dx_screen
            predicted_rect.y += self.dy
            
            # überprüft, ob eine Kollision vorliegt
            if obstacle.check_collision(predicted_rect):
                # wenn man an dem Obstacle stirbt: death=True
                if obstacle.death:
                    death = True
                
                # zuerst war die Hitbox des Spielers höher als die Hitbox des Obstacles,
                # nach dem Update ist die Hitbox aber niedriger als die Hitbox des Obstacles
                # -> springt von oben auf das Hindernis
                if self.hitbox.bottom <= obstacle.hitbox.top and predicted_rect.bottom > obstacle.hitbox.top:
                    stopped_jumping = True
                    # setzt Spieler genau auf die Hitbox des Hindernisses
                    self.dy = obstacle.hitbox.top - self.hitbox.bottom

                # zuerst war die Hitbox des Spielers niedriger als die Hitbox des Obstacles,
                # nach dem Update ist die Hitbox aber höher als die Hitbox des Obstacles
                # -> springt von unten gegen das Hindernis
                elif self.hitbox.top >= obstacle.hitbox.bottom and predicted_rect.top < obstacle.hitbox.bottom:
                    # setzt Sprungkraft auf 0 (=Abbremsung)
                    self.vel_y = 0

                    # setzt Spieler Hitbox genau unter die Hitbox des Hindernisses
                    self.dy = obstacle.hitbox.bottom - self.hitbox.top
                
                # zuerst war die Hitbox des Spielers links von dem Hindernis, dann reingelaufen
                # ist von links in das Hindernis gelaufen
                elif (self.hitbox.right + x_screen) <= obstacle.hitbox.left and predicted_rect.right > obstacle.hitbox.left:
                    # setzt Spieler Hitbox genau an die linke Kante des Hindernisses
                    dx_screen = obstacle.hitbox.left - (self.hitbox.right + x_screen)

                # zuerst war die Hitbox des Spielers rechts von dem Hindernis, dann reingelaufen
                # ist von rechts in das Hindernis gelaufen
                elif (self.hitbox.left + x_screen) >= obstacle.hitbox.right and predicted_rect.left < obstacle.hitbox.right:
                    # setzt Spieler Hitbox genau an die rechte Kante des Hindernisses
                    dx_screen = obstacle.hitbox.right - (self.hitbox.left + x_screen)

        old_jumping = self.jumping

        # wenn er auf ein Hindernis gesprungen ist jumping=False
        if stopped_jumping:
            self.jumping = False

        # wenn er nicht den Boden berührt und nicht auf ein Hindernis gesprungen ist
        elif not is_on_bottom:
            self.jumping = True

        # wenn er gerade aufgehört hat zu springen: Beenden der Sprunganimation
        if not self.jumping and old_jumping:
            self.walk_pos = 0
            self.update_current_animation()
        
        # wenn er links aus der Map laufen würde: Reset Position auf 0
        if predicted_rect.left < 0:
            dx_screen = - self.hitbox.left
        
        return dx_screen, death

    # wird von Model aufgerufen bei jedem Update (so oft, wie fps angegeben sind)  
    def update(self, x_screen, dx_screen, y_screen, current_obstacles):
        # self.dy: Änderung der y-Koordinaten im Vergleich zum letzten Update
        self.dy = 0

        # berechnet Einfluss der Gravitation
        self.physics()

        # überprüft auf Kollisionen
        dx_screen, death = self.adjust_collision_values(x_screen, dx_screen, y_screen, current_obstacles)

        # bewegt Spielerhitbox um berechnetes dy
        self.move(0, self.dy)

        # gibt die Änderung der x-Koordinate zurück und ob der Spieler gestorben ist
        return dx_screen, death
    
    # Lädt die Animationsbilder des Spielers
    def load_animation_img(self):
        # L1-L13 für Links zeigende Bilder, R1-R13 für Rechts zeigende Bilder
        for key, img_list in {"L":self.facing_left_img, "R":self.facing_right_img}.items():
            for i in range(1, AMOUNT_PICTURES + 2):
                # Bild laden
                img = pygame.image.load(f"{PATH_IMAGES}{key}{str(i)}.png")
                # Bild auf Größe scalen
                img = pygame.transform.scale(img, (self.coords.width, self.coords.height))
                # zu Liste hinzufügen
                img_list.append(img)
