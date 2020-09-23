import pygame 
import neat 
import time 
import os 
import random 


WIN_WIDTH =  600 
WIN_HEIGHT = 800 

#loading assets

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets","icon","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets","icon","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets","icon","bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets","icon","pipe-red.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets", "icon","base.pmg")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("all_assets","icon","background-night.png")))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 #how much the bird is tiltilng while  moving up or down
    ROT_VEL = 20        #how much we are going to move bird at each frame 
    ANIMATION_TIME = 5  #do the thing of flapping the wings 

    def __init__(self, x,y):
        self.x = x
        self.y = y 
        self.tilt = 0           #image tilting it is zero because the should be looking in the front while starting 
        self.tick_count = 0     #used for finding physics of the bird 
        self.vel = 0            #how fast the bird is moving 
        self.height = self.y     
        self.img_count = 0 
        self.img= self.IMGS[0]

  
    
    def jump(self):
        """
        we have taken the negative velocity because the edge of the flappy bird start from
        0,0 hence hence going upward requires NEGATIVE velocity and POSITIVE for the downward velocity
        and rest are same left -- -ve and right +ve
        """
        self.vel = -10.5 
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1 

        d = self.vel*self.tick_count + 1.5 * self.tick_count**2 

        # here we setting the terminal velocity dont go up and dont go down          
        if d>=16 :
            d = 16 
        
        if d < 0 :
            d -= 2 

        self.y = self.y + d 

        if d < 0 or self.y < self.height + 50 :




while True:
    bird.move()


