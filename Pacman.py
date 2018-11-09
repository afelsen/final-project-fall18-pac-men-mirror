import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def __str__(self):
        string = "(x:" + str(self.rect.x) + ", y:" + str(self.rect.y) + ")" + " Speed" + self.speed
        return string
    def moveLeft(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
    def moveRight(self):
        self.rect.x += self.speed
        if self.rect.x > 640-20:
            self.rect.x = 640-20
    def moveDown(self):
        self.rect.y += self.speed
        if self.rect.y > 480-20:
            self.rect.y = 480-20
    def moveUp(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = 0
    def getCoordinates(self):
        return self.rect.x,self.rect.y
