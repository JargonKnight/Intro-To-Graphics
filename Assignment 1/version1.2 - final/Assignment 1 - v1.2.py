''' Author: Jesse Higgins
    Last Modified by: Jesse Higgins
    Date Last Modified: May 10th 2013
    Program: Assignment1 - v1.2.py
    Description: A decision making, text-based program that allows the user
                 to have one possible positive outcome
'''
#import libraries for pausing lines of text during
#execution of program
import time

#an intro function giving the user background information of the program
def displayIntro():
            print ('You are on a Hunt for treasure. In front of you,')
            print ('you see two caves. However, You are not sure which,')
            print ('cave will bring you to the treasure!')
            print

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
        print ('A Swarm of bats fly out of the cave! Startles you a bit.')
        print
        #we continue the hunt for treasure
        continueHunt(2, chosenCave)
        
    else:
        print ('A large boulder drops behind you and blocks the exit!')
        print ('No going back now...')
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
    
    else:
        #create the user choice
        userChoice = ''
        while userChoice.upper() != 'L' and userChoice.upper() != 'R':
            print ('Would you like to go Left (L) or Right (R)?')
            #recieve user input to validate their choice
            userChoice = raw_input()
            userChoice = userChoice.upper()

        #each cave has their own scenarios so we check if they
        #picked the first or 2nd cave
        if cave == '1':

            #validate scenarios dependant on which cave the user is in
            if userChoice == 'L':
                print ('You went Left. A Swarm of bats fly out of the wall!')
                print ('Do you Push (P) through them or Attempt (A)')
                print ('to kill them? (B) to go Back.')
            elif userChoice == 'R':
                print ('You went Right. You tripped over a tripwire and triggered!')
                print ('a rolling boulder! Do you Dodge (D) it or do you')
                print ('get in front to Stop (S) it from rolling? (B)')
                print ('to go Back')
            
        else:
            if userChoice == 'L':
                print ('You went Left. Theres a gap in the road.')
                print ('Do you Jump (J) the gap or try to Climb (C) the wall')
                print ('to the other side? (B) to go Back')
            elif userChoice == 'R':
                print ('You went Right. The roof is slowing caving in!')
                print ('Do you Run (R) through the tunnel or do you')
                print ('Hide (H) in a hole in the wall? (B) to go Back')

        #get the users choice for the 3rd decision level
        choice = raw_input()
        #convert it to uppercase for easier validation
        choice = choice.upper()

        #check if the user is going back to recall the 2nd decision level
        if choice == 'B':
            continueHunt(2, cave)
        #and an else statement to then check the users choice
        #for the final outcome of the 3rd decision
        else:
            #Cave 1 and Left
            if choice == 'P':
                print ('You push through the Bats and run into Dracula')
                print ('who defends his cave by draining all of your blood')
            elif choice == 'A':
                print ('There were too many Bats to kill. They swarmed you')
                print ('And have taken your life!')

            #Cave 1 and Right    
            elif choice == 'D':
                print ('You Dodge the Boulder but it catches your shoelace')
                print ('and drags you with it. Knocking you out and killing you')
            elif choice == 'S':
                print ('You had way too much confidence in stopping a BOULDER')
                print ('You are not The Hulk. You were crushed and killed')

            #Cave 2 and Left    
            elif choice == 'J':
                print ('You successfully Jump the gap and make it down the')
                print ('Hall to find the Treasure! YOU WIN!')
            elif choice == 'C':
                print ('The wall crumbles and you fall to your death in')
                print ('the deep, dark pits of the cave')

            #Cave 2 and Right    
            elif choice == 'R':
                print ('You failed to outrun the cave-in and get crushed!')
            elif choice == 'H':
                print ('You are now trapped and cannot get out of the hole.')
                print ('You starve to death')
    
    
#the main function takes care of calling the displayintro for the user
#as well as the choosecave and checkcave fucntions
def main():
    
    playAgain = 'yes'
    #a loop to keep the game running unless the user says anything but 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        continueHunt(1,'')
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
