import pygame
import sys
import os
import time
from pygame.locals import *
from random import randint
from spaceship import *
from alien import *
from lazer import *
from window import *


lazer_list = []
trooper_list = []
freeze_list = []

falcon = class_falcon()
tim = time.time()
score = 0
new_trooper = class_trooper()
trooper_list.append(new_trooper)
window.blit(class_trooper.trooper_img, (new_trooper.x, new_trooper.y))

f = open('high_score.txt', 'r+')
high_score = int(f.readline())
f.seek(0)
f.truncate()

while True:
    clock.tick(60)
    window.fill((0, 0, 0))

    curr_time = time.time()

    # print falcon
    window.blit(class_falcon.falcon_img, (falcon.x, falcon.y))

    # create troopers
    if curr_time >= tim + 2:
        new_trooper = class_trooper()
        trooper_list.append(new_trooper)
        window.blit(new_trooper.trooper_img, (new_trooper.x, new_trooper.y))
        tim = curr_time

    # update troopers
    for trooper in trooper_list:
        # destroy
        if curr_time >= trooper.spawn_time + 8 and trooper_list != []:
            trooper_list.pop(trooper_list.index(trooper))

        for lazer in lazer_list:
            if trooper_list != [] and lazer.y <= trooper.y:
            	if lazer.x == trooper.x:
                    lazer_list.pop(lazer_list.index(lazer))
                    trooper_list.pop(trooper_list.index(trooper))
                    score += 1
                    break

        for lazer in freeze_list:
            if lazer.y <= trooper.y and lazer.x == trooper.x:
                trooper.frozen = True
                trooper.freeze_time = curr_time
                break

    for trooper in trooper_list:
        if trooper.frozen is True:
            if trooper.freeze_time + 5 <= curr_time:
                trooper.frozen = False
            else:
                window.blit(class_trooper.tatti, (trooper.x, trooper.y))
                continue
        elif curr_time - trooper.update_time >= 1:
            trooper.move(curr_time)
        window.blit(trooper.trooper_img, (trooper.x, trooper.y))

    # update lazers
    for lazer in lazer_list:
        if lazer.y > 0:
            lazer.move()
            window.blit(lazer.lazer, (lazer.x, lazer.y))
        elif lazer_list != []:
            lazer_list.pop(lazer_list.index(lazer))

    for lazer in freeze_list:
        if lazer.y > 0:
            lazer.move()
            window.blit(lazer.lazer, (lazer.x, lazer.y))
        elif freeze_list != []:
            freeze_list.pop(freeze_list.index(lazer))

    # event loop
    for event in pygame.event.get():
        cond = (event.type == pygame.KEYDOWN and event.key == pygame.K_q)
        if event.type == pygame.QUIT or cond:
            high_score = max(high_score, score)
            f.write(str(high_score) + '\n')
            f.close()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if falcon.x > 0:
                    falcon.x -= 100

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if falcon.x < 700:
                    falcon.x += 100

            elif (event.key == pygame.K_SPACE):
                shot.play()
                new_lazer = class_lazer(falcon)
                lazer_list.append(new_lazer)
                window.blit(new_lazer.lazer, (new_lazer.x, new_lazer.y))

            elif (event.key == pygame.K_s):
                shot.play()
                new_freeze = class_freeze(falcon)
                freeze_list.append(new_freeze)
                window.blit(new_freeze.lazer, (new_freeze.x, new_freeze.y))
    score_text = myfont.render("Score: " + str(score), True, white)
    high_score_txt = myfont.render('High Score: ' + str(high_score), True, white)
    window.blit(score_text, (0, height / 2))
    window.blit(high_score_txt, (0, height / 2 + 30))
    pygame.display.update()
