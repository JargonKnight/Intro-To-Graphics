'''Author: Jesse Higgins
   Last Modified By: Jesse Higgins
   Date Last Modified: July 25th 2013


Program Description: Leapy is a fun little frogger game with unique
                     levels and requires you to collect all the objects
                     in that level in order to move on to the next.

version 0.2: - added movement to frogger including boundaries on the game screen
             - sound implementation for collisions has been included
             - collision detection included

'''

import pygame, mainmenu, level1
pygame.init()
pygame.mixer.init()



if __name__ == "__main__":
    
    level = mainmenu.mainmenu()
    
    if level == 1:
        level1.main()


        
