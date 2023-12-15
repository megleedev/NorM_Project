# Python: 3.12.1
#
# Author: Meg Lee
#
# Description: Created as part of The Tech Academy's Python Bootcamp. 

def start(nice = 0, mean = 0, name = "") :
    # gets users name
    name = describe_game (name)
    nice, mean, name = nice_mean (nice, mean, name)

def describe_game (name) :
    """
        checks if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank player for playing
        again and continue with the game
    """
    if name != "":
        print ("\nThank you for playing again, {}!".format(name))
    
    else:
        stop = True
        while stop:
            if name == "":
                art = open ('art.txt', 'r')
                print (''.join([line for line in art]))
                name = input ("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print ("\nWelcome, {}!".format(name))
                    print ("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print ("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean (nice, mean, name) :
    stop = True
    while stop:
        show_score (nice, mean, name)
        pick = input ("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()

        if pick == "n":
            print ("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False

        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False

    score (nice, mean, name) # passes the 3 variables to score()

def show_score (nice, mean, name) :
    print ("\n{}, your current total score: \n({}, Nice) and ({}, Mean)".format (name, nice, mean))

def score (nice, mean, name) :
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function
        win (nice, mean, name)
    
    if mean > 2: # if condition is valid, call lose function
        lose (nice, mean, name)

    else: # else, call nice_mean function
        nice_mean (nice, mean, name)

def win (nice, mean, name) :
    print ("\nNice job {}, you win! \nCongrats on the friends you made along the way!".format(name))
    again (nice, mean, name)

def lose (nice, mean, name) :
    print ("\nYou were rude to everyone {}! You now have no friends.".format(name))
    again (nice, mean, name)

def again (nice, mean, name) :
    stop = True
    while stop:
        choice = input ("\nDo you want to play again? (y/n): \n>>>").lower()

        if choice == "y":
            stop = False
            reset (nice, mean, name)

        if choice == "n":
            print ("\nSorry to see you go!")
            stop = False
            quit()

        else:
            print ("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset (nice, mean, name) :
    nice = 0
    mean = 0
    # no need to reset the name variable as the same user is playing the game
    start(nice, mean, name)

if __name__ == "__main__":
    start()