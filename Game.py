import pygame, sys, random
from Ball import Ball
from PlayerBall import PlayerBall
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block
from PlayerSelect import PlayerSelect
from TileSelect import TileSelect
from MapSelect import ScreenSelect
from Enemy import Enemy



pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 10

pygame.display.set_caption("Chaos of the Vintage Variety")

screen = pygame.display.set_mode(size)

pygame.mixer.music.load("music/flipfloop.mp3")
pygame.mixer.music.play(0, 0.0)

balls = pygame.sprite.Group()
players = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
menuItems = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()
projectiles = pygame.sprite.Group()

Ball.containers = (all, balls)
PlayerBall.containers = (all, players)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Button.containers = (all, menuItems)
PlayerSelect.containers = (all, menuItems)
TileSelect.containers = (all, menuItems)
ScreenSelect.containers = (all, menuItems)
Score.containers = (all, hudItems)
Enemy.containers = (all, enemies)
#Bullet.containers = (all, projectiles)

run = False

BackGround("Images/mmscreens/vbg.png", size)

pygame.mouse.set_cursor(*pygame.cursors.diamond)

startButton = Button([width/2, height-580],
                     "Images/Buttons/StartButton.png")
ps1 = PlayerSelect([width/7, height-580])
ps2 = PlayerSelect([width-(width/7), height-580])

kind1 = ""
kind2 = ""
tileType = ""
cleanscreenType = ""

startButton = Button([width/2, height-580],
                     "Images/Buttons/StartButton.png",
                     "Images/Buttons/StartButtonC.png")
                     
quitButton = Button([width/1.32, height-75.5],
                    "Images/Buttons/QButton.png",
                    "Images/Buttons/QButtonC.png")
                    
playeroneleftButton = Button([width/25, height-600.5],
                    "ArrowButtons/ArrowL.png")

playeronerightButton = Button([width/4, height-600.5],
                    "ArrowButtons/ArrowR.png")

playertwoleftButton = Button([width/1.35, height-600.5],
                    "ArrowButtons/ArrowL.png")
                    
playertworightButton = Button([width/1.05, height-600.5],
                    "ArrowButtons/ArrowR.png")
                    
tileselectleftButton = Button([width/20, height-300],
                    "ArrowButtons/ArrowLC.png")
                    
tileselectrightButton = Button([width/2.3, height-300],
                    "ArrowButtons/ArrowRC.png")
                    
mapselectleftButton = Button([width/1.85, height-300],

                    "ArrowButtons/ArrowLC.png")
                    
mapselectrightButton = Button([width/1.05, height-300],
                    "ArrowButtons/ArrowRC.png")
                
#optionsButton = Button([width/4, height-77],
#                  "Images/Buttons/OptionsButton.png",
#                   "Images/Buttons/OptionsButtonC.png")
                    
tile = TileSelect([width/4, height-300])
cleanscreen = ScreenSelect([width/1.35, height-300])


kind = ""




