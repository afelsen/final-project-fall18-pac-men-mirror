import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, speed):
        '''
        Initializes the pacman class
        Args:
            filename (str) - Pacman image filename
            x (int) - Pacman's starting x position
            y (int) - Pacman's starting y position
            speed (int) - Pacman's speed
        '''
        pygame.sprite.Sprite.__init__(self)
        self.imageorig = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.image = self.imageorig
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = 3
        self.speed = speed
        self.mouthState = 0
        self.angle = 0
    def __str__(self):
        '''
        Returns the Pacman object as a string
        Returns: string (str) - Pacman's x, y coordinates and speed
        '''
        string = "(x:" + str(self.rect.x) + ", y:" + str(self.rect.y) + ")" + " Speed" + self.speed
        return string
    def moveLeft(self):
        '''
        Moves pacman left
        '''
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
    def moveRight(self):
        '''
        Moves pacman right
        '''
        self.rect.x += self.speed
        if self.rect.x > 640-20:
            self.rect.x = 640-20
    def moveDown(self):
        '''
        Moves pacman down
        '''
        self.rect.y += self.speed
        if self.rect.y > 480-20:
            self.rect.y = 480-20
    def moveUp(self):
        '''
        Moves pacman up
        '''
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = 0
    def setPos(self,x,y):
        '''
        Sets pacman's position
        Args:
            x (int) - Desired x position
            y (int) - Desired y position
        '''
        self.rect.x = x
        self.rect.y = y
    def getCoordinates(self):
        '''
        Gets pacman's coordinates
        Returns: self.rect.x,self.rect.y (tup) - x and y positions of pacman
        '''
        return self.rect.x,self.rect.y
    def animate(self):
        '''
        Pacman's animation
        '''
        if self.mouthState == 0:
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/pacmanimages/PacmanOpen.png'),(20,20)),self.angle)
            self.mouthState += 1
        elif self.mouthState == 1:
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/pacmanimages/PacmanMiddle.png'),(20,20)),self.angle)
            self.mouthState += 1
        else:
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/pacmanimages/PacmanClosed.png'),(20,20)),self.angle)
            self.mouthState = 0
