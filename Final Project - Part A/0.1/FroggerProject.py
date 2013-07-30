

import pygame, mainmenu, level1
pygame.init()
pygame.mixer.init()



if __name__ == "__main__":
    
    level = mainmenu.mainmenu()
    
    if level == 1:
        level1.main()


        
