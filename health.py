#code from Kevin, Jacob, Phillip
#https://code.google.com/p/butterfly-game1/

import pygame,math,sys,random

class HealthBar():
    def __init__(self, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("images/Health/0health.png")]
        self.surfaces += [pygame.image.load("images/Health/10health.png")]
        self.surfaces += [pygame.image.load("images/Health/25health.png")]
        self.surfaces += [pygame.image.load("images/Health/40health.png")]
        self.surfaces += [pygame.image.load("images/Health/55health.png")]
        self.surfaces += [pygame.image.load("images/Health/70health.png")]
        self.surfaces += [pygame.image.load("images/Health/85health.png")]
        self.surfaces += [pygame.image.load("images/Health/100health.png")]
        self.maxFrame = len(self.surfaces)-1
#        self.surface = pygame.transform.scale(self.faces,(100,25))
        self.frame = self.maxFrame
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.rect.center = position
        #if pygame.mixer:
        #    self.healthSound = pygame.mixer.Sound("health.wav")
        
       
    def  __str__(self):
        return "I'm a Health Bar " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def health_bar(self):
        pass
            
    def update(self, life, maxLife):
        percentLife = float(life)/float(maxLife)
        if percentLife > .85:
            self.frame = 7
            print percentLife
        elif percentLife > .70:
            self.frame = 6
            print percentLife
        elif percentLife > .55:
            self.frame = 5
            print percentLife
        elif percentLife > .40:
            self.frame = 4
            print percentLife
        elif percentLife > .25:
            self.frame = 3
            print percentLife
        elif percentLife > .10:
            self.frame = 2
            print percentLife
        elif percentLife > .0:
            self.frame = 1
            print percentLife
        elif percentLife < .0:
            self.frame = 0
            print percentLife
            self.living = False
        self.surface = self.surfaces[self.frame]
