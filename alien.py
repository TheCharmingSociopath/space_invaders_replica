import pygame
import sys
import os
import time
from pygame.locals import *
from random import randint
from window import *


class class_trooper:
    xy = (int(width / 8), int(height / 8))
    tatti = pygame.image.load('images/tatti.jpg')
    tatti = pygame.transform.scale(tatti, xy)
    
    trooper_img = pygame.image.load('images/trooper.png')
    trooper_img = pygame.transform.scale(trooper_img, xy)

    def __init__(self):
        self.x = randint(0, 7) * width / 8
        self.y = randint(0, 1) * height / 8
        self.spawn_time = time.time()
        self.update_time = time.time()
        self.dir = randint(0, 1)
        self.frozen = False
        self.freeze_time = -1
        if self.dir == 1:
            self.dir = True
        else:
            self.dir = False

    def move(self, curr_time):
        self.update_time = curr_time
        if self.dir is True and self.x < 7 * width / 8:
            self.x += width / 8
            if self.x >= 7 * width / 8:
                self.dir = False
        elif self.dir is False and self.x > 0:
            self.x -= width / 8
            if self.x < width / 8:
                self.dir = True
        else:
            self.dir = not self.dir
