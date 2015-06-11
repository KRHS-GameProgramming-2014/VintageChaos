import pygame
from Ball import Ball
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, kind):
        pygame.sprite.Sprite.__init__(self, self.containers)

        print kind
        basePath = "enemys/"
        #                                                       action|Frame|Direction
        self.walkUpImages = [pygame.image.load(basePath + kind + "a" + ".png"),
                         pygame.image.load(basePath + kind + "m" + "a" + ".png")]

        self.walkDownImages = [pygame.image.load(basePath + kind + "s" + ".png"),
                         pygame.image.load(basePath + kind + "m" + "s"  + ".png")]
   
        self.walkRightImages = [pygame.image.load(basePath + kind + "d" + ".png"),
                         pygame.image.load(basePath + kind + "m" + "d" + ".png")]

        self.walkLeftImages = [pygame.image.load(basePath + kind + "a" + ".png"),
                         pygame.image.load(basePath + kind + "m" + "a" + ".png")]


        self.frame = 0
        self.images = self.walkUpImages
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.06
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = 10
        self.speedx = 20
        self.speedy = 10
        self.speed = [self.speedx, self.speedy]
        self.moving = False
        self.collideWall		
            
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.collideWall(width, height)
        self.animate()
        self.changed = False
    
    def collideBall(self, other):
        if self != other:
            if (self.radius + other.radius) > self.distance(other.rect.center):
                if not self.didBounceX:
                    self.speedx = -self.speedx
                    self.didBouncex = True
                if not self.didBounceY:
                    self.speedy = -self.speedy
                    self.didBounceY = True
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideBlock(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.speedy = 0
    
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                #print "hit xWall"
    
    def animate(self):
        if self.moving:
            if self.waitCount < self.maxWait:
                self.waitCount += 1
            else:
                self.waitCount = 0
                self.changed = True
                if self.frame < self.maxFrame:
                    self.frame += 1
                else:
                    self.frame = 0
            
            if self.changed:    
                if self.facing == "up":
                    self.images = self.walkUpImages
                elif self.facing == "down":
                    self.images = self.walkDownImages
                elif self.facing == "right":
                    self.images = self.walkRightImages
                elif self.facing == "left":
                    self.images = self.walkLeftImages
                
                self.image = self.images[self.frame]
        else:
            self.frame = 0
            self.image = self.images[self.frame]
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.moving = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
            self.moving = False
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.moving = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            self.moving = False
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.moving = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
            self.moving = False
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.moving = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0
            self.moving = False
            

   
