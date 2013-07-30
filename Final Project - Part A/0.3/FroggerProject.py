'''Author: Jesse Higgins
   Last Modified By: Jesse Higgins
   Date Last Modified: July 30th 2013


Program Description: Leapy is a fun little frogger game with unique
                     levels and requires you to collect all the objects
                     in that level in order to move on to the next.

version 0.3: - scoreboard implementation
             - a game over screen has been added as well

'''

import pygame, mainmenu, level1, gameOver
pygame.init()
pygame.mixer.init()



if __name__ == "__main__":
    
    level = mainmenu.mainmenu()
    donePlaying = False
    
    while donePlaying == False:
        while level > 0:
            
            if level == 1:    
                level = level1.main()

            


        level, donePlaying = gameOver.main()


        
