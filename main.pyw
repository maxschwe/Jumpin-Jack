from Controller.controller import Controller
import pygame
import random
import time
import traceback
import os

pygame.init()
random.seed(time.time())

WIDTH = 1200
HEIGHT = 800
FPS = 60

SPEED = 10
JUMP_FORCE = 20
GRAVITY = 1

PLAYER_X = 300
PLAYER_Y = 610


try:
    controller = Controller(WIDTH, HEIGHT, FPS, SPEED, JUMP_FORCE, GRAVITY, PLAYER_X, PLAYER_Y)
    controller.run()
except:
    if not os.path.exists("log"):
        os.mkdir("log")
    with open("log/error.log", "a") as f:
        f.write(traceback.format_exc())
