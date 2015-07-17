import pygame, math

class PlayerSelect(pygame.sprite.Sprite):
    def __init__ (self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.image.load("PlayerSelect/CS1.png"),
                       pygame.image.load("PlayerSelect/CS2.png"),
                       pygame.image.load("PlayerSelect/CS3.png")]
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.place(pos)
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(*args):
        pass
        
    def next(self):
        if self.frame < 2:
            self.frame += 1
        else:
            self.frame = 0
        self.image = self.images[self.frame]
        
    def prev(self):
        if self.frame > 0:
            self.frame -= 1
        else:
            self.frame = 2
        self.image = self.images[self.frame]
    
    def select(self):
        if self.frame == 0:
            return "H"
        if self.frame == 1:
            return "P"
        if self.frame == 2:
            return "M"
