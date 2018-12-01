import pygame

class Cherry(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        '''
        Initializes the Cherry class
        Args:
            filename (str) - cherry image filename
            x (int) - cherry starting x position
            y (int) - cherry starting y position
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        '''
        Gets the cherry's coordinates
        Returns: self.rect.x,self.rect.y (tup) - x and y positions of the cherry
        '''
        return self.rect.x,self.rect.y

class Banana(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        '''
        Initializes the Banana class
        Args:
            filename (str) - banana image filename
            x (int) - banana starting x position
            y (int) - banana starting y position
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        '''
        Gets the banana's coordinates
        Returns: self.rect.x,self.rect.y (tup) - x and y positions of the banana
        '''
        return self.rect.x,self.rect.y

class Snowflake(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        '''
        Initializes the Snowflake class
        Args:
            filename (str) - snowflake image filename
            x (int) - snowflake starting x position
            y (int) - snowflake starting y position
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        '''
        Gets the snowflake's coordinates
        Returns: self.rect.x,self.rect.y (tup) - x and y positions of the snowflake
        '''
        return self.rect.x,self.rect.y

class Heart(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        '''
        Initializes the Heart class
        Args:
            filename (str) - heart image filename
            x (int) - heart starting x position
            y (int) - heart starting y position
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        '''
        Gets the heart's coordinates
        Returns: self.rect.x,self.rect.y (tup) - x and y positions of the heart
        '''
        return self.rect.x,self.rect.y
