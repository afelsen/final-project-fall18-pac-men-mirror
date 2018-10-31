import math
import Pacman
import Powerup
import Ghost
import Screen


def main():
        print("######## Testing Pacman Model Positive Speed #########")
        test_pacman1 = Pacman.Pacman("test",0,0,1);

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
        test_pacman2 = Pacman.Pacman("test", 2,2,-2);

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
        test_cherry = Powerup.Cherry("test",5,10);
        test_banana = Powerup.Banana("test",10,10);
        test_snowflake = Powerup.Snowflake("test",5,13);
        test_powerpellet = Powerup.Powerpellet("test",2,14);

        print("=====Powerup Position Test=====")
        assert  test_cherry.getCoordinates() == (5, 10)
        assert  test_banana.getCoordinates() == (10, 10)
        assert  test_snowflake.getCoordinates() == (5, 13)
        assert  test_powerpellet.getCoordinates() == (2, 14)


        print("######## Testing Ghost Models #########")
        test_pinky = Ghost.Pinky("test", 0,0,10);
        test_inky = Ghost.Inky("test", 0,0,0);
        test_blinky = Ghost.Blinky("test", 0,0,-5);
        test_clyde = Ghost.Clyde("test", 10,10,-3);

        print("=====30 degree test=====")
        test_pinky.move(30)
        test_inky.move(30)
        test_blinky.move(30)
        test_clyde.move(30)

        assert  test_pinky.getCoordinates() == (10*math.cos(math.radians(30)), 10*math.sin(math.radians(30)))
        assert  test_inky.getCoordinates() == (0*math.cos(math.radians(30)), 0*math.sin(math.radians(30)))
        assert  test_blinky.getCoordinates() == (0, 0)
        assert  test_clyde.getCoordinates() == (10+(-3)*math.cos(math.radians(30)), 10+(-3)*math.sin(math.radians(30)))

        print("=====0 degree test=====")
        test_pinky = Ghost.Pinky("test", 0,0,10);
        test_inky = Ghost.Inky("test", 0,0,0);
        test_blinky = Ghost.Blinky("test", 0,0,-5);
        test_clyde = Ghost.Clyde("test", 10,10,-3);

        test_pinky.move(0)
        test_inky.move(0)
        test_blinky.move(0)
        test_clyde.move(0)

        assert  test_pinky.getCoordinates() == (10*math.cos(math.radians(0)), 10*math.sin(math.radians(0)))
        assert  test_inky.getCoordinates() == (0*math.cos(math.radians(0)), 0*math.sin(math.radians(0)))
        assert  test_blinky.getCoordinates() == (0, 0)
        assert  test_clyde.getCoordinates() == (10+(-3)*math.cos(math.radians(0)), 10+(-3)*math.sin(math.radians(0)))

        print("=====380 degree test=====")
        test_pinky = Ghost.Pinky("test", 0,0,10);
        test_inky = Ghost.Inky("test", 0,0,0);
        test_blinky = Ghost.Blinky("test", 0,0,-5);
        test_clyde = Ghost.Clyde("test", 10,10,-3);

        test_pinky.move(380)
        test_inky.move(380)
        test_blinky.move(380)
        test_clyde.move(380)

        assert  test_pinky.getCoordinates() == (10*math.cos(math.radians(20)), 10*math.sin(math.radians(20)))
        assert  test_inky.getCoordinates() == (0*math.cos(math.radians(20)), 0*math.sin(math.radians(20)))
        assert  test_blinky.getCoordinates() == (0, 0)
        assert  test_clyde.getCoordinates() == (10+(-3)*math.cos(math.radians(20)), 10+(-3)*math.sin(math.radians(20)))

        print("=====Negative 200 degree test=====")
        test_pinky = Ghost.Pinky("test", 0,0,10);
        test_inky = Ghost.Inky("test", 0,0,0);
        test_blinky = Ghost.Blinky("test", 0,0,-5);
        test_clyde = Ghost.Clyde("test", 10,10,-3);

        test_pinky.move(-200)
        test_inky.move(-200)
        test_blinky.move(-200)
        test_clyde.move(-200)

        assert  test_pinky.getCoordinates() == (0, 0)
        assert  test_inky.getCoordinates() == (0*math.cos(math.radians(160)), 0*math.sin(math.radians(160)))
        assert  test_blinky.getCoordinates() == (0, 0)
        assert  test_clyde.getCoordinates() == (10+(-3)*math.cos(math.radians(160)), 10+(-3)*math.sin(math.radians(160)))

        print("######## Testing Screen Model #########")
        test_screen = Screen.Screen(5,7);

        print("=====Screen Input Test=====")
        assert test_screen.getMatrix() == [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

main()
