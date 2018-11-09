class Screen:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.matrix = [[0]*self.width]*self.length
        self.matrix[0] = [1]*self.width
        self.matrix[-1] = [1]*self.width
        for i in range(self.length):
            self.matrix[i][0] = 1
            self.matrix[i][-1] = 1
        self.finalpercent = 80
        self.currentpercent = 0
    def getMatrix(self):
        return self.matrix
    def trackPacman(self,pacmanPos):
        #Pacman pos in the format (x,y)
        self.matrix[pacmanPos[1]][pacmanPos[0]] = 1
    def fillArea(self):
        pass
