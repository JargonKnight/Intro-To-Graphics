''' Author: Jesse Higgins
    Date: May 9th 2013
    Program: Assignment1.py
    Description: A decision making, text-based program that allows the user
                 to have one possible positive outcome
'''
#import libraries for randomizing and pausing lines of text during
#execution of program
import random
import time

#an intro function giving the user background information of the program
def displayIntro():
            print ('You are on a Hunt for treasure. In front of you,')
            print ('you see two caves. However, You are not sure which,')
            print ('cave will bring you to the treasure!')
            print

#a function used for recieving the users input on which
#cave they would like to choose
'''def chooseCave():
    cave = ''
    #makes sure the user is inputting either 1 OR 2
    while cave != '1' and cave != '2':
        print ('Which cave will you go into? (1 or 2)')
        cave = raw_input()
    #return the choice the user makes
    return cave'''

#this is the function used to check the cave.
#it will pass in the choice the user made and will check
#if it is the friendly cave or the evil cave
#program responds in different ways for each choice
def checkCave(chosenCave):
    print ('You approach the cave...')
    time.sleep(2)
    print ('It is dark and spooky...')
    print
    time.sleep(2)

    #friendly cave will be the first cave
    friendlyCave = 1

    #check against the users choice and the friendly cave
    if chosenCave == str(friendlyCave):
        print ('A Swarm of bats fly out of the cave!')
        print
        #we continue the hunt for treasure
        continueHunt(2, chosenCave)
        
    else:
        print ('A large boulder drops behind you and blocks the exit!')
        print
        continueHunt(2, chosenCave)



def continueHunt(decisionLevel, cave):
    
    if decisionLevel == 1:
        #makes sure the user is inputting either 1 OR 2
        while cave != '1' and cave != '2':
            print ('Which cave will you go into? (1 or 2)')
            cave = raw_input()
        #return the choice the user makes

        checkCave(cave)
    
    elif decisionLevel == 2:
        userChoice = ''
        while userChoice.upper() != 'L' and userChoice.upper() != 'R':
            print ('Would you like to go Left (L) or Right (R)?')
            userChoice = raw_input()
            userChoice = userChoice.upper()

        if cave == '1':
            
            if userChoice == 'L':
                print ('You went Left. A Swarm of bats fly out of the wall!')
                print ('Do you go run Back (B) or do you Push through them? (P)')
            elif userChoice == 'R':
                print ('You went Right. You tripped over a tripwire and triggered!')
                print ('a rolling boulder! Do you go Back (B) or do you Dodge it?(D)')
            
        else:
            if userChoice == 'L':
                print ('You went Left. Theres a gap in the road.')
                print ('Do you Jump (J) the gap or go Back?(B)')
            elif userChoice == 'R':
                print ('You went Right. The roof is slowing caving in!')
                print ('Do you Run (R) or do you go Back?(B)')

        choice = raw_input()
        choice = choice.upper()

        if choice == 'B':
            continueHunt(2, cave)
        else:
            if choice == 'P':
                print ('hello')
            elif choice == 'D':
                print ('goodbye')
            elif choice == 'J':
                print ('WINNER')
            elif choice == 'R':
                print ('oh no')
    else:
        print
    
    
    
#the main function takes care of calling the displayintro for the user
#as well as the choosecave and checkcave fucntions
def main():
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        continueHunt(1,'')
        'caveNumber = continueHunt(1)'
        'caveNumber = chooseCave()'
        'checkCave(caveNumber)'
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
