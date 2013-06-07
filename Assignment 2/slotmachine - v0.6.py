#Source File Name: slotmachine - v0.6.py
# Author's Name: Jesse Higgins
# Last Modified By: Jesse Higgins
# Date Last Modified: Thursday June 6th, 2013

"""Program Description: This program simulates a Caisno-Style Slot Machine.
It provides the User with an interactive GUI representing a slot machine
with Buttons and Labels. This is created using Pygame.

Version: 0.6 - *sound implementation
             - *added graphics for presentation
             - *fixed up filepaths for images and sounds
             - FINAL VERSION
"""

#import statements
import random
import pygame, sys
from pygame.locals import *

#Label Class used for creating labels and displaying text on the GUI
class Label(pygame.sprite.Sprite):
    
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

#ReelImage class used to display the pictures for the fruits on the reel
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
 
#Button Class used to make a button illusion
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
    Bet = 10
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    cashWin = 0
    counter = 0

    
    #initialize pygame
    pygame.init()
    #initialize pygame mixer for sounds
    pygame.mixer.init()
    
    #create a background image for the slot machine
    bgImage = pygame.image.load('slotmachine.jpg')

    #create background music for the game
    pygame.mixer.music.load("Sounds/bgSlotMusic.ogg")
    #loop the sound file continuously starting at 0.0
    pygame.mixer.music.play(-1,0.0)

    #create array to hold sounds
    sounds = []
    #create the variables and assign them the sounds
    spinSound = pygame.mixer.Sound("Sounds/slotSpinSound.ogg")
    winSound = pygame.mixer.Sound("Sounds/slotWinSound.ogg")
    #add them to the sounds array
    sounds.append(spinSound)
    sounds.append(winSound)
    
    #initialize screen
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption('Slot Machine')

    #create labels to display Bet, Money and Cash Prize
    labelMoney = Label(40,425, str(Player_Money),72)
    labelBet = Label(300, 425, str(Bet), 72)
    labelCashWin = Label(430, 425, str(cashWin), 72)
    labelNoMoney = Label(-200, -200, "Not Enough Money!", 35)
    labelJackpot = Label(255, 75, "Jackpot: " + str(Jack_Pot), 40)
    
    #create instance of spin button and position it
    spinButton = Button(526, 548, 'Buttons/spinButton1.png')
    betOneButton = Button(167, 565, 'Buttons/betButton1.png')
    maxBetButton = Button(295, 565, 'Buttons/maxBetButton1.png')
    cashOutButton = Button(40, 570, 'Buttons/cashOutButton1.png')
    resetButton = Button(425, 605, 'Buttons/resetButton1.png')

    #create a frameImages array to hold all the file names
    frameImages = ['','','','','','','','','','','','','','','','','','','','',
                   '','','','','','','','','','','']

    #add the images to the array
    for i in range (0,31):
        frameImages[i] = pygame.image.load('StarFrame/starFrame-'+str(i)+'.png')

    #create 3 reel images and place them accordingly assigning them
    #the blank image to start
    reel = ReelImage(45,115, 'ReelImages/blank.png')
    reel2 = ReelImage(258,115, 'ReelImages/blank.png')
    reel3 = ReelImage(470,115, 'ReelImages/blank.png')

    #group sprites together
    allSprites = pygame.sprite.Group(reel,reel2,reel3,labelNoMoney,labelJackpot,labelMoney, labelBet, labelCashWin, spinButton, betOneButton, maxBetButton, cashOutButton, resetButton)

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

        #display starFrame images
        starFrame = frameImages[counter]
        #create a counter to display that image in the array
        counter += 1
        #if the counter reaches 30 reset it to start back at the first image
        if counter == 30:
            counter = 0
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #check for mouse motions
            elif event.type == pygame.MOUSEMOTION:
                (mouseX, mouseY) = pygame.mouse.get_pos()

                #checking mouse position in relation to
                #the images so we can load other images
                #to display a hover and click effect
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.hover('Buttons/spinButton2.png')
                else:
                    spinButton.original('Buttons/spinButton1.png')

                if betOneButton_x < mouseX < betOneButton_x + betOneButton_width and betOneButton_y < mouseY < betOneButton_y + betOneButton_height:
                    betOneButton.hover('Buttons/betButton2.png')
                else:
                    betOneButton.original('Buttons/betButton1.png')

                if maxBetButton_x < mouseX < maxBetButton_x + maxBetButton_width and maxBetButton_y < mouseY < maxBetButton_y + maxBetButton_height:
                    maxBetButton.hover('Buttons/maxBetButton2.png')
                else:
                    maxBetButton.original('Buttons/maxBetButton1.png')

                if cashOutButton_x < mouseX < cashOutButton_x + cashOutButton_width and cashOutButton_y < mouseY < cashOutButton_y + cashOutButton_height:
                    cashOutButton.hover('Buttons/cashOutButton2.png')
                else:
                    cashOutButton.original('Buttons/cashOutButton1.png')

                if resetButton_x < mouseX < resetButton_x + resetButton_width and resetButton_y < mouseY < resetButton_y + resetButton_height:
                    resetButton.hover('Buttons/resetButton2.png')
                else:
                    resetButton.original('Buttons/resetButton1.png')


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.click('Buttons/spinButton3.png')
                    
                else:
                    spinButton.original('Buttons/spinButton1.png')

                if betOneButton_x < mouseX < betOneButton_x + betOneButton_width and betOneButton_y < mouseY < betOneButton_y + spinButton_height:
                    betOneButton.click('Buttons/betButton3.png')
                else:
                    betOneButton.original('Buttons/betButton1.png')

                if maxBetButton_x < mouseX < maxBetButton_x + maxBetButton_width and maxBetButton_y < mouseY < maxBetButton_y + maxBetButton_height:
                    maxBetButton.click('Buttons/maxBetButton3.png')
                else:
                    maxBetButton.original('Buttons/maxBetButton1.png')

                if cashOutButton_x < mouseX < cashOutButton_x + cashOutButton_width and cashOutButton_y < mouseY < cashOutButton_y + cashOutButton_height:
                    cashOutButton.click('Buttons/cashOutButton3.png')
                else:
                    cashOutButton.original('Buttons/cashOutButton1.png')

                if resetButton_x < mouseX < resetButton_x + resetButton_width and resetButton_y < mouseY < resetButton_y + resetButton_height:
                    resetButton.click('Buttons/resetButton3.png')
                else:
                    resetButton.original('Buttons/resetButton1.png')

            elif event.type == pygame.MOUSEBUTTONUP:
                #check if mousebutton is up so we can make buttons functional
                if spinButton_x < mouseX < spinButton_x + spinButton_width and spinButton_y < mouseY < spinButton_y + spinButton_height:
                    spinButton.hover('Buttons/spinButton2.png')

                    #stop the sound if its playing so they dont overlap
                    sounds[0].stop()
                    sounds[1].stop()
                    #then play it again
                    sounds[0].play()

                    #adjust labels accordingly
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
                            Player_Money, Jack_Pot, win, cashWin = pullthehandle(Bet, Player_Money, Jack_Pot, cashWin, reel, reel2, reel3, sounds[1],sounds[0])
                            
                            labelMoney.text = str(Player_Money)
                            labelCashWin.text = str(cashWin)
                            labelJackpot.text = "Jackpot: " + str(Jack_Pot)
                            if win:
                                labelNoMoney.text = "YOU WON!"
                                labelNoMoney.changeLocation(275,350)
                               
                    elif is_number(Prompt ):
                        Bet = int(Prompt )
                        # not enough money
                        if Bet > Player_Money:
                           #display the no money label for the user 
                           labelNoMoney.changeLocation(240, 350)
                            
                        # Let's Play
                        elif Bet <= Player_Money:
                            Turn +=1
                            Prev_Bet = Bet
                            #call pullthehandle to take care of determing
                            #if the player wins and calculations
                            Player_Money, Jack_Pot, win, cashWin = pullthehandle(Bet, Player_Money, Jack_Pot, cashWin, reel, reel2, reel3, sounds[1],sounds[0])
                            #display the users money and cashwin if there is any
                            labelMoney.text = str(Player_Money)
                            labelCashWin.text = str(cashWin)
                            labelJackpot.text = "Jackpot: " + str(Jack_Pot)
                            if win:
                                labelNoMoney.text = "YOU WON!!"
                                labelNoMoney.changeLocation(275, 350)
                #checking if coordinates of mouse are on bet button
                if betOneButton_x < mouseX < betOneButton_x + betOneButton_width and betOneButton_y < mouseY < betOneButton_y + spinButton_height:
                    betOneButton.hover('Buttons/betButton2.png')
                    #if bet isnt 100 then increase it by 5
                    if Bet != 100:
                        Bet += 5
                        labelBet.text = str(Bet)
                    else: #once it reaches 100 we reset it back to 5
                        Bet = 10
                        labelBet.text = str(Bet)
                #set bet to 100 if not already when
                #mouse is over the maxbet button
                if maxBetButton_x < mouseX < maxBetButton_x + maxBetButton_width and maxBetButton_y < mouseY < maxBetButton_y + maxBetButton_height:
                    maxBetButton.hover('Buttons/maxBetButton2.png')
                    if Bet!= 100:
                        Bet = 100
                        labelBet.text = str(Bet)
                #we close the program if user cashes out
                if cashOutButton_x < mouseX < cashOutButton_x + cashOutButton_width and cashOutButton_y < mouseY < cashOutButton_y + cashOutButton_height:
                    cashOutButton.hover('Buttons/cashOutButton2.png')
                    pygame.quit()
                    sys.exit()
                #reset all the initial values
                if resetButton_x < mouseX < resetButton_x + resetButton_width and resetButton_y < mouseY < resetButton_y + resetButton_height:
                    resetButton.hover('Buttons/resetButton2.png')

                    Player_Money = 1000
                    Jack_Pot = 500
                    Turn = 1
                    Bet = 10
                    Prev_Bet=0
                    win_number = 0
                    loss_number = 0
                    cashWin = 0

                    labelMoney.text = str(Player_Money)
                    labelBet.text = str(Bet)
                    labelCashWin.text = str(cashWin)
                    labelNoMoney.text = "Not Enough Money!"
                    labelNoMoney.changeLocation(-200,-200)
                    labelJackpot.text = "Jackpot: " + str(Jack_Pot)

                    reel.changeImage("ReelImages/blank.png")
                    reel2.changeImage("ReelImages/blank.png")
                    reel3.changeImage("ReelImages/blank.png")
                    

        #blit the screen
        screen.blit(bgImage, (0, 0))
        screen.blit(starFrame, (-25,-10))
        
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

