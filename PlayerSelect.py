import pygame, math

class PlayerSelect(pygame.sprite.Sprite):
    def __init__ (self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.image.load("PlayerSlect/CS1.png"),
                       pygame.image.load("PlayerSlect/CS2.png"),
                       pygame.image.load("PlayerSlect/CS3.png")]
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
            self.frame = 1
        self.image = images[frame]
        
    def prev(self):
        if self.frame > 1:
            self.frame -= 1
        else:
            self.frame = 2
        self.image = images[frame]
    
    def select(self):
        if self.frame == 1:
            return "H"
        if self.frame == 2:
            return "P"
        if self.frame == 3:
            return "M"
