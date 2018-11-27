class bottomBar:
  self.progress = 2
  self.level = 2
  self.highScore = 2
  self.score = 2
  menubarLives = self.barfont.render("Lives:",False,(255,255,50))
  menubarLivesInt = self.barfont.render(str(self.pacman.lives),False,(255,255,255))
  menubarLevel = self.barfont.render("Level:",False,(255,255,50))
  menubarLevelInt = self.barfont.render(str(level),False,(255,255,255))
  menubarScore = self.barfont.render("Score:",False,(255,255,50))
  menubarScoreInt = self.barfont.render(str(score),False,(255,255,255))
  menubarHighscore = self.barfont.render("HighScore:",False,(255,255,50))
  menubarHighscoreInt = self.barfont.render(str(highScore),False,(255,255,255))
  menubarPercent = self.barfont.render("Progress:",False,(255,255,50))
  menubarPercentOut = self.barfont.render("/80%",False,(255,255,50))
  menubarPercentInt = self.barfont.render(str(progress),False,(255,255,255))
  self.screen.blit(self.background,(0,0))
  self.screen.blit(menubarLives,(0,475))
  self.screen.blit(menubarLivesInt,(65,475))
  self.screen.blit(menubarScore,(85,475))
  self.screen.blit(menubarScoreInt,(168,475))
  self.screen.blit(menubarHighscore,(190,475))
  self.screen.blit(menubarHighscoreInt,(327,475))
  self.screen.blit(menubarPercent,(435,475))
  self.screen.blit(menubarPercentOut,(565,475))
  self.screen.blit(menubarPercentInt,(547,475))
  self.screen.blit(menubarLevel,(345,475))
  self.screen.blit(menubarLevelInt,(415,475))
