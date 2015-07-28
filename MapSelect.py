import pygame, math

class ScreenSelect(pygame.sprite.Sprite):
    def __init__ (self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.image.load("Images/CleanScreen/3drbg.png"),
                       pygame.image.load("Images/CleanScreen/3dbg.png"),
                       pygame.image.load("Images/CleanScreen/3dgbg.png")] #desert basement images not present
                       #pygame.image.load("Images/CleanScreen/desert.png"),
                       #pygame.image.load("Images/CleanScreen/basement.png")]
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.place(pos)
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(*args):
        pass
        
    def next(self):
        if self.frame < 4:
            self.frame += 1
        else:
            self.frame = 0
        self.image = self.images[self.frame]
        
    def prev(self):
        if self.frame > 0:
            self.frame -= 1
        else:
            self.frame = 4
        self.image = self.images[self.frame]
        
   
    
    def select(self):
        if self.frame == 0:
            return "3drbg.png"
        if self.frame == 1:
            return "3dbg.png"
        if self.frame == 2:
            return "3dgbg.png"
        if self.frame == 3:
            return "desert.png"
        if self.frame == 4:
            return "basement.png"