while True:
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
                if event.key == pygame.K_a:
                    ps1.prev()
                if event.key == pygame.K_d:
                    ps1.next()
                if event.key == pygame.K_LEFT:
                    ps2.prev()
                if event.key == pygame.K_RIGHT:
                    ps2.next()
                if event.key == pygame.K_SPACE:
                    tile.next()
                if event.key == pygame.K_p:
                    tile.prev()
                if event.key == pygame.K_m:
                    cleanscreen.next()
                if event.key == pygame.K_o:
                    cleanscreen.prev()
                if event.key == pygame.K_r:
                    player1.go("attack")
                    if event.key == pygame.K_t:
                        player2.go("attack")
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
                quitButton.click(event.pos)
                playeroneleftButton.click(event.pos)
                playeronerightButton.click(event.pos)
                playertwoleftButton.click(event.pos)
                playertworightButton.click(event.pos)
                tileselectleftButton.click(event.pos)
                tileselectrightButton.click(event.pos)
                mapselectrightButton.click(event.pos)
                mapselectleftButton.click(event.pos)
                #optionsButton.click(event.pos) #all MOUSEBUTTONDOWN should be in the same block
            
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = True
                    pygame.mouse.set_visible(False)
                if quitButton.release(event.pos):
                    pygame.quit()
                    sys.exit()
                if playeroneleftButton.release(event.pos):         
                    ps1.prev()
                if playeronerightButton.release(event.pos):
                    ps1.next()
                if playertwoleftButton.release(event.pos):         
                    ps2.prev() 
                if playertworightButton.release(event.pos):         
                    ps2.next()    
                if tileselectleftButton.release(event.pos):         
                    tile.prev()   
                if tileselectrightButton.release(event.pos):         
                    tile.next() 
                if mapselectleftButton.release(event.pos):         
                    cleanscreen.prev()
                if mapselectrightButton.release(event.pos):  
                    cleanscreen.next()
                #if optionsButton.release(event.pos):
                #    pygame.image.load("Images/Screens/temporaryOptionsScreen.png") 
                    
        all.update(width, height)

        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
    kind1 = ps1.select()
    kind2 = ps2.select()
    tileType = tile.select()
    cleanscreenType = cleanscreen.select()
    all.empty()
    
    BackGround("Images/Screens/"+cleanscreenType, size)
    level = Level(size, 50)
    level.loadLevel("1", tileType)

    player1 = PlayerBall([width/2, height/2], kind1)
    print players.sprites()
    print player1.groups()
    player2 = PlayerBall([width/3, height/2], kind2)
    print players.sprites()
    print player2.groups()
    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6


    score1 = Score([width-220,height-25], "Overall Score:", 36)

   
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
                if event.key == pygame.K_UP:
                    player2.go("up")
                if event.key == pygame.K_RIGHT:
                    player2.go("right")
                if event.key == pygame.K_DOWN:
                    player2.go("down")
                if event.key == pygame.K_LEFT:
                    player2.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1.go("stop up")
                if event.key == pygame.K_d:
                    player1.go("stop right")
                if event.key == pygame.K_s:
                    player1.go("stop down")
                if event.key == pygame.K_a:
                    player1.go("stop left")
                if event.key == pygame.K_UP:
                    player2.go("stop up")
                if event.key == pygame.K_RIGHT:
                    player2.go("stop right")
                if event.key == pygame.K_DOWN:
                    player2.go("stop down")
                if event.key == pygame.K_LEFT:
                    player2.go("stop left")
                
                    
                    
        #---------Enemies off until images fixed-----

        if len(balls) < 10:
            if random.randint(0, 1*60) == 0:
                Ball("Images/enemies/ba1w.png",
                          [random.randint(0,10), random.randint(0,10)],
                          [random.randint(100, width-100), random.randint(100, height-100)])

        if random.randint(0, 25*60) == 0:
            print ">>>>>>>>>>>>>>>>>>>"
            Enemy([random.randint(100, width-100), random.randint(100, height-100)], 
                  [random.randint(-3,3),random.randint(-3,3)]) 
                  #'B') #...passing 'B' in to speed makes enemies not move!

        
        if timerWait < timerWaitMax:
            timerWait += 1
        else:
            timerWait = 0
            timer.increaseScore(.1)

        playersHitBalls = pygame.sprite.groupcollide(players, balls, False, True)
        ballsHitBalls = pygame.sprite.groupcollide(balls, balls, False, False)
        playersHitBlocks = pygame.sprite.groupcollide(players, blocks, False, False)
        projectilesHitEnemies = pygame.sprite.groupcollide(projectiles, enemies, True, True)
        

        for player in playersHitBalls:
            for ball in playersHitBalls[player]:
                score1.increaseScore(1)
        
        for player in playersHitBalls:
            for ball in playersHitBalls[player]:
                player1.collideWall
                
        for Enemy in ballsHitBalls:
            for Enemy in ballsHitBalls[Enemy]:
                player1.collideBlock
        
        #GOD DAMNED TAB ERROR....the bane of the python programmer
        for bully in ballsHitBalls:
            for victem in ballsHitBalls[bully]:
                bully.collideBall(victem)
        
        for bully in playersHitBlocks:
            for victem in playersHitBlocks[bully]:
                bully.collideBlock(victem)
        
        for bully in projectilesHitEnemies:
            for victem in projectilesHitEnemies[bully]:
                bully.collideBall(victem)
        
        #ONE MORE TAB ERROR
        all.update(width, height)

        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        
        
        

        


        clock.tick(60)

