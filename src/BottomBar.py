class bottomBar:
    def __init__(self, lives, level, highScore, score, percent):
        '''
        initializes the bottomBar class
        self, lives, level, high score, score, and percent parameters
        '''
        self.lives = lives
        self.level = level
        self.highScore = highScore
        self.score = score
        self.percent = percent
    def data(self):
        '''
        Saves two strings as variables
        self
        returns two strings containing game information
        '''
        dataString1 = "Lives: " + str(self.lives) + " Level: " + str(self.level) + " Percent " + str(self.percent)
        dataString2 = "High Score: " + str(self.highScore) + " Score: " + str(self.score)
        return dataString1,dataString2
