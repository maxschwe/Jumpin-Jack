from Controller.controller import Controller
import pygame
import random
import time

pygame.init()
random.seed(time.time())

WIDTH = 1000
HEIGHT = 800
FPS = 60

SPEED = 10

PLAYER_X = 300
PLAYER_Y = 610

controller = Controller(WIDTH, HEIGHT, FPS, SPEED, PLAYER_X, PLAYER_Y)
controller.run()
