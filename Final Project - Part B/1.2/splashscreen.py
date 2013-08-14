#this is the mainmenu file
import pygame, sys
pygame.init()
pygame.mixer.init()

#initialize the screen
screen = pygame.display.set_mode((1000, 640))

#create a class for random design instances
#a picture, and an x and y position will be needed for where you want it
#placed on the screen
class Design(pygame.sprite.Sprite):
    def __init__(self, pic, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = pygame.image.load(pic)
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy

def main():
    
    pygame.display.set_caption("Leapy")

    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("Resources/splashscreenBG.jpg")
    screen.blit(background, (0,0))

    #create instances of the menu with titels and images
    #for a friendly interface
    gametitle = Design("MainMenu/FroggerAdventures.png", 500, 100)
    picture = Design("Resources/splashscreenLogo.png", 500,340)
 

    #group all the sprites
    allSprites = pygame.sprite.Group(gametitle, picture)
    
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True
    level = 0
    MenuTune = pygame.mixer.Sound("MainMenu/SonicMusicForFrogger.ogg")
    MenuTune.play()

    counter = 0

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            
        counter += 1

        if counter > 100:
            MenuTune.stop()
            level = 0
            keepGoing = False
                    
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        
        
        pygame.display.flip()
        
    return level
