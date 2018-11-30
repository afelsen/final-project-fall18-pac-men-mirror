import pygame
import random
from src import Pacman
from src import Ghost
from src import Powerup
from src import Screen
from src import TopBar
from src import BottomBar

class Controller:
    def __init__(self, width = 640, height = 520):
        self.screen = pygame.display.set_mode((width,height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.pacman = Pacman.Pacman('assets/PacmanOpen.png',0,0,20)
        self.pacGroup = pygame.sprite.Group(self.pacman)
        self.pinkyGroup = pygame.sprite.Group()
        self.inkyGroup = pygame.sprite.Group()
        self.blinkyGroup = pygame.sprite.Group()
        self.clydeGroup = pygame.sprite.Group()
        self.ghostGroupList = [self.pinkyGroup,self.inkyGroup,self.blinkyGroup,self.clydeGroup]

        self.cherryGroup = pygame.sprite.Group()
        self.bananaGroup = pygame.sprite.Group()
        self.snowflakeGroup = pygame.sprite.Group()
        self.powerupGroupList = [self.cherryGroup,self.bananaGroup,self.snowflakeGroup]

        self.boxes = pygame.sprite.Group()
        self.screenmatrix = Screen.Screen(width//20,(height-40)//20)
        self.lives = TopBar.Lives('assets/PacmanMiddle.png',5,5)
        self.bottombar = BottomBar.bottomBar(3,1,0,0,0)


        for i in range(0,width,20):
            for j in range(0,height-40,20):
                self.boxes.add(Screen.Box(i,j,'assets/EmptyBox.png'))
        self.boxes.update(self.screenmatrix)

        done = False
        leveldone = False
        introdone = False
        pacmanSpeed = 2
        ghostSpeed = 2
        generalSpeed = 2
        frame = 1
        #_____Time are variables that keep track of what frame a powerup was collided with
        cherryTime = -100
        bananaTime = -100
        snowflakeTime = -100
        notOnFilled = False
        self.pacDirection = ""

        self.menuscreen = pygame.display.set_mode((width,height))
        self.menubackground = pygame.Surface(self.menuscreen.get_size()).convert()
        self.levelscreen = pygame.display.set_mode((width,height))
        self.levelbackground = pygame.Surface(self.menuscreen.get_size()).convert()
        self.gameoverscreen = pygame.display.set_mode((width,height))
        self.gameoverbackground = pygame.Surface(self.menuscreen.get_size()).convert()
        pygame.font.init()
        self.myfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 75)
        self.subfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 25)
        self.midfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 50)
        self.barfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 30)

        while self.bottombar.level < 100:
            done = False
            # Ghost spawning
            for i in range(self.bottombar.level + 1):
                self.pinkyGroup.add(Ghost.Pinky('assets/pinky.png',random.randint(2,29)*20,random.randint(2,21)*20,20))
            for i in range(self.bottombar.level + 3):
                self.blinkyGroup.add(Ghost.Blinky('assets/blinky.png',random.randint(2,29)*20,random.randint(2,21)*20,10))
            for i in range(self.bottombar.level * 2):
                self.clydeGroup.add(Ghost.Clyde('assets/clyde.png',random.randint(2,29)*20,random.randint(2,21)*20,20))
            inkysSpawned = 0

            while not done:
                introframe = 0
                textTop = self.myfont.render("PacXon",False,(255,255,50))
                textBottom = self.subfont.render("Created by the PacMen",False,(255,255,50))
                textHelp = self.subfont.render("Press SPACEBAR to start!",False,(255,255,50))
                textControls = self.subfont.render("Controls: Arrow keys to move and Q to quit",False,(255,255,50))
                while not introdone:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            introdone = True
                            done = True
                            self.bottombar.level = 100
                            leveldone = True
                        keys = pygame.key.get_pressed()

                    if introframe >= 5: #This ensures that the text is displayed for 10 frames
                        if keys[pygame.K_SPACE]: # space to start
                            introdone = True
                        elif keys[pygame.K_q]: # q to quit
                            introdone = True
                            done = True
                            self.bottombar.level = 100
                            leveldone = True
                    self.menuscreen.blit(self.menubackground,(0,0))
                    self.menuscreen.blit(textTop,(205,75))
                    self.menuscreen.blit(textBottom,(200,300))
                    self.menuscreen.blit(textHelp,(180,210))
                    self.menuscreen.blit(textControls,(0,485))
                    pygame.display.flip()
                    introframe += 1


                #Level Screen
                levelframe = 0
                levelTop = self.myfont.render("Level "+ str(self.bottombar.level),False,(255,255,50))
                levelHelp = self.subfont.render("Press SPACEBAR to continue, Q to quit",False,(255,255,50))
                while not leveldone:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                            leveldone = True
                            self.bottombar.level = 100
                        keys = pygame.key.get_pressed()

                    if levelframe >= 5: #This ensures that the text is displayed for 10 frames
                        if keys[pygame.K_SPACE]: # space to start
                            leveldone = True
                        elif keys[pygame.K_q]: # q to quit
                            leveldone = True
                            done = True
                            self.bottombar.level = 100
                    self.levelscreen.blit(self.levelbackground,(0,0))
                    self.levelscreen.blit(levelTop,(210,75))
                    self.levelscreen.blit(levelHelp,(110,210))
                    ###### fix the spacing for the text ######
                    pygame.display.flip()
                    levelframe += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        self.bottombar.level = 100


                #Inky spawning
                if self.screenmatrix.getPercent() > 5 and inkysSpawned < self.bottombar.level + 3 and frame % 50 == 0: #Spawn an inky if more than 5% of the screen is filled, every fifty frames until level+3 ghosts have been spawned
                    threebythreeList = [] #List of all possible places that inky can spawn (surrounded by 3x3 solid)
                    for i in range(1,(height-40)//20-1):
                        for j in range(1,width//20-1):
                            if self.screenmatrix.matrix[j+1][i+1] == 1 and self.screenmatrix.matrix[j+1][i] == 1 and self.screenmatrix.matrix[j+1][i-1] == 1 and self.screenmatrix.matrix[j-1][i+1] == 1 and self.screenmatrix.matrix[j-1][i] == 1 and self.screenmatrix.matrix[j-1][i-1] == 1 and self.screenmatrix.matrix[j][i+1] == 1 and self.screenmatrix.matrix[j][i-1] == 1: #Checks to see if there is a 3x3 area for inky to spawn
                                threebythreeList += [(j,i)]
                    spawnLocation = random.choice(threebythreeList)
                    self.inkyGroup.add(Ghost.Inky('assets/inky.png',spawnLocation[0]*20,spawnLocation[1]*20,20))
                    inkysSpawned += 1

                #Random powerup spawning
                if frame%300 == 0:
                    choice = random.randint(0,2)
                    if choice == 0:
                        self.cherryGroup.add(Powerup.Cherry('assets/cherry.png',random.randint(1,30)*20,random.randint(1,22)*20))
                    if choice == 1:
                        self.snowflakeGroup.add(Powerup.Snowflake('assets/snowflake.png',random.randint(1,30)*20,random.randint(1,22)*20))
                    if choice == 2:
                        self.bananaGroup.add(Powerup.Banana('assets/banana.png',random.randint(1,30)*20,random.randint(1,22)*20))

                #Powerup fucntionality
                cherryCol = pygame.sprite.spritecollide(self.pacman, self.cherryGroup, True)
                snowflakeCol = pygame.sprite.spritecollide(self.pacman, self.snowflakeGroup, True)
                bananaCol = pygame.sprite.spritecollide(self.pacman, self.bananaGroup, True)

                #Deleting powerups when ghost collide with them
                for ghostGroup in self.ghostGroupList:
                    for powerupGroup in self.powerupGroupList:
                        pygame.sprite.groupcollide(ghostGroup, powerupGroup, False, True)

                if cherryCol:
                    cherryTime = frame
                    pacmanSpeed /= 2
                if snowflakeCol:
                    snowflakeTime = frame
                    ghostSpeed *= 1000
                if bananaCol:
                    bananaTime = frame
                    ghostSpeed *= 2

                if frame == cherryTime + 50:
                    pacmanSpeed *= 2
                if frame == snowflakeTime + 50:
                    ghostSpeed /= 1000
                if frame == bananaTime + 50:
                    ghostSpeed /= 2

                pinkyCol = pygame.sprite.groupcollide(self.pinkyGroup,self.boxes,False, False)
                inkyCol = pygame.sprite.groupcollide(self.inkyGroup,self.boxes,False,False)
                blinkyCol = pygame.sprite.groupcollide(self.blinkyGroup,self.boxes,False,False)


                ## Ghost bouncing

                if (inkyCol and (frame % ghostSpeed) == 0):
                    for ghost in pygame.sprite.groupcollide(self.inkyGroup,self.boxes,False, False):
                        if (ghost.rect.x/20).is_integer() and (ghost.rect.y/20).is_integer():
                            #If a ghost hits a side
                            sidehit = False
                            if ghost.rect.y >= height-40-20 or self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] == 0:
                                ghost.ymultiplier = -1
                                sidehit = True
                            elif ghost.rect.y <= 0 or self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] == 0:
                                ghost.ymultiplier = 1
                                sidehit = True
                            if ghost.rect.x >= width - 20 or self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] == 0:
                                ghost.xmultiplier = -1
                                sidehit = True
                            elif ghost.rect.x <= 0 or self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] == 0:
                                ghost.xmultiplier = 1
                                sidehit = True

                            #If the ghost hits a corner
                            if sidehit == False:
                                for xadd in [-1,1]:
                                    for yadd in [-1,1]:
                                        if self.screenmatrix.matrix[ghost.rect.x//20+xadd][ghost.rect.y//20+yadd] == 0:
                                            ghost.xmultiplier = -xadd
                                            ghost.ymultiplier = -yadd

                    self.inkyGroup.update()
                    ########Make ghost bounce inside filled in area########

                if (blinkyCol and (frame % ghostSpeed) == 0):
                    for ghost in pygame.sprite.groupcollide(self.blinkyGroup,self.boxes,False,False):
                        if (ghost.rect.x/20).is_integer() and (ghost.rect.y/20).is_integer():
                            #If a ghost hits a side
                            sidehit = False

                            if self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] == 1:
                                ghost.ymultiplier = -1
                                sidehit = True
                                if ghost.rect.y//20 != 22:
                                    self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] = 0
                            elif  self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] == 1:
                                ghost.ymultiplier = 1
                                sidehit = True
                                if ghost.rect.y//20 != 1:
                                    self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] = 0
                            if self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier = -1
                                sidehit = True
                                if ghost.rect.x//20 != 30:
                                    self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] = 0
                            elif self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier = 1
                                sidehit = True
                                if ghost.rect.x//20 != 1:
                                    self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] = 0


                            #If the ghost hits a corner
                            if sidehit == False:
                                for xadd in [-1,1]:
                                    for yadd in [-1,1]:
                                        if self.screenmatrix.matrix[ghost.rect.x//20+xadd][ghost.rect.y//20+yadd] == 1:
                                            ghost.xmultiplier = -xadd
                                            ghost.ymultiplier = -yadd
                                            if ghost.rect.x//20 != 22 and ghost.rect.y//20 != 30 and ghost.rect.x//20 != 1 and ghost.rect.y//20 != 1:
                                                self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20+1] = 0

                    self.boxes.update(self.screenmatrix)
                    self.blinkyGroup.update()

                if (pinkyCol and (frame % ghostSpeed) == 0):
                    for ghost in pygame.sprite.groupcollide(self.pinkyGroup,self.boxes,False, False):
                        if (ghost.rect.x/20).is_integer() and (ghost.rect.y/20).is_integer():
                            #If a ghost hits a side
                            sidehit = False
                            if self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] == 1:
                                ghost.ymultiplier = -1
                                sidehit = True
                            elif  self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] == 1:
                                ghost.ymultiplier = 1
                                sidehit = True
                            if self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier = -1
                                sidehit = True
                            elif self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier = 1
                                sidehit = True


                            #If the ghost hits a corner
                            if sidehit == False:
                                for xadd in [-1,1]:
                                    for yadd in [-1,1]:
                                        if self.screenmatrix.matrix[ghost.rect.x//20+xadd][ghost.rect.y//20+yadd] == 1:
                                            ghost.xmultiplier = -xadd
                                            ghost.ymultiplier = -yadd
                    self.pinkyGroup.update()

                ########Add orange ghost bounce########


                #Pacman-box collision
                overbox = pygame.sprite.spritecollide(self.pacman, self.boxes, False)
                if(overbox):
                    for box in pygame.sprite.spritecollide(self.pacman, self.boxes, False):
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] == .5:
                                self.bottombar.lives -= 1
                                self.pacman.setPos(0,0)
                                self.screenmatrix.removeTrack()
                        if frame % pacmanSpeed == 0:
                            self.screenmatrix.trackPacman((box.rect.x//20,box.rect.y//20))
                            box.update(self.screenmatrix)
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] != 1:
                            notOnFilled = True
                            #This prevents the next lines from running over and over if the pacman is just staying in the "filled area"
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] == 1 and notOnFilled == True:
                            self.screenmatrix.fillMatrix(self.ghostGroupList)
                            self.boxes.update(self.screenmatrix)
                            notOnFilled = False
                            self.bottombar.score += 3
                            self.bottombar.percent = self.screenmatrix.getPercent()

                #If pacman's trail (or pacman himself) is collided with by a ghost, let pacman lose a life and reset to the top left.
                for ghostGroup in self.ghostGroupList:
                    for box in pygame.sprite.groupcollide(ghostGroup, self.boxes,False, False):
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] == .5 or pygame.sprite.spritecollide(self.pacman, ghostGroup,False, False):
                            deathFrame = 0
                            while deathFrame <=14*100:
                                if deathFrame%100 ==0:
                                    self.pacman.animateDeath()
                                deathFrame +=1
                            self.bottombar.lives -= 1
                            self.pacman.setPos(0,0)
                            self.screenmatrix.removeTrack()
                            break


                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    self.pacDirection = "U"
                    self.pacman.angle = 90
                    if notOnFilled == False and frame % pacmanSpeed == 0:
                        self.pacman.moveUp()
                elif keys[pygame.K_DOWN]:
                    self.pacDirection = "D"
                    self.pacman.angle = 270
                    if notOnFilled == False and frame % pacmanSpeed == 0:
                        self.pacman.moveDown()
                elif keys[pygame.K_LEFT]:
                    self.pacDirection = "L"
                    self.pacman.angle = 180
                    if notOnFilled == False and frame % pacmanSpeed == 0:
                        self.pacman.moveLeft()
                elif keys[pygame.K_RIGHT]:
                    self.pacDirection = "R"
                    self.pacman.angle = 0
                    if notOnFilled == False and frame % pacmanSpeed == 0:
                        self.pacman.moveRight()
                elif keys[pygame.K_q]:
                    done = True
                    self.bottombar.level = 100

                if frame % pacmanSpeed == 0 and notOnFilled:
                    if self.pacDirection == "U":
                        self.pacman.moveUp()
                    if self.pacDirection == "D":
                        self.pacman.moveDown()
                    if self.pacDirection == "L":
                        self.pacman.moveLeft()
                    if self.pacDirection == "R":
                        self.pacman.moveRight()

                if frame % generalSpeed == 0:
                    self.pacman.animate()
                frame += 1


                ########PRINT HIGH SCORE WHEN LOSE########
                #If pacman has 0 lives, show GAMEOVER screen
                if self.bottombar.lives == 0:
                    done = True
                    self.bottombar.level = 1
                    #Gameover Screen
                    gameoverdone = False
                    gameoverframe = 0
                    gameoverTop = self.myfont.render("GAMEOVER!",False,(255,255,50))
                    gameoverHelp = self.subfont.render("Press SPACEBAR to restart, Q to quit",False,(255,255,50))
                    while not gameoverdone:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                done = True
                                gameoverdone = True
                                self.bottombar.level = 100
                            keys = pygame.key.get_pressed()

                        if gameoverframe >= 10: #This ensures that the text is displayed for 10 frames
                            if keys[pygame.K_SPACE]: # space to start
                                gameoverdone = True
                                self.bottombar.level = 1
                                self.bottombar.score = 0
                                self.screenmatrix.reset()
                                self.pacman.setPos(0,0)
                                for ghostGroup in self.ghostGroupList:
                                    ghostGroup.empty()
                                done = True
                                self.boxes.update(self.screenmatrix)
                                self.bottombar.lives += 3
                                leveldone = False
                            elif keys[pygame.K_q]: # q to quit
                                gameoverdone = True
                                done = True
                                self.bottombar.level = 100
                        self.gameoverscreen.blit(self.gameoverbackground,(0,0))
                        self.gameoverscreen.blit(gameoverTop,(93,75))
                        self.gameoverscreen.blit(gameoverHelp,(110,210))
                        pygame.display.flip()
                        gameoverframe += 1

                ########Update High Score########


                if self.screenmatrix.getPercent() >= 80:
                    self.bottombar.level += 1
                    self.screenmatrix.reset()
                    self.pacman.setPos(0,0)
                    for ghostGroup in self.ghostGroupList:
                        ghostGroup.empty()
                    done = True
                    self.boxes.update(self.screenmatrix)
                    self.bottombar.lives += 3
                    leveldone = False


                bottombar = self.barfont.render(self.bottombar.data(),False,(255,255,50))
                self.screen.blit(self.background,(0,0))
                self.screen.blit(bottombar,(0,height-45))


                self.boxes.draw(self.screen)
                self.pacGroup.draw(self.screen)
                for powerupGroup in self.powerupGroupList:
                    powerupGroup.draw(self.screen)
                for ghostGroup in self.ghostGroupList:
                    ghostGroup.draw(self.screen)
                pygame.display.flip()
