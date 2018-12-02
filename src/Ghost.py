import math
import pygame
import random

class Pinky(pygame.sprite.Sprite): #Pink; normal bouncing ghost
    def __init__(self, filename, x, y, speed):
        '''
        Initializes the Pinky class
        args:
            filename (str) - image filename
            x (int) - initial x position
            y (int) - initial y position
            speed (int) - ghost speed
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.xmultiplier = random.choice([-1,1])
        self.ymultiplier = random.choice([-1,1])

    def update(self):
        '''
        Updates the each Pinky object's positon
        '''
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2

    def getCoordinates(self):
        '''
        Gets the coordinates of the Pinky ghosts
        Returns: self.x,self.y (tup) - x and y position
        '''
        return self.rect.x,self.rect.y

class Inky(pygame.sprite.Sprite): #Light blue; Bounces in fenced in areas
    def __init__(self, filename, x, y, speed):
        '''
        Initializes the Inky class
        args:
            filename (str) - image filename
            x (int) - initial x position
            y (int) - initial y position
            speed (int) - ghost speed
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
        Updates each Inky object's positon
        '''
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        '''
        Gets the coordinates of each Inky ghost
        Returns: x and y position
        '''
        return self.rect.x,self.rect.y

class Blinky(pygame.sprite.Sprite): #Red; Breaks any block it hits - moves at 1/2 speed
    def __init__(self, filename, x, y, speed):
        '''
        Initializes the Blinky class
        args:
            filename (str) - image filename
            x (int) - initial x position
            y (int) - initial y position
            speed (int) - ghost speed
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
        Updates each Blinky object's positon
        '''
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        '''
        Gets the coordinates of each Blinky ghost
        Returns: self.x,self.y (tup) - x and y position
        '''
        return self.rect.x,self.rect.y

class Clyde(pygame.sprite.Sprite): #Orange; Follows the edges of the fences
    def __init__(self, filename, x, y, speed):
        '''
        Initializes the Clyde class
        args:
            filename (str) - image filename
            x (int) - initial x position
            y (int) - initial y position
            speed (int) - ghost speed
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.clydeState = random.choice(range(4))

    def update(self):
        '''
        Updates each Clyde object's positon (moves in a diamond shape)
        '''
        if self.clydeState == 0:
            self.clydeState += 1
            self.rect.x += self.speed
            self.rect.y += self.speed
        elif self.clydeState == 1:
            self.clydeState += 1
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.clydeState == 2:
            self.clydeState += 1
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.clydeState == 3:
            self.clydeState = 0
            self.rect.x -= self.speed
            self.rect.y += self.speed

    def getCoordinates(self):
        '''
        Gets the coordinates of the Clyde class
        Returns: self.x,self.y (tup) - x and y position
        '''
        return self.rect.x,self.rect.y
