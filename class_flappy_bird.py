import pygame 
from pygame.locals import  * 

import neat 
import time 
import os 
import sys 
import random
import pickle
pygame.font.init() 

WIN_WIDTH = 500 
WIN_HEIGHT = 800   #CAPITAL HENCE CONSTANT 
FLOOR = 730
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)
DRAW_LINES = False

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")


BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "bluebird-upflap.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "bluebird-midflap.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "bluebird-downflap.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "pipe-red.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon", "background-night.png")))



class Bird:
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
        self.vel = 0 
        self.height = self.y 
        self.img_count = 0 
        self.img = self.IMGS[0]
        self.tick_count = 0
    
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

        if d< 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
            else:
                if self.tilt > -90 :
                    self.tilt -=  self.ROT_VEL

    def draw(self, win):
        """
        draw the bird
        :param win: pygame window or surface
        :return: None
        """
        self.img_count += 1

        # For animation of bird, loop through three images
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # so when bird is nose diving it isn't flapping
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2


        # tilt the bird
        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe:
    '''
    property of the pipe how it should behave 

    '''
    GAP = 200 
    VEL = 5 

    def __init__(self,x):
        self.x = x 
        self.height = 0 

        #self.gap = 100
        
        self.top = 0 
        self.bottom = 0 
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM=  PIPE_IMG

        self.passed = False 
        self.set_height() 

    def set_height(self):
        self.height = random.randrange(50, 450 )
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL
    
    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM,(self.x, self.bottom))

    def collide(self, bird, win):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)
        
        if b_point or t_point:
            return True
        
        return False

class Base:
    '''
    property of the base class
    '''
    VEL = 5 
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG 

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0 :
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH <0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))




def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

