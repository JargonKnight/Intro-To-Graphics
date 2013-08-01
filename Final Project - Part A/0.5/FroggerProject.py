'''Author: Jesse Higgins
   Last Modified By: Jesse Higgins
   Date Last Modified: July 31st 2013


Program Description: Leapy is a fun little frogger game with unique
                     levels and requires you to collect all the objects
                     in that level in order to move on to the next.

version 0.5: - level 3 implementation

'''

import pygame, mainmenu, level1, level2, level3, gameOver
pygame.init()
pygame.mixer.init()



if __name__ == "__main__":
    
 
    donePlaying = False
    
    while donePlaying == False:
        level = mainmenu.mainmenu()
        while level >= 0:
            if level == 0:
                level = mainmenu.mainmenu()
            
            if level == 1:    
                level = level1.main()

            if level == 2:
                level = level2.main()

            if level == 3:
                level = level3.main()


        level, donePlaying = gameOver.main()


        
