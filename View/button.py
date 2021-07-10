import pygame

class Button:
    def __init__(self, x, y, width, height, col):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = col
        self.square = self.get_rect()
        self.border = False

    def check_if_clicked(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def setBorder(self,visibility):
        self.border = visibility

    def draw(self, window):
        print("BUTTON1")
        pygame.draw.rect(window, self.color, self.square)
        if self.border:
            print("BUTTON2")
            pygame.draw.rect(window, "blue", self.square, 2 if self.border else 0)
