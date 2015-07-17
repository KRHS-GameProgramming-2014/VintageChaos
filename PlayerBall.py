import pygame
from Ball import Ball

class PlayerBall(pygame.sprite.Sprite):
    def __init__(self, pos, kind):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #Kinds:
        # 'H' : Heavy
        # 'M' : Medic
        # 'P' : Pablo
        print kind
        basePath = "players/"
        #                                                       action|Frame|Direction
        self.walkUpImages = [pygame.image.load(basePath + kind + "w" + "0" + "w" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "1" + "w" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "2" + "w" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "3" + "w" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "4" + "w" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "5" + "w" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "6" + "w" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "7" + "w" + ".PNG")]
        self.walkDownImages = [pygame.image.load(basePath + kind + "w" + "0" + "s" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "1" + "s" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "2" + "s" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "3" + "s" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "4" + "s" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "5" + "s" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "6" + "s" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "7" + "s" + ".PNG")]
        self.walkRightImages = [pygame.image.load(basePath + kind + "w" + "0" + "d" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "1" + "d" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "2" + "d" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "3" + "d" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "4" + "d" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "5" + "d" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "6" + "d" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "7" + "d" + ".PNG")]
        self.walkLeftImages = [pygame.image.load(basePath + kind + "w" + "0" + "a" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "1" + "a" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "2" + "a" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "3" + "a" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "4" + "a" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "5" + "a" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "6" + "a" + ".PNG"),
                         pygame.image.load(basePath + kind + "w" + "7" + "a" + ".PNG")]
        self.shoot = [pygame.image.load("players/Ha2a.png")]

        
        self.facing = "up"
        self.changed = False
        self.images = self.walkUpImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.06
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = 10
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.moving = False
        self.attacking = False
            
            
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
                self.speedx = 0
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
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
            
    def attack(self, atk):
        if atk == "Minigun" and self.MinigunCoolDown == 0:
            self.shooting = True
            #self.MinigunCoolDown = self.MinigunCoolDownMax
            return [Bullet(self.rect.center, self.angle)]
        
        return []
            
   
