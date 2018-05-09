import pygame
import sys
import os
import time
from pygame.locals import *
from random import randint


pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.mouse.set_visible(0)

pygame.mixer.init()
shot = pygame.mixer.Sound('sounds/blaster.wav')

pygame.mixer.init()
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(100)

clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 800))
pygame.mouse.set_visible(0)

width = window.get_width()
height = window.get_height()

myfont = pygame.font.SysFont("Arial", 30)

white = (255, 255, 255)
