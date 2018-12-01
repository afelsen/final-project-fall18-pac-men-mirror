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
<<<<<<< HEAD

class Banana(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
=======

class Banana(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()

>>>>>>> ba2690bf87d3228fd4b1b432c545d077669b6aa2
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        return self.rect.x,self.rect.y

class Snowflake(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
<<<<<<< HEAD
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        return self.rect.x,self.rect.y

class Heart(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
=======

>>>>>>> ba2690bf87d3228fd4b1b432c545d077669b6aa2
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        return self.rect.x,self.rect.y