def pullthehandle(Bet, Player_Money, Jack_Pot, cashWin, reel, reel2, reel3, winSound, spinSound):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
 
    
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    print str(Jack_Pot)
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
        #set cashwin to the amount won
        cashWin = winnings
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        winSound.play()#play winning sound
        spinSound.stop()#stop the spin sound so there is no overlapping
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            cashWin = Jack_Pot + winnings
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n" + str(Jack_Pot))
    # No win
    else:
        print(Fruits + "\nPlease try again. \n")

    #now we pass in the fruits and reel sprites
    #so we can update them from the function
    loadFruitImages(Fruit_Reel[0], Fruit_Reel[1], Fruit_Reel[2], reel, reel2, reel3)
    
    
    return Player_Money, Jack_Pot, win, cashWin

def loadFruitImages(Fruit_Reel1, Fruit_Reel2, Fruit_Reel3, reel, reel2, reel3):

    print Fruit_Reel1, Fruit_Reel2, Fruit_Reel3
#### FRUIT REEL #1 IMAGES
    if Fruit_Reel1 == "Blank":
        reel.changeImage('ReelImages/blank.png')
        
    elif Fruit_Reel1 == "Grapes":
        reel.changeImage('ReelImages/grapes.png')
        
    elif Fruit_Reel1 == "Banana":
        reel.changeImage('ReelImages/banana.png')
        
    elif Fruit_Reel1 == "Orange":
        reel.changeImage('ReelImages/orange.png')
        
    elif Fruit_Reel1 == "Cherry":
        reel.changeImage('ReelImages/cherry.png')
        
    elif Fruit_Reel1 == "Bar":
        reel.changeImage('ReelImages/goldenbar.png')
        
    elif Fruit_Reel1 == "Bell":
        reel.changeImage('ReelImages/bell.png')
        
    elif Fruit_Reel1 == "Seven":
        reel.changeImage('ReelImages/seven.png')

        
