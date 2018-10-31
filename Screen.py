class Screen:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.matrix = [[0]*self.width]*self.length
        self.finalpercent = 80
        self.currentpercent = 0
    def getMatrix(self):
        return self.matrix
