import math
import pygame
import random

class Pinky(pygame.sprite.Sprite): #Pink; normal bouncing ghost
    def __init__(self, filename, x, y, speed):
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
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2

    def getCoordinates(self):
        return self.x,self.y

class Inky(pygame.sprite.Sprite): #Light blue; Bounces in fenced in areas
    def __init__(self, filename, x, y, speed):
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
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        return self.x,self.y

class Blinky(pygame.sprite.Sprite): #Red; Breaks any block it hits - moves at 1/2 speed
    def __init__(self, filename, x, y, speed):
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
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        return self.x,self.y

class Clyde(pygame.sprite.Sprite): #Orange; Follows the edges of the fences
    def __init__(self, filename, x, y, speed):
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
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        return self.x,self.y
