import pygame
import random
from src import Pacman
from src import Ghost
from src import Powerup
from src import Screen
from src import BottomBar

class Controller:
    def __init__(self, width = 640, height = 560):
        '''
        Initializes the Controller class and creates the game loop
        '''
        self.screen = pygame.display.set_mode((width,height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.pacman = Pacman.Pacman('assets/pacmanimages/PacmanOpen.png',0,0,20)
        self.pacGroup = pygame.sprite.Group(self.pacman)
        self.pinkyGroup = pygame.sprite.Group()
        self.inkyGroup = pygame.sprite.Group()
        self.blinkyGroup = pygame.sprite.Group()
        self.clydeGroup = pygame.sprite.Group()
        self.ghostGroupList = [self.pinkyGroup,self.inkyGroup,self.blinkyGroup,self.clydeGroup]

        self.cherryGroup = pygame.sprite.Group()
        self.bananaGroup = pygame.sprite.Group()
        self.snowflakeGroup = pygame.sprite.Group()
        self.heartGroup = pygame.sprite.Group()
        self.powerupGroupList = [self.cherryGroup,self.bananaGroup,self.snowflakeGroup, self.heartGroup]
        self.boxes = pygame.sprite.Group()
        self.screenmatrix = Screen.Screen(width//20,(height-80)//20)
        self.bottombar = BottomBar.Bottombar(3,1,0,0,0)
        fptr = open("assets/highscore.txt", "r")
        self.bottombar.highScore = int(fptr.read())
        fptr.close()


        for i in range(0,width,20):
            for j in range(0,height-80,20):
                self.boxes.add(Screen.Box(i,j,'assets/screenimages/EmptyBox.png'))
        self.boxes.update(self.screenmatrix)

        done = False
        leveldone = False
        introdone = False
        instructionsdone = False
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
            for i in range(self.bottombar.level//2+1):
                self.pinkyGroup.add(Ghost.Pinky('assets/ghostimages/pinky.png',random.randint(2,29)*20,random.randint(2,21)*20,20))
            for i in range(self.bottombar.level//3):
                self.blinkyGroup.add(Ghost.Blinky('assets/ghostimages/blinky.png',random.randint(2,29)*20,random.randint(2,21)*20,10))
            for i in range(self.bottombar.level//3):
                self.clydeGroup.add(Ghost.Clyde('assets/ghostimages/clyde.png',random.randint(2,29)*20,random.randint(2,21)*20,20))
            inkysSpawned = 0

            while not done:
                introframe = 0
                textTop = self.myfont.render("PacXon",False,(255,255,50))
                textBottom = self.subfont.render("Created by the PacMen",False,(255,255,50))
                textHelp = self.subfont.render("Press SPACEBAR to start!",False,(255,255,50))
                textControls = self.subfont.render("Press 'I' for instructions",False,(255,255,50))
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
                        elif keys[pygame.K_i]: # i for instructions
                            instructionsdone = False
                            instructionsframe = 0
                            instructionsTop = self.myfont.render("Instructions:",False,(255,255,50))
                            instructionsCont = self.subfont.render("Use the arrows keys to move",False,(255,255,50))
                            instructionsP1 = self.subfont.render("Increases Pacman's speed",False,(255,160,16))
                            instructionsP2 = self.subfont.render("Decreases Ghost speed",False,(0,192,0))
                            instructionsP3 = self.subfont.render("Freezes all Ghosts",False,(0,50,255))
                            instructionsP4 = self.subfont.render("Gives Pacman an extra life",False,(255,0,0))
                            instructionsQ = self.subfont.render("Press SPACEBAR to return to menu, and Q to quit",False,(255,255,50))
                            instructionsLev = self.subfont.render("To complete each level, you must fill in 80% of the screen",False,(255,255,50))
                            instructionsHeart = pygame.transform.scale(pygame.image.load("assets/powerupimages/heart.png"),(40, 40))
                            instructionsCherry = pygame.transform.scale(pygame.image.load("assets/powerupimages/cherry.png"),(40, 40))
                            instructionsBanana = pygame.transform.scale(pygame.image.load("assets/powerupimages/banana.png"),(40, 40))
                            instructionsSnowflake = pygame.transform.scale(pygame.image.load("assets/powerupimages/snowflake.png"),(40, 40))
                            while not instructionsdone:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        introdone = True
                                        done = True
                                        self.bottombar.level = 100
                                        leveldone = True
                                        instructionsdone = True
                                    keys = pygame.key.get_pressed()

                                if instructionsframe >= 5: #This ensures that the text is displayed for 10 frames
                                    if keys[pygame.K_SPACE]: # space to go back
                                        instructionsdone = True
                                        introframe = 0
                                    elif keys[pygame.K_q]: # q to quit
                                        introdone = True
                                        done = True
                                        self.bottombar.level = 100
                                        leveldone = True
                                        instructionsdone = True
                                self.menuscreen.blit(self.menubackground,(0,0))
                                self.menuscreen.blit(instructionsTop,(120,0))
                                self.menuscreen.blit(instructionsCont,(175,100))
                                self.menuscreen.blit(instructionsP1,(200,220))
                                self.menuscreen.blit(instructionsP2,(200,290))
                                self.menuscreen.blit(instructionsP3,(200,360))
                                self.menuscreen.blit(instructionsP4,(200,430))
                                self.menuscreen.blit(instructionsQ,(65,500))
                                self.menuscreen.blit(instructionsLev,(40,150))
                                self.menuscreen.blit(instructionsCherry,(150,220))
                                self.menuscreen.blit(instructionsBanana,(150,290))
                                self.menuscreen.blit(instructionsSnowflake,(150,360))
                                self.menuscreen.blit(instructionsHeart,(150,430))
                                pygame.display.flip()
                                instructionsframe += 1
                    self.menuscreen.blit(self.menubackground,(0,0))
                    self.menuscreen.blit(textTop,(205,75))
                    self.menuscreen.blit(textBottom,(200,300))
                    self.menuscreen.blit(textHelp,(180,210))
                    self.menuscreen.blit(textControls,(0,525))
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
                    pygame.display.flip()
                    levelframe += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        self.bottombar.level = 100


                #Inky spawning
                if self.screenmatrix.getPercent() > 5 and inkysSpawned < (self.bottombar.level+1)//3+1 and frame % 50 == 0: #Spawn an inky if more than 5% of the screen is filled, every fifty frames until level+3 ghosts have been spawned
                    threebythreeList = [] #List of all possible places that inky can spawn (surrounded by 3x3 solid)
                    for i in range(1,(height-80)//20-1):
                        for j in range(1,width//20-1):
                            if self.screenmatrix.matrix[j+1][i+1] == 1 and self.screenmatrix.matrix[j+1][i] == 1 and self.screenmatrix.matrix[j+1][i-1] == 1 and self.screenmatrix.matrix[j-1][i+1] == 1 and self.screenmatrix.matrix[j-1][i] == 1 and self.screenmatrix.matrix[j-1][i-1] == 1 and self.screenmatrix.matrix[j][i+1] == 1 and self.screenmatrix.matrix[j][i-1] == 1: #Checks to see if there is a 3x3 area for inky to spawn
                                threebythreeList += [(j,i)]
                    if threebythreeList != []:
                        spawnLocation = random.choice(threebythreeList)
                        self.inkyGroup.add(Ghost.Inky('assets/ghostimages/inky.png',spawnLocation[0]*20,spawnLocation[1]*20,20))
                        inkysSpawned += 1

                #Random powerup spawning
                if frame%200 == 0:
                    choice = random.randint(0,3)
                    if choice == 0:
                        self.cherryGroup.add(Powerup.Cherry('assets/powerupimages/cherry.png',random.randint(1,30)*20,random.randint(1,22)*20))
                    if choice == 1:
                        self.snowflakeGroup.add(Powerup.Snowflake('assets/powerupimages/snowflake.png',random.randint(1,30)*20,random.randint(1,22)*20))
                    if choice == 2:
                        self.bananaGroup.add(Powerup.Banana('assets/powerupimages/banana.png',random.randint(1,30)*20,random.randint(1,22)*20))
                    if choice == 3:
                        self.heartGroup.add(Powerup.Heart('assets/powerupimages/heart.png',random.randint(1,30)*20,random.randint(1,22)*20))

                #Powerup fucntionality
                cherryCol = pygame.sprite.spritecollide(self.pacman, self.cherryGroup, True)
                snowflakeCol = pygame.sprite.spritecollide(self.pacman, self.snowflakeGroup, True)
                bananaCol = pygame.sprite.spritecollide(self.pacman, self.bananaGroup, True)
                heartCol = pygame.sprite.spritecollide(self.pacman, self.heartGroup, True)


                #Deleting powerups when ghost collide with them
                for ghostGroup in self.ghostGroupList:
                    for powerupGroup in self.powerupGroupList:
                        pygame.sprite.groupcollide(ghostGroup, powerupGroup, False, True)

                if cherryCol and frame > cherryTime + 50: #Prevents two cherrys from being collected in the same time period
                    cherryTime = frame
                    pacmanSpeed /= 2
                if snowflakeCol and frame > snowflakeTime + 50:
                    snowflakeTime = frame
                    ghostSpeed *= 1000
                if bananaCol and frame > bananaTime + 50: #Prevents two bananas from being collected in the same time period
                    bananaTime = frame
                    ghostSpeed *= 2
                if heartCol:
                    self.bottombar.lives += 1

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
                            if ghost.rect.y >= height-80-20 or self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] != 1: #If the next block is 1 or .5
                                ghost.ymultiplier = -1
                                sidehit = True
                            elif ghost.rect.y <= 0 or self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] != 1:
                                ghost.ymultiplier = 1
                                sidehit = True
                            if ghost.rect.x >= width - 20 or self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] != 1:
                                ghost.xmultiplier = -1
                                sidehit = True
                            elif ghost.rect.x <= 0 or self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] != 1:
                                ghost.xmultiplier = 1
                                sidehit = True

                            #If the ghost hits a corner
                            if sidehit == False:
                                for xadd in [-1,1]:
                                    for yadd in [-1,1]:
                                        if self.screenmatrix.matrix[ghost.rect.x//20+xadd][ghost.rect.y//20+yadd] != 1 and ghost.xmultiplier == xadd and ghost.ymultiplier == yadd:
                                            ghost.xmultiplier = -xadd
                                            ghost.ymultiplier = -yadd

                    self.inkyGroup.update()

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
                                    self.boxes.update(self.screenmatrix)
                            elif  self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] == 1:
                                ghost.ymultiplier = 1
                                sidehit = True
                                if ghost.rect.y//20 != 1:
                                    self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] = 0
                                    self.boxes.update(self.screenmatrix)
                            if self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier = -1
                                sidehit = True
                                if ghost.rect.x//20 != 30:
                                    self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] = 0
                                    self.boxes.update(self.screenmatrix)
                            elif self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier = 1
                                sidehit = True
                                if ghost.rect.x//20 != 1:
                                    self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] = 0
                                    self.boxes.update(self.screenmatrix)


                            #If the ghost hits a corner
                            if sidehit == False:
                                for xadd in [-1,1]:
                                    for yadd in [-1,1]:
                                        if self.screenmatrix.matrix[ghost.rect.x//20+xadd][ghost.rect.y//20+yadd] == 1 and ghost.xmultiplier == xadd and ghost.ymultiplier == yadd:
                                            ghost.xmultiplier = -xadd
                                            ghost.ymultiplier = -yadd
                                            if ghost.rect.x//20 != 22 and ghost.rect.y//20 != 30 and ghost.rect.x//20 != 1 and ghost.rect.y//20 != 1:
                                                self.screenmatrix.matrix[ghost.rect.x//20+xadd][ghost.rect.y//20+yadd] = 0
                                                self.boxes.update(self.screenmatrix)

                            self.bottombar.percent = self.screenmatrix.getPercent()
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
                                        if self.screenmatrix.matrix[ghost.rect.x//20+xadd][ghost.rect.y//20+yadd] == 1 and ghost.xmultiplier == xadd and ghost.ymultiplier == yadd:
                                            ghost.xmultiplier = -xadd
                                            ghost.ymultiplier = -yadd
                    self.pinkyGroup.update()

                #Orange ghost bounce
                if frame % (ghostSpeed*3) == 0:
                    self.clydeGroup.update()


                #If pacman's trail (or pacman himself) is collided with by a ghost, let pacman lose a life and reset to the top left.
                for ghostGroup in self.ghostGroupList:
                    for box in pygame.sprite.groupcollide(ghostGroup, self.boxes,False, False):
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] == .5 or pygame.sprite.spritecollide(self.pacman, ghostGroup,False, False):
                            self.bottombar.lives -= 1
                            self.pacman.setPos(0,0)
                            self.screenmatrix.removeTrack()
                            break

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
                            boxesfilled = self.screenmatrix.getNumLastFilled()
                            self.bottombar.score +=  int(boxesfilled**1.6/200 + boxesfilled//2)#Score increases with an exponential function based on boxes filled. Rewards taking risks. (max of 170 if every box is filled
                            self.bottombar.percent = self.screenmatrix.getPercent()

                #Pacman moving functionality
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


                #Print the bottombar
                bottombar1 = self.barfont.render(self.bottombar.data()[0],False,(255,255,50))
                bottombar2 = self.barfont.render(self.bottombar.data()[1],False,(255,255,50))
                bottombar3 = pygame.transform.scale(pygame.image.load("assets/pacxon.png"),(640-250, 320))
                self.screen.blit(self.background,(0,0))
                self.screen.blit(bottombar1,(0,height-85))
                self.screen.blit(bottombar2,(0,height-45))
                self.screen.blit(bottombar3,(335,height-176))



                self.boxes.draw(self.screen)
                self.pacGroup.draw(self.screen)
                for powerupGroup in self.powerupGroupList:
                    powerupGroup.draw(self.screen)
                for ghostGroup in self.ghostGroupList:
                    ghostGroup.draw(self.screen)
                pygame.display.flip()

                #If pacman has 0 lives, show GAMEOVER screen
                if self.bottombar.lives == 0:
                    done = True
                    self.bottombar.level = 1
                    #Gameover Screen
                    gameoverdone = False
                    gameoverframe = 0
                    gameoverTop = self.myfont.render("GAMEOVER!",False,(255,255,50))
                    gameoverHelp = self.subfont.render("Press SPACEBAR to restart, Q to quit",False,(255,255,50))
                    gameoverScore = self.subfont.render("Your Score: "+str(self.bottombar.score),False,(255,255,50))
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

                        # Update High Score
                        if self.bottombar.score > self.bottombar.highScore:
                            fptr = open("assets/highscore.txt", "w")
                            fptr.write(str(self.bottombar.score))
                            self.bottombar.highScore = self.bottombar.score
                            fptr.close()
                        gameoverHighScore = self.subfont.render("High Score: "+str(self.bottombar.highScore),False,(255,255,50))

                        self.gameoverscreen.blit(self.gameoverbackground,(0,0))
                        self.gameoverscreen.blit(gameoverTop,(93,75))
                        self.gameoverscreen.blit(gameoverHelp,(110,210))
                        self.gameoverscreen.blit(gameoverScore,(240,310))
                        self.gameoverscreen.blit(gameoverHighScore,(230,410))
                        pygame.display.flip()
                        gameoverframe += 1


                if self.screenmatrix.getPercent() >= 80:
                    self.bottombar.level += 1
                    self.screenmatrix.reset()
                    self.pacman.setPos(0,0)
                    for ghostGroup in self.ghostGroupList:
                        ghostGroup.empty()
                    done = True
                    self.boxes.update(self.screenmatrix)
                    self.bottombar.lives += 2
                    leveldone = False
                    self.bottombar.percent = 0
                    self.bottombar.score += 250
