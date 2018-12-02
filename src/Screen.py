import pygame
class Screen:
    def __init__(self, width, height):
        '''
        Initializes the Screen class
        args:
            width (int) - width of screen
            height (int) - height of screen
        '''
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
        self.numpointsfilled = 0

    def getMatrix(self):
        '''
        Gets the matrix
        Returns: self.matrix (list) - the matrix
        '''
        return self.matrix
    def trackPacman(self,pacmanPos):
        '''
        Tracks pacman's position - turns the matrix value of his position to .5
        Args: pacmanPos (tup) - Pacman's current position
        '''
        if self.matrix[pacmanPos[0]][pacmanPos[1]] == 0:
            self.matrix[pacmanPos[0]][pacmanPos[1]] = .5
            self.numpointsfilled +=1

    def fillMatrix(self,ghostGroupList):
        '''
        Fills in the matrix in areas without a ghost that are fenced in
        Args: ghostGroupList - List of each ghost group
        '''
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[j][i] == .5:
                    self.matrix[j][i] = 1

        ultimateAreaPoints = []
        done = False

        while not done:
            #find a starting point
            startingPoint = None
            for c in range(self.height):
                for r in range(self.width):
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
                if p[0] != self.width-1 and (p[0]+1,p[1]) not in currentPoints:
                    if self.matrix[p[0]+1][p[1]] == 0:
                        currentPoints.append((p[0]+1,p[1]))
                if p[0] != 0 and (p[0]-1,p[1]) not in currentPoints:
                    if self.matrix[p[0]-1][p[1]] == 0:
                        currentPoints.append((p[0]-1,p[1]))
                if p[1] != self.height-1 and (p[0],p[1]+1) not in currentPoints:
                    if self.matrix[p[0]][p[1]+1] == 0:
                        currentPoints.append((p[0],p[1]+1))
                if p[1] != 0 and (p[0],p[1]-1) not in currentPoints:
                    if self.matrix[p[0]][p[1]-1] == 0:
                        currentPoints.append((p[0],p[1]-1))

            #Add all currentPoints to the mater list of all points that have been checked
            for i in currentPoints:
                ultimateAreaPoints.append(i)

            #If ghost is not in the region, fill it in with 1s
            Ghost = False
            for ghostGroup in ghostGroupList:
                for ghost in ghostGroup:
                    if (ghost.rect.x//20,ghost.rect.y//20) in currentPoints:
                        Ghost = True
            if Ghost == False:
                for i in currentPoints:
                    self.matrix[i[0]][i[1]] = 1
                    self.numpointsfilled += 1
    def reset(self):
        '''
        Resets the middle of the matrix to zero
        '''
        for i in range(1,self.height-1):
            for j in range(1,self.width-1):
                self.matrix[j][i] = 0

    def getNumLastFilled(self):
        '''
        Gets the number of boxes filled during last matrix fill
        Returns: final (int) - the number of filled boxes
        '''
        final = self.numpointsfilled
        self.numpointsfilled = 0
        return final


    def getPercent(self):
        '''
        Gets the percent of the screen that is filled in
        Returns: Final (int) - the percent of screen filled
        '''
        accum = 0
        total = 0
        for i in range(1,self.height-1):
            for j in range(1,self.width-1):
                if self.matrix[j][i] == 1:
                    accum += 1
                total += 1
        final = int((accum/total)*100)
        return final

    def removeTrack(self):
        '''
        Removes any trail that the Pacman has made
        '''
        for i in range(1,self.height-1):
            for j in range(1,self.width-1):
                if self.matrix[j][i] == .5:
                    self.matrix[j][i] = 0

class Box(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        '''
        Initializes the Box class
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, screen):
        '''
        Updates the each box's image
        Args: screen (src.Screen.Screen) - The Screen object
        '''
        if screen.matrix[self.rect.x//20][self.rect.y//20] == 1:
            self.image = pygame.transform.scale(pygame.image.load('assets/screenimages/Bluebox.png'),(20,20))
        if screen.matrix[self.rect.x//20][self.rect.y//20] == .5:
            self.image = pygame.transform.scale(pygame.image.load('assets/screenimages/Halfwaybox.png'),(20,20))
        if screen.matrix[self.rect.x//20][self.rect.y//20] == 0:
            self.image = pygame.transform.scale(pygame.image.load('assets/screenimages/EmptyBox.png'),(20,20))
