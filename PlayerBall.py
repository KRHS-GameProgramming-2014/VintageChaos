import pygame
from Ball import Ball

class PlayerBall(Ball):
    def __init__(self, playerNum, pos):
        Ball.__init__(self, "images/Player/mcp1.png", [0,0], pos)
        if playerNum == 1:
            self.upImages = [pygame.image.load("images/Player/mcp1.png"),
                             pygame.image.load("images/Player/mcw1w.png"),
                             pygame.image.load("images/Player/mcw2w.png"),
                             pygame.image.load("images/Player/mcw1w.png"),
                             pygame.image.load("images/Player/mcp1.png"),
                             pygame.image.load("images/Player/mcw1w4.png"),
                             pygame.image.load("images/Player/mcw2w8.png"),
                             pygame.image.load("images/Player/mcw1w4.png")]
           
            self.downImages = [pygame.image.load("images/Player/mcp1down.png"),
                               pygame.image.load("images/Player/mcw1s.png"),
                               pygame.image.load("images/Player/mcw2s.png"),
                               pygame.image.load("images/Player/mcw1s.png"),
                               pygame.image.load("images/Player/mcp1down.png"),
                               pygame.image.load("images/Player/mcw1s3.png"),
                               pygame.image.load("images/Player/mcw2s7.png"),
                               pygame.image.load("images/Player/mcw1s3.png")]
                               
                             
            self.leftImages = [pygame.image.load("images/Player/mcp1left.png"),
                                pygame.image.load("images/Player/mcw1a.png"),
                                pygame.image.load("images/Player/mcw2a.png"),
                                pygame.image.load("images/Player/mcw1a.png"),
                                pygame.image.load("images/Player/mcp1left.png"),
                                pygame.image.load("images/Player/mcw1a1.png"),
                                pygame.image.load("images/Player/mcw2a5.png"),
                                pygame.image.load("images/Player/mcw1a1.png")]
                               
            self.rightImages = [pygame.image.load("images/Player/mcp1right.png"),
                                pygame.image.load("images/Player/mcw1d.png"),
                                pygame.image.load("images/Player/mcw2d.png"),
                                pygame.image.load("images/Player/mcw1d.png"),
                                pygame.image.load("images/Player/mcp1right.png"),
                                pygame.image.load("images/Player/mcw1d2.png"),
                                pygame.image.load("images/Player/mcw2d6.png"),
                                pygame.image.load("images/Player/mcw1d2.png")]
                                
            self.upPunchImages = [pygame.image.load("images/Player/punchUP.png")]
            self.rightPunchImages = [pygame.image.load("images/Player/punchRight.png")]
            self.leftPunchImages = [pygame.image.load("images/Player/punchLeft.png")]
            self.downPunchImages = [pygame.image.load("images/Player/punchDown.png")]
        else:
            self.upImages = [pygame.image.load("images/Player2/blkw.PNG"),
                             pygame.image.load("images/Player2/blkw1w.PNG"),
                             pygame.image.load("images/Player2/blkw2w.PNG"),
                             pygame.image.load("images/Player2/blkw1w.PNG"),
                             pygame.image.load("images/Player2/blkw.PNG"),
                             pygame.image.load("images/Player2/blkw1rw.PNG"),
                             pygame.image.load("images/Player2/blkw2rw.PNG"),
                             pygame.image.load("images/Player2/blkw1rw.PNG")]
                          
            self.downImages = [pygame.image.load("images/Player2/blks.PNG"),
                               pygame.image.load("images/Player2/blkw1s.PNG"),
                               pygame.image.load("images/Player2/blkw2s.PNG"),
                               pygame.image.load("images/Player2/blkw1s.PNG"),
                               pygame.image.load("images/Player2/blks.PNG"),
                               pygame.image.load("images/Player2/blkw1rs.PNG"),
                               pygame.image.load("images/Player2/blkw2rs.PNG"),
                               pygame.image.load("images/Player2/blkw1rs.PNG")]
                               
                             
            self.leftImages = [pygame.image.load("images/Player2/blka.PNG"),
                               pygame.image.load("images/Player2/blkw1a.PNG"),
                               pygame.image.load("images/Player2/blkw2a.PNG"),
                               pygame.image.load("images/Player2/blkw1a.PNG"),
                               pygame.image.load("images/Player2/blka.PNG"),
                               pygame.image.load("images/Player2/blkw1ra.PNG"),
                               pygame.image.load("images/Player2/blkw2ra.PNG"),
                               pygame.image.load("images/Player2/blkw1ra.PNG")]
                               
            self.rightImages = [pygame.image.load("images/Player2/blkd.PNG"),
                                pygame.image.load("images/Player2/blkw1d.PNG"),
                                pygame.image.load("images/Player2/blkw2d.PNG"),
                                pygame.image.load("images/Screens/steven hawking.PNG"),
                                pygame.image.load("images/Player2/blkd.PNG"),
                                pygame.image.load("images/Player2/blkw1rd.PNG"),
                                pygame.image.load("images/Player2/blkw2rd.PNG"),
                                pygame.image.load("images/Player2/blkw1rd.PNG")]
                                
            self.upPunchImages = [pygame.image.load("images/Player2/blkpw.PNG")]
            self.rightPunchImages = [pygame.image.load("images/Player2/blkpd.PNG")]
            self.leftPunchImages = [pygame.image.load("images/Player2/blkpa.PNG")]
            self.downPunchImages = [pygame.image.load("images/Player2/blkps.PNG")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 5
        self.punching = False
        self.punchTime = 0
        self.maxPunchTime = .15*60
            
    def update(self, width, height):
        Ball.update(self, width, height)
        
        if self.punchTime > 0:
            if self.punchTime < self.maxPunchTime:
                self.punchTime += 1
                self.changed = True
            else:
                self.punchTime = 0
                self.punching = False
                self.changed = True
        
        self.animate()
        self.changed = False
        
    def collideEdge(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 1
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
                #print "hit xWall"
    
    def collideWall(self, wall):
        if self.rect.right > wall.rect.left and self.rect.left < wall.rect.right:
            if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.bottom:
                if not self.didBounceX and self.speedx != 0:
                    self.speedx = -self.speedx*2
                    self.move()
                    self.speedx = 1
                    #print "x"
                    self.didBouncex = True
                if not self.didBounceY and self.speedy != 0:
                    self.speedy = -self.speedy*2
                    self.move()
                    self.speedy = 0
                    #print "y"
                    self.didBounceY = True
                    #print "hit Ball"
    
    def collideLevelChangeWall(self, wall):
        if self.rect.right > wall.rect.left and self.rect.left < wall.rect.right:
            if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.bottom:
                return True
        return False
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 2
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.punching:
                self.maxFrame = len(self.upPunchImages)-1
                if self.facing == "up":
                    self.images = self.upPunchImages
                elif self.facing == "down":
                    self.images = self.downPunchImages
                elif self.facing == "right":
                    self.images = self.rightPunchImages
                elif self.facing == "left":
                    self.images = self.leftPunchImages

            else:
                self.maxFrame = len(self.upImages)-1
                if self.facing == "up":
                    self.images = self.upImages
                elif self.facing == "down":
                    self.images = self.downImages
                elif self.facing == "right":
                    self.images = self.rightImages
                elif self.facing == "left":
                    self.images = self.leftImages   
                
            if self.frame > self.maxFrame:
                self.frame = 0
            #print self.frame, self.maxFrame, len(self.images)
            self.image = self.images[self.frame]
            self.rect = self.image.get_rect(center = self.rect.center)

    def punch(self):
       self.punching = True
       self.punchTime = 1
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0
            
    def shoot(self, command):
        if command == "stop":
            self.shooting = False
        elif command == "fire":
            return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing, self)]
            self.shooting = True
            return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing, self)]
        else:
            return []

    def collideBullet(self, other, owner):
        self.owner = owner
        if other != self.owner:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.living = False
                    #print "dead"  
    


