import pygame
import random
from src import Pacman
from src import Ghost
from src import Powerup
from src import Screen

class Controller:
    def __init__(self, width = 640, height = 520):
        self.screen = pygame.display.set_mode((width,height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.pacman = Pacman.Pacman('assets/PacmanOpen.png',0,0,20)
        self.pacGroup = pygame.sprite.Group(self.pacman)
        self.pinky1 = Ghost.Pinky('assets/pinky.png',random.randint(1,30)*20,random.randint(1,22)*20,20)
        self.pinky2 = Ghost.Pinky('assets/pinky.png',random.randint(1,30)*20,random.randint(1,22)*20,20)
        self.pinkyGroup = pygame.sprite.Group(self.pinky1,self.pinky2)
        self.cherry = Powerup.Cherry('assets/cherry.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.cherryGroup = pygame.sprite.Group(self.cherry)
        self.banana = Powerup.Banana('assets/banana.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.bananaGroup = pygame.sprite.Group(self.banana)
        self.snowflake = Powerup.Snowflake('assets/snowflake.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.snowflakeGroup = pygame.sprite.Group(self.snowflake)
        self.powerpellet = Powerup.Powerpellet('assets/powerpellet.png',random.randint(1,30)*20,random.randint(1,22)*20)
        self.powerpelletGroup = pygame.sprite.Group(self.powerpellet)
        self.boxes = pygame.sprite.Group()
        self.screenmatrix = Screen.Screen(width//20,(height-40)//20)

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
        while not done:
            self.menuscreen = pygame.display.set_mode((width,height))
            self.menubackground = pygame.Surface(self.menuscreen.get_size()).convert()
            pygame.font.init()
            self.myfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 75)
            self.subfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 25)
            self.midfont = pygame.font.Font("assets/KaushanScript-Regular.otf", 50)
            while not introdone:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        introdone = True
                        done = True
                    keys = pygame.key.get_pressed()
                    textTop = self.myfont.render("PacXon",False,(255,255,50))
                    textBottom = self.subfont.render("Created by the PacMen",False,(255,255,50))
                    textHelp = self.subfont.render("Press SPACEBAR to start!",False,(255,255,50))
                    textControls = self.subfont.render("Controls: Arrow keys and Q to quit",False,(255,255,50))
                if frame % 1 == 0:
                    if keys[pygame.K_SPACE]: # space to start
                        introdone = True
                    elif keys[pygame.K_q]: # q to quit
                        introdone = True
                        done = True
                    frame += 1
                    self.menuscreen.blit(self.menubackground,(0,0))
                    self.menuscreen.blit(textTop,(205,75))
                    self.menuscreen.blit(textBottom,(200,300))
                    self.menuscreen.blit(textHelp,(180,210))
                    self.menuscreen.blit(textControls,(0,440))
                    pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.pacDirection = "U"
                self.pacman.angle = 90
            elif keys[pygame.K_DOWN]:
                self.pacDirection = "D"
                self.pacman.angle = 270
            elif keys[pygame.K_LEFT]:
                self.pacDirection = "L"
                self.pacman.angle = 180
            elif keys[pygame.K_RIGHT]:
                self.pacDirection = "R"
                self.pacman.angle = 0
            elif keys[pygame.K_q]:
                done = True


            if frame % pacmanSpeed == 0:
                if self.pacDirection == "U":
                    self.pacman.moveUp()
                if self.pacDirection == "D":
                    self.pacman.moveDown()
                if self.pacDirection == "L":
                    self.pacman.moveLeft()
                if self.pacDirection == "R":
                    self.pacman.moveRight()
            if frame % ghostSpeed == 0:
                self.pinkyGroup.update()

            if frame % generalSpeed == 0:
                self.pacman.animate()
            frame += 1

            #Powerup fucntionality
            powerpelletCol = pygame.sprite.spritecollide(self.pacman, self.powerpelletGroup, True)
            cherryCol = pygame.sprite.spritecollide(self.pacman, self.cherryGroup, True)
            snowflakeCol = pygame.sprite.spritecollide(self.pacman, self.snowflakeGroup, True)
            bananaCol = pygame.sprite.spritecollide(self.pacman, self.bananaGroup, True)

            #Pinky collide
            pygame.sprite.groupcollide(self.pinkyGroup, self.powerpelletGroup, False, True)
            pygame.sprite.groupcollide(self.pinkyGroup, self.cherryGroup, False, True)
            pygame.sprite.groupcollide(self.pinkyGroup, self.snowflakeGroup, False, True)
            pygame.sprite.groupcollide(self.pinkyGroup, self.bananaGroup, False, True)


            if powerpelletCol:
                pass
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
                pass
            if frame == cherryTime + 50:
                pacmanSpeed *= 2
            if frame == snowflakeTime + 50:
                ghostSpeed /= 1000
            if frame == bananaTime + 50:
                ghostSpeed /= 2





            overbox = pygame.sprite.spritecollide(self.pacman, self.boxes, False)
            if(overbox):
                for box in pygame.sprite.spritecollide(self.pacman, self.boxes, False):
                    self.screenmatrix.trackPacman((box.rect.x//20,box.rect.y//20))
                    box.update(self.screenmatrix)
                    if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] != 1:
                        notOnFilled = True
                        #This prevents the next lines from running over and over if the pacman is just staying in the "filled area"
                    if self.screenmatrix.matrix[box.rect.x//20][box.rect.y//20] == 1 and notOnFilled == True:
                        self.screenmatrix.fillMatrix(self.pinkyGroup)
                        self.boxes.update(self.screenmatrix)
                        notOnFilled = False

            self.screen.blit(self.background,(0,0))
            self.boxes.draw(self.screen)
            self.pacGroup.draw(self.screen)
            self.powerpelletGroup.draw(self.screen)
            self.snowflakeGroup.draw(self.screen)
            self.pinkyGroup.draw(self.screen)
            self.cherryGroup.draw(self.screen)
            self.bananaGroup.draw(self.screen)

            pygame.display.flip()