###FRUIT REEL # 2 IMAGES
    if Fruit_Reel2 == "Blank":
        reel2.changeImage('ReelImages/blank.png')
        
    elif Fruit_Reel2 == "Grapes":
        reel2.changeImage('ReelImages/grapes.png')
        
    elif Fruit_Reel2 == "Banana":
        reel2.changeImage('ReelImages/banana.png')
        
    elif Fruit_Reel2 == "Orange":
        reel2.changeImage('ReelImages/orange.png')
        
    elif Fruit_Reel2 == "Cherry":
        reel2.changeImage('ReelImages/cherry.png')
        
    elif Fruit_Reel2 == "Bar":
        reel2.changeImage('ReelImages/goldenbar.png')
        
    elif Fruit_Reel2 == "Bell":
        reel2.changeImage('ReelImages/bell.png')
        
    elif Fruit_Reel2 == "Seven":
        reel2.changeImage('ReelImages/seven.png')

###FRUIT REEL # 3 IMAGES
    if Fruit_Reel3 == "Blank":
        reel3.changeImage('ReelImages/blank.png')
        
    elif Fruit_Reel3 == "Grapes":
        reel3.changeImage('ReelImages/grapes.png')
        
    elif Fruit_Reel3 == "Banana":
        reel3.changeImage('ReelImages/banana.png')
        
    elif Fruit_Reel3 == "Orange":
        reel3.changeImage('ReelImages/orange.png')
        
    elif Fruit_Reel3 == "Cherry":
        reel3.changeImage('ReelImages/cherry.png')
        
    elif Fruit_Reel3 == "Bar":
        reel3.changeImage('ReelImages/goldenbar.png')
        
    elif Fruit_Reel3 == "Bell":
        reel3.changeImage('ReelImages/bell.png')
        
    elif Fruit_Reel3 == "Seven":
        reel3.changeImage('ReelImages/seven.png')


if __name__ == "__main__": main()
