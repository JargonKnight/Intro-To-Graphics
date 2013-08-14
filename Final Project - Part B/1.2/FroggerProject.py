'''Author: Jesse Higgins
   Last Modified By: Jesse Higgins
   Date Last Modified: August 13th 2013


Program Description: Leapy is a fun little frogger game with unique
                     levels and requires you to collect all the objects
                     in that level in order to move on to the next.

version 1.2: - First Boss Battle Implementation in progress
             - Splash Screen Implementation

'''

import pygame, mainmenu, level1, level2, level3, level4, gameOver, win, splashscreen
pygame.init()
pygame.mixer.init()


if __name__ == "__main__":
    
 
    donePlaying = False
    
    while donePlaying == False:
        level = splashscreen.main()
        while level >= 0:
            if level == 0:
                level = mainmenu.mainmenu()
            
            if level == 1:    
                level = level1.main()

            if level == 2:
                level = level2.main()

            if level == 3:
                level = level3.main()

            if level == 4:
                level = level4.main()

        if level == -1:
            level, donePlaying = gameOver.main()
            
        if level == -2:
            level, donePlaying = win.main()


        
