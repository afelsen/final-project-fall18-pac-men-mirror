import math
import pygame

class Pinky(pygame.sprite.Sprite): #Pink; normal bouncing ghost
    def __init__(self, filename, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = 45
        self.xmultiplier = 1
        self.ymultiplier = -1

    def update(self, direction):
        if self.rect.x <= 0:
            self.xmultiplier = 1
        if self.rect.x >= 640-20:
            self.xmultiplier = -1
        if self.rect.y <=0:
            self.ymultiplier = 1
        if self.rect.y >=480-20:
            self.ymultiplier = -1
        print(self.rect.y)
        self.rect.x += self.xmultiplier*self.speed/2
        self.rect.y += self.ymultiplier*self.speed/2


    def getCoordinates(self):
        return self.x,self.y

class Inky(pygame.sprite.Sprite): #Light blue; Bounces in fenced in areas
    def __init__(self, filename, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def move(self, direction):
        direction = math.radians(direction)
        self.x += self.speed*math.cos(direction)
        self.y += self.speed*math.sin(direction)
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
    def getCoordinates(self):
        return self.x,self.y

class Blinky(pygame.sprite.Sprite): #Red; Breaks any block it hits - moves at 1/2 speed
    def __init__(self, filename, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def move(self, direction):
        direction = math.radians(direction)
        self.x += self.speed*math.cos(direction)
        self.y += self.speed*math.sin(direction)
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
    def getCoordinates(self):
        return self.x,self.y

class Clyde(pygame.sprite.Sprite): #Orange; Follows the edges of the fences
    def __init__(self, filename, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def move(self, direction):
        direction = math.radians(direction)
        self.x += self.speed*math.cos(direction)
        self.y += self.speed*math.sin(direction)
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
    def getCoordinates(self):
        return self.x,self.y
