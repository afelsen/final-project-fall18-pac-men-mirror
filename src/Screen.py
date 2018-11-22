import pygame
class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[0]*self.height for i in range (self.width)]
        self.matrix[0] = [1]*self.height
        self.matrix[-1] = [1]*self.height
        for i in range(self.width):
            self.matrix[i][0] = 1
            self.matrix[i][-1] = 1
        self.finalpercent = 80
        self.currentpercent = 0

    def getMatrix(self):
        return self.matrix
    def trackPacman(self,pacmanPos):
        #Pacman pos in the format (x,y)
        if self.matrix[pacmanPos[0]][pacmanPos[1]] == 0:
            self.matrix[pacmanPos[0]][pacmanPos[1]] = .5

    def fillMatrix(self,pinkyGroup):

        #fills in the current line
        for i in range(24):
            for j in range(32):
                if self.matrix[j][i] == .5:
                    self.matrix[j][i] = 1

        ultimateAreaPoints = []
        done = False

        while not done:
            #find a starting point
            startingPoint = None
            for c in range(24):
                for r in range(32):
                    if self.matrix[r][c] == 0 and (r,c) not in ultimateAreaPoints:
                        startingPoint = (r,c)
                        break
            if startingPoint == None: #If all areas have been mapped
                done = True
                continue

            filled = False
            currentPoints = [startingPoint]
            #Check adjacent points to currentPoints. If those points have the matrix value of 0, append it to currentPoints.
            for p in currentPoints:
                if p[0] != 31 and (p[0]+1,p[1]) not in currentPoints:
                    if self.matrix[p[0]+1][p[1]] == 0:
                        currentPoints.append((p[0]+1,p[1]))
                if p[0] != 0 and (p[0]-1,p[1]) not in currentPoints:
                    if self.matrix[p[0]-1][p[1]] == 0:
                        currentPoints.append((p[0]-1,p[1]))
                if p[1] != 23 and (p[0],p[1]+1) not in currentPoints:
                    if self.matrix[p[0]][p[1]+1] == 0:
                        currentPoints.append((p[0],p[1]+1))
                if p[1] != 0 and (p[0],p[1]-1) not in currentPoints:
                    if self.matrix[p[0]][p[1]-1] == 0:
                        currentPoints.append((p[0],p[1]-1))

            #Add all currentPoints to the mater list of all points that have been checked
            for i in currentPoints:
                ultimateAreaPoints.append(i)

            #If pinky is not in the region, fill it in with 1s
            Pinky = False
            for pinky in pinkyGroup:
                if (pinky.rect.x//20,pinky.rect.y//20) in currentPoints:
                    Pinky = True
            if Pinky == False:
                for i in currentPoints:
                    self.matrix[i[0]][i[1]] = 1

class Box(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, screen):
        if screen.matrix[self.rect.x//20][self.rect.y//20] == 1:
            self.image = pygame.transform.scale(pygame.image.load('assets/Bluebox.png'),(20,20))
        if screen.matrix[self.rect.x//20][self.rect.y//20] == .5:
            self.image = pygame.transform.scale(pygame.image.load('assets/Halfwaybox.png'),(20,20))
