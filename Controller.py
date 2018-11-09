import pygame
import Pacman
import Ghost
import Powerup

class Controller:
    def __init__(self, width = 640, height = 480):
        self.screen = pygame.display.set_mode((width,height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.pacman = Pacman.Pacman('Pacman.png',100,100,20)
        self.pacGroup = pygame.sprite.Group(self.pacman)
        self.pinky1 = Ghost.Pinky('pinky.png',100,100,20)
        self.pinky2 = Ghost.Pinky('pinky.png',200,200,20)
        self.pinkyGroup = pygame.sprite.Group(self.pinky1,self.pinky2)
        self.cherry = Powerup.Cherry('cherry.png',300,300)
        self.cherryGroup = pygame.sprite.Group(self.cherry)
        self.banana = Powerup.Banana('banana.png',400,400)
        self.bananaGroup = pygame.sprite.Group(self.banana)


        done = False
        introdone = False
        frame = 1
        self.pacDirection = ""
        self.pinkyangle = 45
        self.pacangle = 0
        while not done:
            self.menuscreen = pygame.display.set_mode((width,height))
            self.menubackground = pygame.Surface(self.menuscreen.get_size()).convert()
            pygame.font.init()
            self.myfont = pygame.font.Font("KaushanScript-Regular.otf", 50)
            self.subfont = pygame.font.Font("KaushanScript-Regular.otf", 25)
            frame = 1
            while not introdone:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        introdone = True
                        done = True
                keys = pygame.key.get_pressed()
                if frame % 1 == 0:
                    textTop = self.myfont.render("PacXon",False,(50,50,50))
                    textBottom = self.subfont.render("Created by the PacMen",False,(50,50,50))
                    if keys[pygame.K_SPACE]: # space to start
                        introdone = True
                    frame += 1
                    self.menuscreen.blit(self.menubackground,(0,0))
                    self.menuscreen.blit(textTop,(242,100))
                    self.menuscreen.blit(textBottom,(200,300))
                    pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            keys = pygame.key.get_pressed()
            if frame % 1 == 0:
                if keys[pygame.K_UP]:
                    self.pacDirection = "U"
                elif keys[pygame.K_DOWN]:
                    self.pacDirection = "D"
                elif keys[pygame.K_LEFT]:
                    self.pacDirection = "L"
                elif keys[pygame.K_RIGHT]:
                    self.pacDirection = "R"

                if self.pacDirection == "U":
                    self.pacman.moveUp()
                if self.pacDirection == "D":
                    self.pacman.moveDown()
                if self.pacDirection == "L":
                    self.pacman.moveLeft()
                if self.pacDirection == "R":
                    self.pacman.moveRight()

                self.pinkyGroup.update(self.pinkyangle)

            frame += 1

            self.screen.blit(self.background,(0,0))
            self.pacGroup.draw(self.screen)
            self.pinkyGroup.draw(self.screen)
            self.cherryGroup.draw(self.screen)
            self.bananaGroup.draw(self.screen)

            pygame.display.flip()


def main():
    controller = Controller()

main()
