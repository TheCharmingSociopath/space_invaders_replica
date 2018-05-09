import pygame
import sys
import os
import time
from pygame.locals import *
from random import randint
from window import *


class parent_lazers:
    def __init__(self, falcon):
        self.x = falcon.x
        self.y = height - falcon.falcon_img.get_height() - self.lazer.get_height()

    def move(self):
        self.y -= 10


class class_lazer(parent_lazers):
    lazer = pygame.image.load('images/lazer.png')
    lazer = pygame.transform.scale(lazer, (int(width / 8), int(height / 8)))

    def __init__(self, falcon):
        parent_lazers.__init__(self, falcon)


class class_freeze(parent_lazers):
    lazer = pygame.image.load('images/freeze.gif')
    lazer = pygame.transform.scale(lazer, (int(width / 8), int(height / 8)))

    def __init__(self, falcon):
        parent_lazers.__init__(self, falcon)
