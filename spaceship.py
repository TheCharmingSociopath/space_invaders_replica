import pygame
import sys
import os
import time
from pygame.locals import *
from random import randint
from window import *


class class_falcon:
    falcon_img = pygame.image.load('images/falcon.png')
    falcon_img = pygame.transform.scale(falcon_img, (int(width / 8), int(height / 8)))

    def __init__(self):
        self.y = height - self.falcon_img.get_height()
        self.x = width - self.falcon_img.get_width()
