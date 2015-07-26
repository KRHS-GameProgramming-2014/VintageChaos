import pygame, math

class TileSelect(pygame.sprite.Sprite):
    def __init__ (self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.image.load("maps/Images/TileSelect/tile1s.png"),
                       pygame.image.load("maps/Images/TileSelect/tile2s.png"),
                       pygame.image.load("maps/Images/TileSelect/tile3s.png"),
                       pygame.image.load("maps/Images/TileSelect/tile4s.png"),
                       pygame.image.load("maps/Images/TileSelect/tile5s.png")]
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
            return "Tile1"
        if self.frame == 1:
            return "Tile2"
        if self.frame == 2:
            return "Tile3"
        if self.frame == 3:
            return "Tile4"
        if self.frame == 4:
            return "Tile5"
