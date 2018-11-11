# PacXon
## CS 110 Final Project
### Semester 1, 2018

[https://github.com/binghamtonuniversity-cs110/final-project-fall18-pac-men](https://github.com/binghamtonuniversity-cs110/final-project-fall18-pac-men#)

[Link to demo presentation slides - TBD](#)

### Team:
#### Adiel Felsen, Matt Damiata, Jack Stanley

***

## Project Description
PacXon is a game where a player controls a Pacman character to fence portions of the screen. The challenge is that the Pacman has to avoid ghosts who are bouncing around the screen. If the Pacman hits into a ghost, he loses a life. The game is over when Pacman runs out of lives or fences in a certain percentage of the screen. There are many levels with a different number of ghosts and even ghosts with special abilities to make the game more challenging. Pacman can also collect powerups of his own to help him succeed. PacXon uses Pacman’s original characters – Pacman and ghosts – but it is entirely a unique game of its own.

1. Core
   1. Pacman moves across screen
   2. Pacman fences in parts of the screen
   3. Pacman wins when a certain percent of the screen is fenced in
   4. Ghosts bounce across walls
     * Pacman does not fence in area occupied by ghosts
   6. Pacman loses when his current line is hit by a ghost
2. Features
   1. Pacman image changes direction
   2. Multiple levels
     * More ghosts on later levels
     * Some ghosts move faster in later levels
   3. Powerups
     * Allows Pacman to move faster.
     * Remain unaffected by ghosts for a period of time.
3. Dreams
   1. Multiplayer mode – Pacmen compete or work together
   2. Pacman does not immediately die when his current line is hit – there is a delay based on how far away the ghost is
   3. You can apply different skins for the Pacman and ghosts


***    

## User Interface Design
1.	Start Screen

   TBD
2.	Instructions Screen

   TBD

3.	The Game Menu

   TBD

4.	Next Level Screen

   TBD

5.	Game Over Screen

   TBD

Pictures: TBD

***        

## Program Design

### Non-Standard Libraries and Modules Used
* **Pygame** (https://pygame.org) - A free and Open Source python programming language library for making multimedia applications like games, developed by Pete Shinners and the pygame community.
* TBD

### List of Classes
* **Controller** -
* **Pacman** - A class that defines the Pacman which is the character that the player controls. The character moves in any direction and is able to "fence in" portions of the screen.
* **Pinky** - the pink ghost that Pacman needs to avoid. This ghost bounces off the walls of non-fenced in areas of the screen. If Pinky collides with Pacman or one of the fences he is currently drawing, Pacman loses a life.
* **Inky** - the light-blue ghost that Pacman needs to avoid. This ghost bounces off the walls of fenced in areas of the screen. If Inky collides with Pacman, Pacman loses a life.
* **Binky** - the red ghost that Pacman needs to avoid. This ghost bounces off the walls of the non-fenced in areas of the screen and breaks any block it hits into (excluding the borders). If Blinky collides with Pacman or one of the fences he is currently drawing, Pacman loses a life.
* **Clyde** - the orange ghost that Pacman needs to avoid. This ghost moves along the edge of a fenced in area. If Clyde collides with Pacman, Pacman loses a life.
* **Banana** - one of the powerups that Pacman can collide with. Once collided with, Pacman's speed will double for <some period of time>.
* **Snowflake** - one of the powerups that Pacman can collide with. Once collided with, the speed of the ghosts is set to zero for <some period of time>.
* **Powerpellet** - one of the powerups that Pacman can collide with. Once collided with, Pacman is no longer affected by the ghosts for <some period of time>. During this time, if Pacman collides with a ghost, the ghost's location is reset.
* **Screen** - this class holds the matrix which includes the state of each box on the grid - filled (state = 1), unfilled (state = 0) or in the process of being drawn (state = .5). This class also has a method to fill in areas of the screen not containing a ghost.
* **Box** - this class defines each "box" object of the grid background. This class references the matrix in the Screen class for changing the images of the objects.  
***

## Tasks and Responsibilities

### Software Lead - Adiel Felsen

TBD

### Front End Specialist - Matt Damiata

TBD

### Back End Specialist - Jack Stanley

TBD

***

## Testing

### Menu Testing

TBD

### Game Testing

TBD

**Acceptance Test Procedure**

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | TBD  | TBD  | TBD |
|  2  | TBD  | TBD | TBD |
etc...
