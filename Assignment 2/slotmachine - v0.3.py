# Source File Name: slotmachine - v0.3.py
# Author's Name: Jesse Higgins
# Last Modified By: Jesse Higgins
# Date Last Modified: Tuesday June 4th, 2013

"""Program Description: This program simulates a Caisno-Style Slot Machine.
It provides the User with an interactive GUI representing a slot machine
with Buttons and Labels. This is created using Pygame.

Version: 0.3 - *Implementing multiple buttons onto interface
             - *Buttons will all have a hover, original and click method to display
                different images to show interaction
             - *Button class will be dynamic. In the sense that you can
                create the instance and give a name for the button to load
                rather than creating multiple classes for multiple buttons
             - *Keeping the mouse position tracker for location assistance
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

    def __init__(self, x, y, buttonName):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(buttonName)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.center = (x,y)
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.center

    #return width of button
    def getWidth(self):
        return self.rect.width

    #return height of button
    def getHeight(self):
        return self.rect.height

    #methods for changing images
    #they do not need their own methods
    #it can be done in 1
    #i used named methods so i knew which images to use
    def hover(self, buttonName):
        self.image = pygame.image.load(buttonName)

    def original(self, buttonName):
        self.image = pygame.image.load(buttonName)

    def click(self, buttonName):
        self.image = pygame.image.load(buttonName)

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
    spinButton = Button(526, 548, 'spinButton1.png')
    betOneButton = Button(167, 565, 'betButton1.png')
    maxBetButton = Button(295, 565, 'maxBetButton1.png')
    cashOutButton = Button(40, 570, 'cashOutButton1.png')
    resetButton = Button(425, 605, 'resetButton1.png')

    #group sprites together
    allSprites = pygame.sprite.Group(labelEvent, spinButton, betOneButton, maxBetButton, cashOutButton, resetButton)

    #SPIN BUTTON ATTRIBUTES - COLLISION DETECTION
    spinButton_x = spinButton.rect.x
    spinButton_y = spinButton.rect.y
    spinButton_width = spinButton.getWidth()
    spinButton_height = spinButton.getHeight()

    #BET ONE BUTTON ATTRIBUTES - COLLISION DETECTION
    betOneButton_x = betOneButton.rect.x
    betOneButton_y = betOneButton.rect.y
    betOneButton_width = betOneButton.getWidth()
    betOneButton_height = betOneButton.getHeight()

    #MAX BET BUTTON ATTRIBUTES - COLLISION DETECTION
    maxBetButton_x = maxBetButton.rect.x
    maxBetButton_y = maxBetButton.rect.y
    maxBetButton_width = maxBetButton.getWidth()
    maxBetButton_height = maxBetButton.getHeight()

    #CASH OUT BUTTON ATTRIBUTES - COLLISION DETECTION
    cashOutButton_x = cashOutButton.rect.x
    cashOutButton_y = cashOutButton.rect.y
    cashOutButton_width = cashOutButton.getWidth()
    cashOutButton_height = cashOutButton.getHeight()

    #RESET BUTTON ATTRIBUTES - COLLISION DETECTION
    resetButton_x = resetButton.rect.x
    resetButton_y = resetButton.rect.y
    resetButton_width = resetButton.getWidth()
    resetButton_height = resetButton.getHeight()

    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #check for mouse motions
            elif event.type == pygame.MOUSEMOTION:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                #display mouse position
                labelEvent.text = "mouse: (%d, %d)" % (mouseX, mouseY)

                #checking mouse position in relation to
                #the images so we can load other images
                #to display a hover and click effect
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.hover('spinButton2.png')
                else:
                    spinButton.original('spinButton1.png')

                if betOneButton_x < mouseX < betOneButton_x + betOneButton_width and betOneButton_y < mouseY < betOneButton_y + betOneButton_height:
                    betOneButton.hover('betButton2.png')
                else:
                    betOneButton.original('betButton1.png')

                if maxBetButton_x < mouseX < maxBetButton_x + maxBetButton_width and maxBetButton_y < mouseY < maxBetButton_y + maxBetButton_height:
                    maxBetButton.hover('maxBetButton2.png')
                else:
                    maxBetButton.original('maxBetButton1.png')

                if cashOutButton_x < mouseX < cashOutButton_x + cashOutButton_width and cashOutButton_y < mouseY < cashOutButton_y + cashOutButton_height:
                    cashOutButton.hover('cashOutButton2.png')
                else:
                    cashOutButton.original('cashOutButton1.png')

                if resetButton_x < mouseX < resetButton_x + resetButton_width and resetButton_y < mouseY < resetButton_y + resetButton_height:
                    resetButton.hover('resetButton2.png')
                else:
                    resetButton.original('resetButton1.png')


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.click('spinButton3.png')
                else:
                    spinButton.original('spinButton1.png')

                if betOneButton_x < mouseX < betOneButton_x + betOneButton_width and betOneButton_y < mouseY < betOneButton_y + spinButton_height:
                    betOneButton.click('betButton3.png')
                else:
                    betOneButton.original('betButton1.png')

                if maxBetButton_x < mouseX < maxBetButton_x + maxBetButton_width and maxBetButton_y < mouseY < maxBetButton_y + maxBetButton_height:
                    maxBetButton.click('maxBetButton3.png')
                else:
                    maxBetButton.original('maxBetButton1.png')

                if cashOutButton_x < mouseX < cashOutButton_x + cashOutButton_width and cashOutButton_y < mouseY < cashOutButton_y + cashOutButton_height:
                    cashOutButton.click('cashOutButton3.png')
                else:
                    cashOutButton.original('cashOutButton1.png')

                if resetButton_x < mouseX < resetButton_x + resetButton_width and resetButton_y < mouseY < resetButton_y + resetButton_height:
                    resetButton.click('resetButton3.png')
                else:
                    resetButton.original('resetButton1.png')

            elif event.type == pygame.MOUSEBUTTONUP:
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.hover('spinButton2.png')

                if betOneButton_x < mouseX < betOneButton_x + betOneButton_width and betOneButton_y < mouseY < betOneButton_y + spinButton_height:
                    betOneButton.hover('betButton2.png')

                if maxBetButton_x < mouseX < maxBetButton_x + maxBetButton_width and maxBetButton_y < mouseY < maxBetButton_y + maxBetButton_height:
                    maxBetButton.hover('maxBetButton2.png')

                if cashOutButton_x < mouseX < cashOutButton_x + cashOutButton_width and cashOutButton_y < mouseY < cashOutButton_y + cashOutButton_height:
                    cashOutButton.hover('cashOutButton2.png')

                if resetButton_x < mouseX < resetButton_x + resetButton_width and resetButton_y < mouseY < resetButton_y + resetButton_height:
                    resetButton.hover('resetButton2.png')

        #blit the screen
        screen.blit(bgImage, (0, 0))
        
        allSprites.clear(screen, bgImage)
        allSprites.update()
        allSprites.draw(screen)
        
        #update the entire display
        pygame.display.flip()
            

if __name__ == "__main__": main()
