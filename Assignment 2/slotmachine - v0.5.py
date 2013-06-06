# Source File Name: slotmachine - v0.5.py
# Author's Name: Jesse Higgins
# Last Modified By: Jesse Higgins
# Date Last Modified: Thursday June 6th, 2013

"""Program Description: This program simulates a Caisno-Style Slot Machine.
It provides the User with an interactive GUI representing a slot machine
with Buttons and Labels. This is created using Pygame.

Version: 0.5 - *added images for the slot reels
             - *new class for these images

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
    def __init__(self, x, y, text, size):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", size)
        self.text = text
        self.center = (x,y)
                
    def update(self):
        self.image = self.font.render(self.text, 1, (0,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.center

    def changeLocation(self, x, y):
        self.center = (x, y)


class ReelImage(pygame.sprite.Sprite):
    def __init__(self, x, y, imageName):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageName)
        self.image = self.image.convert()
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.center = (x,y)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.center

    def changeImage(self, imageName):
        self.image = pygame.image.load(imageName)
 

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

    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 5
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    cashWin = 0

    
    #initialize pygame
    pygame.init()
    #create a background image for the slot machine
    bgImage = pygame.image.load('slotmachine.jpg')
    
    #initialize screen
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption('Slot Machine')

    #label to display mouse coordinates
    labelEvent = Label(220, 200, "", 72)

    #create labels to display Bet, Money and Cash Prize
    labelMoney = Label(40,425, str(Player_Money),72)
    labelBet = Label(300, 425, str(Bet), 72)
    labelCashWin = Label(430, 425, str(cashWin), 72)
    labelNoMoney = Label(-200, -200, "Not Enough Money!", 35)
    
    #create instance of spin button and position it
    spinButton = Button(526, 548, 'spinButton1.png')
    betOneButton = Button(167, 565, 'betButton1.png')
    maxBetButton = Button(295, 565, 'maxBetButton1.png')
    cashOutButton = Button(40, 570, 'cashOutButton1.png')
    resetButton = Button(425, 605, 'resetButton1.png')

    reel = ReelImage(45,115, 'blank.png')
    reel2 = ReelImage(258,115, 'blank.png')
    reel3 = ReelImage(470,115, 'blank.png')

    #group sprites together
    allSprites = pygame.sprite.Group(reel,reel2,reel3,labelNoMoney, labelMoney, labelBet, labelCashWin, labelEvent, spinButton, betOneButton, maxBetButton, cashOutButton, resetButton)

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
 #               labelEvent.text = "mouse: (%d, %d)" % (mouseX, mouseY)

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
                    cashWin = 0
                    labelCashWin.text = str(cashWin)
                    labelNoMoney.text = "Not Enough Money!"
                    labelNoMoney.changeLocation(-200,-200)
                    
                    # User Input
                    Prompt = labelBet.text
                    if Prompt  == "q" or Prompt  == "Q":
                        KeepGoing = False
                        break
                    
                    if Prompt == "" and Turn >1:
                        Bet = Prev_Bet
                        print("Using Previous Bet")
                        if Bet > Player_Money:
                            labelNoMoney.changeLocation(240, 350)
                            
                        elif Bet <= Player_Money:
                            Turn +=1
                            Prev_Bet = Bet
                            Player_Money, Jack_Pot, win, cashWin = pullthehandle(Bet, Player_Money, Jack_Pot, cashWin, reel, reel2, reel3)
                            
                            labelMoney.text = str(Player_Money)
                            labelCashWin.text = str(cashWin)
                            if win:
                                labelNoMoney.text = "YOU WON!"
                                labelNoMoney.changeLocation(275,350)
                               
                    elif is_number(Prompt ):
                        Bet = int(Prompt )
                        # not enough money
                        if Bet > Player_Money:
                           labelNoMoney.changeLocation(240, 350)
                            
                        # Let's Play
                        elif Bet <= Player_Money:
                            Turn +=1
                            Prev_Bet = Bet
                            Player_Money, Jack_Pot, win, cashWin = pullthehandle(Bet, Player_Money, Jack_Pot, cashWin, reel, reel2, reel3)

                            labelMoney.text = str(Player_Money)
                            labelCashWin.text = str(cashWin)
                            if win:
                                labelNoMoney.text = "YOU WON!!"
                                labelNoMoney.changeLocation(275, 350)

                if betOneButton_x < mouseX < betOneButton_x + betOneButton_width and betOneButton_y < mouseY < betOneButton_y + spinButton_height:
                    betOneButton.hover('betButton2.png')
                    if Bet != 100:
                        Bet += 5
                        labelBet.text = str(Bet)
                    else:
                        Bet = 5
                        labelBet.text = str(Bet)

                if maxBetButton_x < mouseX < maxBetButton_x + maxBetButton_width and maxBetButton_y < mouseY < maxBetButton_y + maxBetButton_height:
                    maxBetButton.hover('maxBetButton2.png')
                    if Bet!= 100:
                        Bet = 100
                        labelBet.text = str(Bet)

                if cashOutButton_x < mouseX < cashOutButton_x + cashOutButton_width and cashOutButton_y < mouseY < cashOutButton_y + cashOutButton_height:
                    cashOutButton.hover('cashOutButton2.png')
                    pygame.quit()
                    sys.exit()

                if resetButton_x < mouseX < resetButton_x + resetButton_width and resetButton_y < mouseY < resetButton_y + resetButton_height:
                    resetButton.hover('resetButton2.png')

                    Player_Money = 1000
                    Jack_Pot = 500
                    Turn = 1
                    Bet = 5
                    Prev_Bet=0
                    win_number = 0
                    loss_number = 0
                    cashWin = 0

                    labelMoney.text = str(Player_Money)
                    labelBet.text = str(Bet)
                    labelCashWin.text = str(cashWin)
                    labelNoMoney.text = "Not Enough Money!"
                    labelNoMoney.changeLocation(-200,-200)

                    reel.changeImage("blank.png")
                    reel2.changeImage("blank.png")
                    reel3.changeImage("blank.png")
                    

        #blit the screen
        screen.blit(bgImage, (0, 0))
        
        allSprites.clear(screen, bgImage)
        allSprites.update()
        allSprites.draw(screen)
        
        #update the entire display
        pygame.display.flip()

        win = 0
        # Give the player some money if he goes broke
        if Player_Money <1:
            Player_Money = 500
            labelMoney.text = str(Player_Money)
            labelNoMoney.text = "No More Money. Here is $500"
            labelNoMoney.changeLocation(175,350)


def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Grapes"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Banana"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Orange"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Cherry"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Bar"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Bell"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Seven"    

    
    return Bet_Line

def is_number(Bet):
    """ This function Checks if the Bet entered by the user is a valid number """
    try:
        int(Bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False

def pullthehandle(Bet, Player_Money, Jack_Pot, cashWin, reel, reel2, reel3):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
 
    
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    Fruit_Reel = Reels()
    Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]
    
    # Match 3
    if Fruit_Reel.count("Grapes") == 3:
        winnings,win = Bet*20,True
    elif Fruit_Reel.count("Banana") == 3:
        winnings,win = Bet*30,True
    elif Fruit_Reel.count("Orange") == 3:
        winnings,win = Bet*40,True
    elif Fruit_Reel.count("Cherry") == 3:
        winnings,win = Bet*100,True
    elif Fruit_Reel.count("Bar") == 3:
        winnings,win = Bet*200,True
    elif Fruit_Reel.count("Bell") == 3:
        winnings,win = Bet*300,True
    elif Fruit_Reel.count("Seven") == 3:
        print("Lucky Seven!!!")
        winnings,win = Bet*1000,True
    # Match 2
    elif Fruit_Reel.count("Blank") == 0:
        if Fruit_Reel.count("Grapes") == 2:
            winnings,win = Bet*2,True
        if Fruit_Reel.count("Banana") == 2:
            winnings,win = Bet*2,True
        elif Fruit_Reel.count("Orange") == 2:
            winnings,win = Bet*3,True
        elif Fruit_Reel.count("Cherry") == 2:
            winnings,win = Bet*4,True
        elif Fruit_Reel.count("Bar") == 2:
            winnings,win = Bet*5,True
        elif Fruit_Reel.count("Bell") == 2:
            winnings,win = Bet*10,True
        elif Fruit_Reel.count("Seven") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("Seven") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")        
        Player_Money += int(winnings)
        cashWin = winnings
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            cashWin = Jack_Pot + winnings
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(Fruits + "\nPlease try again. \n")

    loadFruitImages(Fruit_Reel[0], Fruit_Reel[1], Fruit_Reel[2], reel, reel2, reel3)
    
    
    return Player_Money, Jack_Pot, win, cashWin

def loadFruitImages(Fruit_Reel1, Fruit_Reel2, Fruit_Reel3, reel, reel2, reel3):

    print Fruit_Reel1, Fruit_Reel2, Fruit_Reel3
#### FRUIT REEL #1 IMAGES
    if Fruit_Reel1 == "Blank":
        reel.changeImage('blank.png')
        
    elif Fruit_Reel1 == "Grapes":
        reel.changeImage('grapes.png')
        
    elif Fruit_Reel1 == "Banana":
        reel.changeImage('banana.png')
        
    elif Fruit_Reel1 == "Orange":
        reel.changeImage('orange.png')
        
    elif Fruit_Reel1 == "Cherry":
        reel.changeImage('cherry.png')
        
    elif Fruit_Reel1 == "Bar":
        reel.changeImage('goldenbar.png')
        
    elif Fruit_Reel1 == "Bell":
        reel.changeImage('bell.png')
        
    elif Fruit_Reel1 == "Seven":
        reel.changeImage('seven.png')

        
###FRUIT REEL # 2 IMAGES
    if Fruit_Reel2 == "Blank":
        reel2.changeImage('blank.png')
        
    elif Fruit_Reel2 == "Grapes":
        reel2.changeImage('grapes.png')
        
    elif Fruit_Reel2 == "Banana":
        reel2.changeImage('banana.png')
        
    elif Fruit_Reel2 == "Orange":
        reel2.changeImage('orange.png')
        
    elif Fruit_Reel2 == "Cherry":
        reel2.changeImage('cherry.png')
        
    elif Fruit_Reel2 == "Bar":
        reel2.changeImage('goldenbar.png')
        
    elif Fruit_Reel2 == "Bell":
        reel2.changeImage('bell.png')
        
    elif Fruit_Reel2 == "Seven":
        reel2.changeImage('seven.png')

###FRUIT REEL # 3 IMAGES
    if Fruit_Reel3 == "Blank":
        reel3.changeImage('blank.png')
        
    elif Fruit_Reel3 == "Grapes":
        reel3.changeImage('grapes.png')
        
    elif Fruit_Reel3 == "Banana":
        reel3.changeImage('banana.png')
        
    elif Fruit_Reel3 == "Orange":
        reel3.changeImage('orange.png')
        
    elif Fruit_Reel3 == "Cherry":
        reel3.changeImage('cherry.png')
        
    elif Fruit_Reel3 == "Bar":
        reel3.changeImage('goldenbar.png')
        
    elif Fruit_Reel3 == "Bell":
        reel3.changeImage('bell.png')
        
    elif Fruit_Reel3 == "Seven":
        reel3.changeImage('seven.png')


if __name__ == "__main__": main()
