class Bottombar:
    def __init__(self, lives, level, highScore, score, percent):
        '''
        Initializes the bottomBar class
        args:
            lives (int) - current lives
            level (int) - current level
            high score (int) - high score
            score (int) - current score
            percent (int) - percent of screen filled
        '''
        self.lives = lives
        self.level = level
        self.highScore = highScore
        self.score = score
        self.percent = percent
    def data(self):
        '''
        Saves two strings as variables
        Returns: dataString1,dataString2 (tup) - two strings containing game information
        '''
        dataString1 = "Lives: " + str(self.lives) + " Level: " + str(self.level) + " Percent: " + str(self.percent)
        dataString2 = "High Score: " + str(self.highScore) + " Score: " + str(self.score)
        return dataString1,dataString2
