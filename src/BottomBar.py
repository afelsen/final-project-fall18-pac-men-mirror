class bottomBar:
    def __init__(self, lives, level, highScore, score, percent):
        self.lives = lives
        self.level = level
        self.highScore = highScore
        self.score = score
        self.percent = percent
    def data(self):
        dataString1 = "Lives: " + str(self.lives) + " Level: " + str(self.level) + " Percent " + str(self.percent)
        dataString2 = "High Score: " + str(self.highScore) + " Score: " + str(self.score)
        return dataString1,dataString2
