''' Author: Jesse Higgins
    Program: First program
    Description: ***
'''

def main():
    #tell the user something
    print ("Welcome to the cheese shop!")

    #get information from the user
    cheeseType = raw_input("What kind of cheese would you like?")

    #we dont have that kind
    print ("Sorry! We are all out of ")
    print (cheeseType)

if __name__ == "__main__": main()
