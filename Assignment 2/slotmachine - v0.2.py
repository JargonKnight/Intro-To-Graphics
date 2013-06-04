# Source File Name: slotmachine - v0.2.py
# Author's Name: Jesse Higgins
# Last Modified By: Jesse Higgins
# Date Last Modified: Tuesday June 4th, 2013

"""Program Description: This program simulates a Caisno-Style Slot Machine.
It provides the User with an interactive GUI representing a slot machine
with Buttons and Labels. This is created using Pygame.

Version: 0.2 - *Implementing spin button onto the interface
             - *Button will have a hover, original and click method to display
                different images to show interaction
             - *Adding a mouse position tracker for location assistance
               when displaying buttons etc..

"""

#import statements
import random
import pygame, sys
from pygame.locals import *

class Label(pygame.sprite.Sprite):
    """ Label Class (simplest version) 
        Attributes:
            font: any pygame Font or SysFont objects
            text: text to display
            center: desired position of label center (x, y)
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (320, 240)
                
    def update(self):
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('button1.jpeg')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.center = (x,y)
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.center

    def getWidth(self):
        return self.rect.width
    
    def getHeight(self):
        return self.rect.height

    def hover(self):
        self.image = pygame.image.load('button2.jpeg')

    def original(self):
        self.image = pygame.image.load('button1.jpeg')

    def click(self):
        self.image = pygame.image.load('button3.jpeg')

def main():

    #initialize pygame
    pygame.init()
    #create a background image for the slot machine
    bgImage = pygame.image.load('slotmachine.jpg')
    
    #initialize screen
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption('Slot Machine')

    #label to display mouse coordinates
    labelEvent = Label()
    #create instance of spin button and position it
    spinButton = Button(524, 548)

    #group sprites together
    allSprites = pygame.sprite.Group(labelEvent, spinButton)

    #SPIN BUTTON ATTRIBUTES - COLLISION DETECTION
    spinButton_x = spinButton.rect.x
    spinButton_y = spinButton.rect.y
    spinButton_width = spinButton.getWidth()
    spinButton_height = spinButton.getHeight()

    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                labelEvent.text = "mouse: (%d, %d)" % (mouseX, mouseY)

                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.hover()
                else:
                    spinButton.original()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.click()
                else:
                    spinButton.original()

            elif event.type == pygame.MOUSEBUTTONUP:
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.hover()


        #blit the screen
        screen.blit(bgImage, (0, 0))
        
        allSprites.clear(screen, bgImage)
        allSprites.update()
        allSprites.draw(screen)
        
        #update the entire display
        pygame.display.flip()

    

    
            

if __name__ == "__main__": main()
