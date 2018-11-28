class bottomBar:
    def __init__(self, lives, level, highScore, score, percent):
        self.lives = 2
        self.level = 2
        self.highScore = 2
        self.score = 2
        self.percent = 2
    def data(self):
        dataString = "Lives: " + str(self.lives) + " Level: " + str(self.level) + " High Score: " + str(self.highScore) + " Score: " + str(self.score) + " Percent " + str(self.percent)
        return dataString
