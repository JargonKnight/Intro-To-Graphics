'''Author: Jesse Higgins
   Last Modified By: Jesse Higgins
   Date Last Modified: July 30th 2013


Program Description: Leapy is a fun little frogger game with unique
                     levels and requires you to collect all the objects
                     in that level in order to move on to the next.

version 0.3: - scoreboard implementation

'''
import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 640))


def main():
 
    pygame.display.set_caption("Leapy")

    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))


    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "",
    "",
    "",
    "",
    "                                *!* ~ Leapy ~ *!*",
    "",
    "",
    "",
    "",
    "                                  GAME OVER",
    "",
    "                             Click to Play Again!"
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0,0,255))
        insLabels.append(tempLabel)

    for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

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
                level = 1
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
    pygame.mouse.set_visible(True)

    return level, donePlaying
