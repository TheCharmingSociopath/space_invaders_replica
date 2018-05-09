import pygame, sys, os, time
from pygame.locals import *
from random import randint

clock = pygame.time.Clock()
window = pygame.display.set_mode((800,800))
pygame.mouse.set_visible(0)
lazer_list = []
trooper_list = []
freeze_list = []

class class_falcon:
	def __init__(self):
		self.falcon_img = pygame.image.load('images/falcon.png')
		self.falcony = window.get_height() - self.falcon_img.get_height()
		self.falconx = window.get_width() - self.falcon_img.get_width()

class parent_lazers:
	def __init__(self, falcon):
		self.lazerx = falcon.falconx
		self.lazery = window.get_height() - falcon.falcon_img.get_height() - self.lazer.get_height()
	
	def move(self):
		self.lazery -= 10

class class_lazer(parent_lazers):
	def __init__(self, falcon):
		self.lazer = pygame.image.load('images/lazer.png')
		parent_lazers.__init__(self, falcon)

class class_freeze(parent_lazers):
	def __init__(self, falcon):
		self.lazer = pygame.image.load('images/freeze.gif')
		parent_lazers.__init__(self, falcon)

class class_trooper:

	def __init__(self):
		self.trooper_img = pygame.image.load('images/trooper.png')
		self.trooperx = randint(0, 7) * 100
		self.troopery = randint(0, 1) * 100
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
		if self.dir == True and self.trooperx < 700:
			self.trooperx += 100
			if self.trooperx >= 700:
				self.dir = False
		elif self.dir == False and self.trooperx > 10:
			self.trooperx -= 100
			if self.trooperx < 100:
				self.dir = True
		else:
			self.dir = not self.dir

falcon = class_falcon()
tim = time.time()
score = 0
new_trooper = class_trooper()
trooper_list.append(new_trooper)
window.blit(new_trooper.trooper_img, (new_trooper.trooperx, new_trooper.troopery))

while True:
	clock.tick(60)
	window.fill((0, 0, 0))
	
	curr_time = time.time()

	#print falcon
	window.blit(falcon.falcon_img, (falcon.falconx, falcon.falcony))

	#create troopers
	if curr_time >= tim + 2:
		new_trooper = class_trooper()
		trooper_list.append(new_trooper)
		window.blit(new_trooper.trooper_img, (new_trooper.trooperx, new_trooper.troopery))
		tim = curr_time
	
	#update troopers
	for trooper in trooper_list:
		# destroy
		if curr_time >= trooper.spawn_time + 8:
			trooper_list.pop(trooper_list.index(trooper))

		for lazer in lazer_list:
			if lazer.lazery <= trooper.troopery and lazer.lazerx == trooper.trooperx:
				lazer_list.pop(lazer_list.index(lazer))
				trooper_list.pop(trooper_list.index(trooper))
				score += 1
				break

		for lazer in freeze_list:
			if lazer.lazery <= trooper.troopery and lazer.lazerx == trooper.trooperx:
				trooper.frozen = True
				trooper.freeze_time = curr_time
				break

	for trooper in trooper_list:			
		if trooper.frozen == True:
			if trooper.freeze_time + 5 <= curr_time:
				trooper.frozen = False
			else:
				window.blit(trooper.trooper_img, (trooper.trooperx, trooper.troopery))
				continue	
		elif curr_time - trooper.update_time >= 1:
			trooper.move(curr_time)
		window.blit(trooper.trooper_img, (trooper.trooperx, trooper.troopery))

	#update lazers
	for lazer in lazer_list:
		if lazer.lazery > 0:
			lazer.move()
			window.blit(lazer.lazer, (lazer.lazerx, lazer.lazery))
		else:
			lazer_list.pop(lazer_list.index(lazer))

	for lazer in freeze_list:
		if lazer.lazery > 0:
			lazer.move()
			window.blit(lazer.lazer, (lazer.lazerx, lazer.lazery))
		else:
			freeze_list.pop(freeze_list.index(lazer))

	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			sys.exit()

		if event.type == pygame.KEYDOWN:
			
			if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and falcon.falconx > 0:
				falcon.falconx -= 100
			
			elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and falcon.falconx < 700:
				falcon.falconx += 100
			
			elif (event.key == pygame.K_SPACE):
				new_lazer = class_lazer(falcon)
				lazer_list.append(new_lazer)
				window.blit(new_lazer.lazer, (new_lazer.lazerx, new_lazer.lazery))
			
			elif (event.key == pygame.K_i):
				new_freeze = class_freeze(falcon)
				freeze_list.append(new_freeze)
				window.blit(new_freeze.lazer, (new_freeze.lazerx, new_freeze.lazery))
	pygame.display.update()
