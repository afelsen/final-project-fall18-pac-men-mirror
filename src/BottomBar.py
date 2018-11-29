class bottomBar:
    def __init__(self, lives, level, highScore, score, percent):
        self.lives = lives
        self.level = level
        self.highScore = highScore
        self.score = score
        self.percent = percent
    def data(self):
        dataString = "Lives: " + str(self.lives) + " Level: " + str(self.level) + " High Score: " + str(self.highScore) + " Score: " + str(self.score) + " Percent " + str(self.percent)
        return dataString
