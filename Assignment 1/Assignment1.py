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
            print ('you see two caves. Both caves meet up later on! However,')
            print ('In one cave, the path is much more difficult to get to the')
            print ('treasure and the other cave is a walk in the park.')
            print

#a function used for recieving the users input on which
#cave they would like to choose
def chooseCave():
    cave = ''
    #makes sure the user is inputting either 1 OR 2
    while cave != '1' and cave != '2':
        print ('Which cave will you go into? (1 or 2)')
        cave = raw_input()
    #return the choice the user makes
    return cave

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
        print ('Friendly bunny rabbits begin prancing out of the cave')
        print ('This must be the simple cave. phewf')
        print
        #we continue the hunt for treasure
        continueHunt()
        
    else:
        print ('A large boulder drops in front of you and')
        print ('just misses you... this must be the difficult cave')
        print
        continueHunt()

def continueHunt():
    print
    
    
    
#the main function takes care of calling the displayintro for the user
#as well as the choosecave and checkcave fucntions
def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
