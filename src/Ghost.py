import math
import pygame
import random

class Pinky(pygame.sprite.Sprite): #Pink; normal bouncing ghost
    def __init__(self, filename, x, y, speed):
        '''
        initializes the Pinky class
        self, file name, x position, y position, and speed parameters
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = 45
        self.xmultiplier = random.choice([-1,1])
        self.ymultiplier = random.choice([-1,1])

    def update(self):
        '''
        updates the Pinky class's positon
        self

        '''
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2

    def getCoordinates(self):
        '''
        gets the coordinates of the Pinky class
        self
        returns x and y position
        '''
        return self.x,self.y

class Inky(pygame.sprite.Sprite): #Light blue; Bounces in fenced in areas
    def __init__(self, filename, x, y, speed):
        '''
        initializes the Inky class
        self, file name, x position, y position, and speed parameters
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = 45
        self.xmultiplier = random.choice([-1,1])
        self.ymultiplier = random.choice([-1,1])

    def update(self):
        '''
        updates the Inky class's positon
        self

        '''
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        '''
        gets the coordinates of the Inky class
        self
        returns x and y position
        '''
        return self.x,self.y

class Blinky(pygame.sprite.Sprite): #Red; Breaks any block it hits - moves at 1/2 speed
    def __init__(self, filename, x, y, speed):
        '''
        initializes the Blinky class
        self, file name, x position, y position, and speed parameters
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = 45
        self.xmultiplier = random.choice([-1,1])
        self.ymultiplier = random.choice([-1,1])

    def update(self):
        '''
        updates the Blinky class's positon
        self

        '''
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        '''
        gets the coordinates of the Blinky class
        self
        returns x and y position
        '''
        return self.x,self.y

class Clyde(pygame.sprite.Sprite): #Orange; Follows the edges of the fences
    def __init__(self, filename, x, y, speed):
        '''
        initializes the Clyde class
        self, file name, x position, y position, and speed parameters
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.clydeState = 0
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.xmultiplier = random.choice([-1,1])
        self.ymultiplier = random.choice([-1,1])

    def update(self):
        '''
        updates the Clyde class's positon
        self

        '''
        if self.clydeState == 0:
            self.clydeState += 1
            self.rect.x += 20
            self.rect.y += 20
        elif self.clydeState == 1:
            self.clydeState += 1
            self.rect.x += 20
            self.rect.y -= 20
        elif self.clydeState == 2:
            self.clydeState += 1
            self.rect.x -= 20
            self.rect.y -= 20
        elif self.clydeState == 3:
            self.clydeState = 0
            self.rect.x -= 20
            self.rect.y += 20
        print(self.rect.x)

    def getCoordinates(self):
        '''
        gets the coordinates of the Clyde class
        self
        returns x and y position
        '''
        return self.x,self.y
