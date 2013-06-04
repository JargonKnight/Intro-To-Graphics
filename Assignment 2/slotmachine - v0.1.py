# Source File Name: slotmachine - v0.1.py
# Author's Name: Jesse Higgins
# Last Modified By: Jesse Higgins
# Date Last Modified: Tuesday June 4th, 2013

"""Program Description: This program simulates a Caisno-Style Slot Machine.
It provides the User with an interactive GUI representing a slot machine
with Buttons and Labels. This is created using Pygame.

Version: 0.1 - *Beginning with creating the background image to
                represent the slot machine.

"""

#import statements
import random
import pygame, sys
from pygame.locals import *


def main():

    #initialize pygame
    pygame.init()
    #create a background image for the slot machine
    bgImage = pygame.image.load('slotmachine-bg.jpg')

    #initialize screen
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption('Slot Machine')


    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #blit the screen
        screen.blit(bgImage, (0, 0))
        #update the entire display
        pygame.display.flip()

    

    
            

if __name__ == "__main__": main()
