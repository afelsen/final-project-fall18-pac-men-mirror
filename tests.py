import math
from src import Pacman
from src import Powerup
from src import Ghost
from src import Screen
from src import BottomBar
import pygame


def main():
        print("######## Testing Pacman Model Positive Speed #########")
        test_pacman1 = Pacman.Pacman("assets/PacmanOpen.png",0,0,1);

        print("=====Right Input Test=====")
        test_pacman1.moveRight()
        assert  test_pacman1.getCoordinates() == (1, 0)
        print("=====Left Input Test=====")
        test_pacman1.moveLeft()
        assert  test_pacman1.getCoordinates() == (0, 0)
        print("=====Up Input Test=====")
        test_pacman1.moveUp()
        assert  test_pacman1.getCoordinates() == (0, 0)
        print("=====Down Input Test=====")
        test_pacman1.moveDown()
        assert  test_pacman1.getCoordinates() == (0, 1)

        print("######## Testing Pacman Model Negative Speed #########")
        test_pacman2 = Pacman.Pacman("assets/PacmanOpen.png", 2,2,-2);

        print("=====Right Input Test=====")
        test_pacman2.moveRight()
        assert  test_pacman2.getCoordinates() == (0, 2)
        print("=====Left Input Test=====")
        test_pacman2.moveLeft()
        assert  test_pacman2.getCoordinates() == (2, 2)
        print("=====Up Input Test=====")
        test_pacman2.moveUp()
        assert  test_pacman2.getCoordinates() == (2, 4)
        print("=====Down Input Test=====")
        test_pacman2.moveDown()
        assert  test_pacman2.getCoordinates() == (2, 2)

        print("######## Testing Powerups #########")
        test_cherry = Powerup.Cherry("assets/PacmanOpen.png",5,10);
        test_banana = Powerup.Banana("assets/PacmanOpen.png",10,10);
        test_snowflake = Powerup.Snowflake("assets/PacmanOpen.png",5,13);
        test_heart = Powerup.Heart("assets/PacmanOpen.png",2,14);

        print("=====Powerup Position Test=====")
        assert  test_cherry.getCoordinates() == (5, 10)
        assert  test_banana.getCoordinates() == (10, 10)
        assert  test_snowflake.getCoordinates() == (5, 13)
        assert  test_heart.getCoordinates() == (2, 14)


        print("######## Testing Pinky, Inky and Blinky Ghost Models #########")
        test_pinky = Ghost.Pinky("assets/PacmanOpen.png", 10,10,10);
        test_pinky.xmultiplier = 1
        test_pinky.ymultiplier = -1
        test_inky = Ghost.Inky("assets/PacmanOpen.png", 10,10,20);
        test_inky.xmultiplier = -1
        test_inky.ymultiplier = 1
        test_blinky = Ghost.Blinky("assets/PacmanOpen.png", 20,20,-20);
        test_blinky.xmultiplier = 1
        test_blinky.ymultiplier = 1

        print("=====Update Test=====")
        test_pinky.update()
        test_inky.update()
        test_blinky.update()

        assert  test_pinky.getCoordinates() == (15,5)
        assert  test_inky.getCoordinates() == (0,20)
        assert  test_blinky.getCoordinates() == (10, 10)

        print("######## Testing Clyde Ghost Model #########")
        test_clyde = Ghost.Clyde("assets/PacmanOpen.png", 100,100,20);
        test_clyde.clydeState = 0

        print("=====Update Test=====")
        test_clyde.update()
        assert test_clyde.clydeState == 1
        assert  test_clyde.getCoordinates() == (120,120)

        test_clyde.update()
        assert test_clyde.clydeState == 2
        assert  test_clyde.getCoordinates() == (140,100)

        test_clyde.update()
        assert test_clyde.clydeState == 3
        assert  test_clyde.getCoordinates() == (120,80)

        test_clyde.update()
        assert test_clyde.clydeState == 0
        assert  test_clyde.getCoordinates() == (100,100)


        print("######## Testing Screen Model #########")
        test_screen = Screen.Screen(8,7);
        test_screen.matrix[2][2] = 1
        test_screen.matrix[2][3] = 1
        test_screen.matrix[2][4] = 1
        test_screen.matrix[2][5] = 1

        test_screen.matrix[3][2] = 1
        test_screen.matrix[4][2] = 1
        test_screen.matrix[5][2] = 1

        test_screen.matrix[5][3] = 1
        test_screen.matrix[5][4] = 1
        test_screen.matrix[5][5] = 1

        test_screen.matrix[4][5] = 1
        test_screen.matrix[3][5] = 1

        print("=====Screen Test=====")
        assert test_screen.getMatrix() == [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,1,1],[1,0,1,0,0,1,1],[1,0,1,0,0,1,1],[1,0,1,1,1,1,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]

        print("=====Percent Test=====")
        assert test_screen.getPercent() == int((12/(6*5))*100)

        print("=====Fill Test=====")
        pinkyGroup = pygame.sprite.Group()
        inkyGroup = pygame.sprite.Group()
        blinkyGroup = pygame.sprite.Group()
        clydeGroup = pygame.sprite.Group()
        clydeGroup.add(Ghost.Clyde("assets/PacmanOpen.png", 6*20,2*20,20)) #Puts ghost in 2nd to last row, 2nd (starting from 0) collumn
        ghostGroupList = [pinkyGroup,inkyGroup,blinkyGroup,clydeGroup]
        #The above is because ghostGroupList is a required argument for fillMatrix()
        test_screen.fillMatrix(ghostGroupList)
        assert test_screen.getMatrix() == [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,1,1],[1,0,1,1,1,1,1],[1,0,1,1,1,1,1],[1,0,1,1,1,1,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]

        print("=====Number of Last Filled Test=====")
        assert test_screen.getNumLastFilled() == 4

        print("=====Reset Test=====")
        test_screen.reset()
        assert test_screen.getMatrix() == [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]

        print("=====Track Pacman Test=====")
        test_screen.trackPacman((3,3))
        assert test_screen.getMatrix() == [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,.5,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]


        print("=====Remove Track Test=====")
        test_screen.matrix = [[1,1,1,1,1,1,1],[1,0,.5,0,0,0,1],[1,0,0,0,0,0,1],[1,0,.5,.5,0,.5,1],[1,0,0,0,0,.5,1],[1,0,.5,.5,.5,.5,1],[1,.5,0,.5,0,0,1],[1,1,1,1,1,1,1]]
        test_screen.removeTrack()
        assert test_screen.getMatrix() == [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]


        print("######## Testing Bottombar Model #########")
        print("=====Checking Output=====")
        test_bottombar = BottomBar.Bottombar(0,0,0,0,0)
        test_bottombar.lives = 5
        test_bottombar.level = 15
        test_bottombar.percent = 80
        test_bottombar.highScore = 1000
        test_bottombar.score = 500
        assert test_bottombar.data() == ("Lives: 5 Level: 15 Percent: 80", "High Score: 1000 Score: 500")


main()
