import pygame, sys, random
from Ball import Ball
from PlayerBall import PlayerBall
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block
from HUD import Score
from PlayerSelect import PlayerSelect

pygame.init()

clock = pygame.time.Clock()

width = 1150
height = 700
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Images/mmscreens/bg.png").convert()
bgRect = bgImage.get_rect()

balls = pygame.sprite.Group()
players = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
buttons = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Ball.containers = (all, balls)
PlayerBall.containers = (all, players)
PlayerSelect.containers = (all, buttons)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Score.containers = (all, hudItems)



run = False

startButton = Button([width/2, height-300], 
                     "Images/Button/sgbutton.png", 
                     "Images/Button/sgbuttonc.png")



p1Select = PlayerSelect([200,200])
p2Select = PlayerSelect([200,400])

#healthbar = HealthBar([width - 75, 125])  #DEFAULT: 100 MODED: 200

bullets = []

balls = []
balls += [Ball("images/Ball/crabman.png", [0,0], [150, 200])]

pygame.mixer.music.load("Music/crny.mp3")
pygame.mixer.music.play(-1, 0.0)



timer = Score([80, height - 25], "Time:",36)
timerWait = 0
timerWaitMax =20

title = Text([height/4, width/8], "Hello HUD!!", 20)

score1 = Score([width-220,height-25], "HUBBA:", 36)
score2 = Score([width-80,height-25], "BUBBA:", 36)


run = False

startButton = Button([width/2, height-300], 
                                     "images/button/sgbutton.png", 
                                     "images/button/sgbutton.png")

while True:
        while not run:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        run = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                startButton.click(event.pos)
                        if event.type == pygame.MOUSEBUTTONUP:
                                if startButton.release(event.pos):
                                        run = True

                bgColor = r,g,b
                screen.fill(bgColor)
                screen.blit(bgImage, bgRect)
                screen.blit(startButton.image, startButton.rect)
                pygame.display.flip()
                clock.tick(60)
        
BackGround("images/mmscreens/Main Screen.png")
    
player = PlayerBall([width/2, height/2], "M")
    
    
    level = Level(size, 50)
    level.loadLevel("1")

    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6

    score = Score([width-80, height-25], "Score: ", 36)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player1.go("up")
                    if event.key == pygame.K_d:
                        player1.go("right")
                    if event.key == pygame.K_s:
                        player1.go("down")
                    if event.key == pygame.K_a:
                        player1.go("left")
                    if event.key == pygame.K_q:
                        player1.punch()

                    if event.key == pygame.K_UP:
                        player2.go("up")
                    if event.key == pygame.K_RIGHT:
                        player2.go("right")
                    if event.key == pygame.K_DOWN:
                        player2.go("down")
                    if event.key == pygame.K_LEFT:
                        player2.go("left")
                    if event.key == pygame.K_m:
                        player2.punch()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        player1.go("stop up")
                    if event.key == pygame.K_d:
                        player1.go("stop right")
                    if event.key == pygame.K_s:
                        player1.go("stop down")
                    if event.key == pygame.K_a:
                        player1.go("stop left")
                    if event.key == pygame.K_q:
                        player1.go("stop punch")

                    if event.key == pygame.K_UP:
                        player2.go("stop up")
                    if event.key == pygame.K_RIGHT:
                        player2.go("stop right")
                    if event.key == pygame.K_DOWN:
                        player2.go("stop down")
                    if event.key == pygame.K_LEFT:
                        player2.go("stop left")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if  event.button == 1:
                        print "OW!!!!!"
                        player2.punch()
                    
                
            if len(balls) < 2:
                if random.randint(0, .25*60) == 0:
                    balls += [Ball("images/Ball/spinnything.png",
                              [random.randint(0,10), random.randint(0,10)],
                              [random.randint(100, width-100), random.randint(100, height-100)])
                              ]
            if len(balls) < 2:
                if random.randint(0, .25*60) == 0:
                    balls += [Ball("images/Ball/crabman.png",
                              [random.randint(0,10), random.randint(0,10)],
                              [random.randint(100, width-100), random.randint(100, height-100)]
                            )]
                              
            
      
      
            player1.update(width, height)
            player2.update(width, height)
            timer.update()
            score1.update()
            score2.update()

            
            HealthBar.update

            
         #   for vision in visions:
           #     vision.update()
            
            for ball in balls:
                ball.update(width, height)
                
            for bullet in bullets:
                bullet.update(width, height)
               
            for bullet in bullets:
                bullet.collidePlayer(player1)
                bullet.collidePlayer(player2)
                player2.collideBullet(bullet)
                player1.collideBullet(bullet)

            for bullet in bullets:
                if not bullet.living:
                    bullets.remove(bullet)
                
            for wall in walls:
                player1.collideWall(wall)
                player2.collideWall(wall)
            for wall in lcWalls:
                if player1.collideLevelChangeWall(wall) or player2.collideLevelChangeWall(wall):
                    bgI = pygame.image.load("images/Screens/" + wall.target + ".png")
                    bgR = bgI.get_rect()
                    walls = []

            for bully in balls:
                for victem in balls:
                    bully.collideBall(victem)


                    
            for bullet in bullets:
                bullet.update(screenWidth, screenHeight)


                if bully.collidePlayer(player1):
                    score1.increaseScore()
                if bully.collidePlayer(player2):
                    score2.increaseScore()



                    bully.collidePlayer(player1)
                    bully.collidePlayer(player2)
                    
            #if player1.health <= 0:
             #   player1.living = False
                    
                    

            for ball in balls:
                if not ball.living:
                    balls.remove(ball)
            if timerWait < timerWaitMax:
                timerWait += 10

            else:
                timerWait = 0
                timer.increaseScore(.1)
        
        playersHitBalls = pygame.sprite.groupcollide(players, balls, False, True)
        ballsHitBalls = pygame.sprite.groupcollide(balls, balls, False, False)
        
        for player in playersHitBalls:
            for ball in playersHitBalls[player]:
                score.increaseScore(1)
                
        for bully in ballsHitBalls:
            for victem in ballsHitBalls[bully]:
                bully.collideBall(victem)
        
        all.update(width, height)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
        
        
        
        
        
        
        
