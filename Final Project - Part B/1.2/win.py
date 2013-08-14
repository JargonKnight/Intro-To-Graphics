'''Author: Jesse Higgins
   Last Modified By: Jesse Higgins
   Date Last Modified: July 30th 2013


Program Description: Leapy is a fun little frogger game with unique
                     levels and requires you to collect all the objects
                     in that level in order to move on to the next.

'''
import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 640))


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
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    gametitle = Design("MainMenu/FroggerAdventures.gif", 500, 50)
    picture = Design("MainMenu/FROGGER.gif", 175,340)
    leaf = Design("MainMenu/FroggerLeaf.gif", 800, 200) 

    allSprites = pygame.sprite.Group(gametitle, picture, leaf)

    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "                                           YOU WON!!",
    "",
    "                                     Click to Play Again!"
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0,255,0))
        insLabels.append(tempLabel)

    for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

    allSprites.clear(screen, background)
    allSprites.draw(screen)

    pygame.display.flip()

    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
                level = 0
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
    pygame.mouse.set_visible(True)

    return level, donePlaying
