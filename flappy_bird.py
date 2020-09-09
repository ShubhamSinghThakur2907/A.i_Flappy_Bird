import pygame 
import neat 
import time 
import os 
import random

WIN_WIDTH = 500 
WIN_HEIGHT = 800   #CAPITAL HENCE CONSTANT 

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
        return pygame,mask.from_surface(self.img)

def draw_window(win, bird):
    win.blit(BG_IMG,(0,0))
    bird.draw(win)
    pygame.display.update()

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

def main():
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True 
    while run:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bird.move()
        draw_window(win, bird)

    pygame.quit()
    quit()

main()
