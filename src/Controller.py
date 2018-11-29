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

        self.cherry = Powerup.Cherry('assets/cherry.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.cherryGroup = pygame.sprite.Group(self.cherry)
        self.banana = Powerup.Banana('assets/banana.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.bananaGroup = pygame.sprite.Group(self.banana)
        self.snowflake = Powerup.Snowflake('assets/snowflake.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.snowflakeGroup = pygame.sprite.Group(self.snowflake)
        self.powerpellet = Powerup.Powerpellet('assets/powerpellet.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.powerpelletGroup = pygame.sprite.Group(self.powerpellet)
        self.powerupGroupList = [self.cherryGroup,self.bananaGroup,self.snowflakeGroup,self.powerpelletGroup]

        self.boxes = pygame.sprite.Group()
        self.screenmatrix = Screen.Screen(width//20,(height-40)//20)
        self.lives = TopBar.Lives('assets/PacmanMiddle.png',5,5)
        self.bottombar = BottomBar.bottomBar(2,2,2,2,2)


        for i in range(0,width,20):
            for j in range(0,height-40,20):
                self.boxes.add(Screen.Box(i,j,'assets/EmptyBox.png'))
        self.boxes.update(self.screenmatrix)

        done = False
        introdone = False
        pacmanSpeed = 2
        ghostSpeed = 2
        generalSpeed = 2
        frame = 1
        #_____Time are variables that keep track of what frame a powerup was collided with
        cherryTime = -100
        bananaTime = -100
        snowflakeTime = -100
        powerpelletTime = -100
        notOnFilled = False
        self.pacDirection = ""
        self.pinkyangle = 45

        self.menuscreen = pygame.display.set_mode((width,height))
        self.menubackground = pygame.Surface(self.menuscreen.get_size()).convert()
        pygame.font.init()
        self.myfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 75)
        self.subfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 25)
        self.midfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 50)
        self.barfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 30)

        self.level = 1
        while self.level < 100:

            for i in range(self.level + 1):
                self.pinkyGroup.add(Ghost.Pinky('assets/pinky.png',random.randint(2,29)*20,random.randint(2,21)*20,20))
            ######## Here you add the spawning of all ghosts ########
            #Make sure to create a group at the top and use a for loop to add the ghosts in with some function (2*level or level + 1, etc.)
            for i in range(self.level + 2):
                self.inkyGroup.add(Ghost.Inky('assets/inky.png',random.randint(2,29)*20,random.randint(2,21)*20,20))
            for i in range(self.level + 3):
                self.blinkyGroup.add(Ghost.Blinky('assets/blinky.png',random.randint(2,29)*20,random.randint(2,21)*20,20))
            for i in range(self.level * 2):
                self.clydeGroup.add(Ghost.Clyde('assets/clyde.png',random.randint(2,29)*20,random.randint(2,21)*20,20))

            while not done:
                while not introdone:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            introdone = True
                            done = True
                            self.level = 100
                        keys = pygame.key.get_pressed()
                        textTop = self.myfont.render("PacXon",False,(255,255,50))
                        textBottom = self.subfont.render("Created by the PacMen",False,(255,255,50))
                        textHelp = self.subfont.render("Press SPACEBAR to start!",False,(255,255,50))
                        textControls = self.subfont.render("Controls: Arrow keys to move and Q to quit",False,(255,255,50))

                    if frame % 1 == 0:
                        if keys[pygame.K_SPACE]: # space to start
                            introdone = True
                            self.level = 100
                        elif keys[pygame.K_q]: # q to quit
                            introdone = True
                            done = True
                            self.level = 100
                        frame += 1
                        self.menuscreen.blit(self.menubackground,(0,0))
                        self.menuscreen.blit(textTop,(205,75))
                        self.menuscreen.blit(textBottom,(200,300))
                        self.menuscreen.blit(textHelp,(180,210))
                        self.menuscreen.blit(textControls,(0,485))
                        pygame.display.flip()

                ######## Here add a "Level ___" screen ########
                # if getPercent() > 80:
                    # self.level += 1
                    # self.levelscreen = pygame.display.set_mode((width,height))
                    # self.levelbackground = pygame.Surface(self.menuscreen.get_size()).convert()
                    # levelText = self.myfont.render("Level",False,(255,255,50))
                    # levelnumberText = self.myfont.render(str(self.level),False,(255,255,255))
                    # self.levelscreen.blit(self.levelbackground,(0,0))
                    # self.levelscreen.blit(levelText,(205,125))
                    # self.levelscreen.blit(levelnumberText,(305,125))


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        self.level = 100

                ######## Here add random powerup spawning ########

                #Powerup fucntionality

                powerpelletCol = pygame.sprite.spritecollide(self.pacman, self.powerpelletGroup, True)
                cherryCol = pygame.sprite.spritecollide(self.pacman, self.cherryGroup, True)
                snowflakeCol = pygame.sprite.spritecollide(self.pacman, self.snowflakeGroup, True)
                bananaCol = pygame.sprite.spritecollide(self.pacman, self.bananaGroup, True)

                #Deleting powerups when ghost collide with them
                for ghostGroup in self.ghostGroupList:
                    for powerupGroup in self.powerupGroupList:
                        pygame.sprite.groupcollide(ghostGroup, powerupGroup, False, True)

                if powerpelletCol:
                    powerpelletTime = frame
                    pacmanInvicible = True
                if cherryCol:
                    cherryTime = frame
                    pacmanSpeed /= 2
                if snowflakeCol:
                    snowflakeTime = frame
                    ghostSpeed *= 1000
                if bananaCol:
                    bananaTime = frame
                    ghostSpeed *= 2

                if frame == powerpelletTime + 50:
                    pacmanInvincible = False
                if frame == cherryTime + 50:
                    pacmanSpeed *= 2
                if frame == snowflakeTime + 50:
                    ghostSpeed /= 1000
                if frame == bananaTime + 50:
                    ghostSpeed /= 2

                pinkyCol = pygame.sprite.groupcollide(self.pinkyGroup,self.boxes,False, False)
                inkyCol = pygame.sprite.groupcollide(self.inkyGroup,self.boxes,False,False)
                blinkyCol = pygame.sprite.groupcollide(self.blinkyGroup,self.boxes,False,True)


                ## Ghost bouncing
                if (inkyCol and (frame % ghostSpeed) == 0):
                    for ghost in pygame.sprite.groupcollide(self.inkyGroup,self.boxes,False, False):
                        if (ghost.rect.x/20).is_integer() and (ghost.rect.y/20).is_integer():
                            if self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] == 1 or  self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] == 1:
                                ghost.ymultiplier *= -1
                            if self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] == 1 or  self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier *= -1
                    self.inkyGroup.update()

                if (blinkyCol and (frame %ghostSpeed) == 0):
                    for ghost in pygame.sprite.groupcollide(self.blinkyGroup,self.boxes,False,False):
                        if (ghost.rect.x/20).is_integer() and (ghost.rect.y/20).is_integer():
                            if self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] == 1 or  self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] == 1:
                                ghost.ymultiplier *= -1
                            if self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] == 1 or  self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] == 1:
                                ghost.xmultiplier *= -1
                    self.blinkyGroup.update()

                if (pinkyCol and (frame % ghostSpeed) == 0):
                    for ghost in pygame.sprite.groupcollide(self.pinkyGroup,self.boxes,False, False):
                        if (ghost.rect.x/20).is_integer() and (ghost.rect.y/20).is_integer():
                            if self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20+1] == 1 or  self.screenmatrix.matrix[ghost.rect.x//20][ghost.rect.y//20-1] == 1: #If the ghost collides on top or bottom
                                ghost.ymultiplier *= -1
                            if self.screenmatrix.matrix[ghost.rect.x//20+1][ghost.rect.y//20] == 1 or  self.screenmatrix.matrix[ghost.rect.x//20-1][ghost.rect.y//20] == 1: #If the ghost collides on left or right
                                ghost.xmultiplier *= -1
                    self.pinkyGroup.update()


                #Pacman-box collision
                overbox = pygame.sprite.spritecollide(self.pacman, self.boxes, False)
                if(overbox):
                    for box in pygame.sprite.spritecollide(self.pacman, self.boxes, False):
                        self.screenmatrix.trackPacman((box.rect.x//20,box.rect.y//20))
                        box.update(self.screenmatrix)
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] != 1:
                            notOnFilled = True
                            #This prevents the next lines from running over and over if the pacman is just staying in the "filled area"
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] == 1 and notOnFilled == True:
                            self.screenmatrix.fillMatrix(self.ghostGroupList)
                            self.boxes.update(self.screenmatrix)
                            notOnFilled = False


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


                ########Add collision with pacman's trail here########
                #If pacman's trail is collided with by a ghost or by pacman, let pacman lose a life, reset to the top left.
                trailpacCol = pygame.sprite.groupcollide(self.pacGroup, self.boxes,False, False)
                trailpinkyCol = pygame.sprite.groupcollide(self.pinkyGroup, self.boxes,False, False)
                trailinkyCol = pygame.sprite.groupcollide(self.inkyGroup, self.boxes,False, False)
                trailblinkyCol = pygame.sprite.groupcollide(self.blinkyGroup, self.boxes,False, False)
                trailclydeCol = pygame.sprite.groupcollide(self.clydeGroup, self.boxes,False, False)

                # if trailpacCol:
                #     for box in pygame.sprite.spritecollide(self.pacman, self.boxes, False):
                #         #if self.screenmatrix[box.rect.x//20][box.rect.y//20] == .5
                #         self.bottombar.lives -= 1
                #         self.pacman.setPos(0,0)
                if trailpinkyCol:
                    for box in pygame.sprite.groupcollide(self.pinkyGroup, self.boxes,False, False):
                        if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] == .5:
                            self.bottombar.lives -= 1
                            self.pacman.setPos(0,0)
                            self.screenmatrix.removeTrack()
                # if trailinkyCol:
                #     self.bottombar.lives -= 1
                #     self.pacman.setPos(0,0)
                # if trailblinkyCol:
                #     self.bottombar.lives -= 1
                #     self.pacman.setPos(0,0)
                # if trailclydeCol:
                #     self.bottombar.lives -= 1
                #     self.pacman.setPos(0,0)


                ########Add loss functionality here########
                #If pacman has 0 lives, set done = true, and level = 100
                    ########Add Game Over Screen########
                # if self.bottombar.lives == 0:
                #     done = True
                #     self.level = 1
                #     self.gameoverscreen = pygame.display.set_mode((width,height))
                #     self.gameoverscreenbackground = pygame.Surface(self.menuscreen.get_size()).convert()
                #     gameoverText = self.myfont.render("Game Over!",False,(255,0,0))
                #     self.gameoverscreen.blit(self.levelbackground,(0,0))
                #     self.gameoverscreen.blit(gameoverText,(205,125))


                ########Add win functionality here########
                #If the screen is >= 80% full, set done = true, level += 1
                # if self.screen.getPercent() > 80:
                #     done = True
                #     level += 1


                bottombar = self.barfont.render(self.bottombar.data(),False,(255,255,50))
                self.screen.blit(self.background,(0,0))
                self.screen.blit(bottombar,(0,475))


                self.boxes.draw(self.screen)
                self.pacGroup.draw(self.screen)
                for powerupGroup in self.powerupGroupList:
                    powerupGroup.draw(self.screen)
                for ghostGroup in self.ghostGroupList:
                    ghostGroup.draw(self.screen)
                pygame.display.flip()
