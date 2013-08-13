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

#a cursor class so the menu screen isnt so boring   
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image = pygame.image.load("MainMenu/MouseCursor.gif")
        self.rect = self.image.get_rect()
               
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


def mainmenu():
    
    pygame.display.set_caption("Leapy")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0,0))

    #create instances of the menu with titels and images
    #for a friendly interface
    gametitle = Design("MainMenu/FroggerAdventures.gif", 500, 50)
    picture = Design("MainMenu/FROGGER.gif", 175,340)
    start = Design("MainMenu/FroggerStart.gif", 500, 300)
    instructions = Design("MainMenu/FroggerInstructions.gif", 500, 400)
    leaf = Design("MainMenu/FroggerLeaf.gif", 800, 200)
    cursor = Cursor()

    #group all the sprites
    allSprites = pygame.sprite.Group(gametitle, picture, start, instructions, leaf)
    allCursors = pygame.sprite.Group(cursor)
    
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True
    level = 0
    MenuTune = pygame.mixer.Sound("MainMenu/SonicMusicForFrogger.ogg")
    MenuTune.play()

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            #if the user clicks and the cursor is colliding with the start
            #button, then we stop the menu tune and exit the loop
            #causing the level value returned to the project file
            #in which the loop will then fire the first level
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.rect.colliderect(start.rect):
                    MenuTune.stop()
                    level = 4
                    keepGoing = False
                 
            if cursor.rect.colliderect(start.rect):
                start.image = pygame.image.load("MainMenu/FroggerStart2.gif")
            
            else:
                start.image = pygame.image.load("MainMenu/FroggerStart.gif")
                
            if cursor.rect.colliderect(instructions.rect):
                instructions.image = pygame.image.load("MainMenu/FroggerInstructions2.gif")
                
            else:
                instructions.image = pygame.image.load("MainMenu/FroggerInstructions.gif")
            
        
                    
                
        allSprites.clear(screen, background)
        allCursors.clear(screen, background)
        allCursors.update()
        allSprites.draw(screen)
        allCursors.draw(screen)
        
        
        pygame.display.flip()
        
    return level
