class Pacman:
    def __init__(self, filename, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def __str__(self):
        string = "(x:" + str(self.x) + ", y:" + str(self.y) + ")" + " Speed" + self.speed
        return string
    def moveLeft(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0
    def moveRight(self):
        self.x += self.speed
        if self.x < 0:
            self.x = 0
    def moveDown(self):
        self.y += self.speed
        if self.y < 0:
            self.y = 0
    def moveUp(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0
    def getCoordinates(self):
        return self.x,self.y
