import pygame

class Cherry(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        return self.rect.x,self.rect.y

class Banana(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        return self.rect.x,self.rect.y

class Snowflake(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        return self.rect.x,self.rect.y

class Powerpellet(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        return self.rect.x,self.rect.y
