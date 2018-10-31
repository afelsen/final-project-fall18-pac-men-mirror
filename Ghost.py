import math

class Pinky: #Pink; normal bouncing ghost
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

class Inky: #Light blue; Bounces in fenced in areas
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

class Blinky: #Red; Breaks any block it hits - moves at 1/2 speed
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

class Clyde: #Orange; Follows the edges of the fences
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
