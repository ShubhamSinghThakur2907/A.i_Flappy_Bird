import pygame 
import neat 
import time 
import os 
import random

WIN_WIDTH = 600 
WIN_HEIGHT = 800   #CAPITAL HENCE CONSTANT 

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "bluebird-upflap.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "bluebird-midflap.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "bluebird-downflap.png")))]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "pipe-red.png")))

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "base.png")))

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "background-night.png")))


class bird:
    """
    IMGS : images of the flappy bird 
    MAX_ROTATION : maximum rotation that flappy bird can take (tilt)
    ROT_VAL : the velocity of the rotation per frame 
    ANIMATION_TIME : how much the bird can fly in a frame  
    """
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 
    ROT_VEL = 20
    ANIMATION_TIME = 5 

    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.tilt = 0 
        self.vol = 0 
        self.height = self.y 
        self.img_count = 0 
        self.img = self.IMGS[0]
    
    def jump(self):
        self.vel = -10.5
        self.tick_count = 0 
        self.height = self.y 

    def move(self):
        self.tick_count += 1 

        d = self.vel*self.tick_count + 1.5*self.tick_count **2 

        if d>= 16:
            d = 16 

        if  d< 0 :
            d -= 2

        self.y = self.y + 4 

        if d< 0 or self.y = self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
            else:
                if self.tilt > -90 :
                    self.tilt -=  self.ROT_VEL

        
        

while True:
    bird.move()

