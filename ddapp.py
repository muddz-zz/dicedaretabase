#!/usr/local/bin/python2.7
# encoding: utf-8
'''
dicedaretabase -- Dice Dare CLI app

dicedaretabase is small CLI application which lets you do different kind of dice dares.

It defines classes_and_methods

@author:     Muddz

@copyright:  2014 Muddz. All rights reserved.

@license:    license

@deffield    updated: 20-4-2014
'''

import sys
import os
import sqlite3
import random
import collections

con = sqlite3.connect('daretabase.db')
cur = con.cursor()

__all__ = []
__version__ = 0.1
__date__ = '2014-04-20'
__updated__ = '2014-04-20'


#The first function that starts
#redirects to the different functions of the program
def main():

    print('''What would you like to do?
    Press 1 to show the different dare groups
    Press 2 to add a dare (not implemented yet)
    Press 3 to export a dare (not implemented yet)
    ''')

    choice = raw_input("What would you like to do?: ")
    choice = toInt(choice)


    if choice == 1:
        Menu().chooseTypeMenu()
    elif choice == 2:
        Menu().addDareMenu()

    elif choice == 3:
        pass
    else:
        main()

#this function tries to convert a users input to int
#If it does not work it throws an exception, also all the tables.
# (╯°□°）╯︵ ┻━┻


def toInt(i):
    try:
        i = int(i)
    except:
        print("Got shit in your eyes? You did not enter a number, please do.")
    return i


# Colors and stuff
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# The function that actually throws all the steps on the screen
class ShowDare:

    def show(self, dare):

        cur.execute("SELECT * FROM steps WHERE dare = (?)", (dare,))
        steps = cur.fetchall()

        for step in steps:
            print(step[3])
            raw_input(bcolors.OKGREEN
                      + "Press any key to see what you rolled"
                      + bcolors.ENDC)
            outcome = random.randrange(1, 6)
            print("Ow, you got a {0}!").format(outcome)


class AddDare:

    def addDare(self):
        print(bcolors.HEADER
              + "What kind of dare do you want to add?"
              + bcolors.ENDC)

        # Asks for the list of dare types and displays the menu.
        darenumbers = Menu().listDareTypes()
        choice = raw_input("I choose number:")
        choice = toInt(choice)
        if choice in darenumbers:
            print("You choose number {0}, lets get started shall we?") \
            .format(choice)
        else:
            print("You didn't enter a valid choice, please do next time.")
            self.addDare()
        darename = raw_input("And how would you want to call the dice dare?: ")
        nickname = raw_input("And what is your (nick)name?: ")
        cur.execute("INSERT INTO dares VALUES (NULL, ?, ?, ?)", (choice, darename, nickname))
        dareid = cur.lastrowid

        print(
              """We are going to go through each step of the dice dare,
              For each step I will ask you how to call the step and
              What the possible outcomes are.
              Right now, every step needs 6 outcomes.""")

        # declare a bool to check if there are any more steps coming after this
        stop = False

        stepnr = 1
        while not stop:
            steptext = raw_input("For this step, the dare-y needs to: ")

            cur.execute("INSERT INTO steps VALUES (NULL, ?, ?, ?)",
                        (dareid, stepnr, steptext))

            print("Great idea! And what are the outcomes going to be?")
            for i in range(1, 7):
                text = raw_input("What does the dare-y have to do when rolling a {0}: ".format(i))

                cur.execute("INSERT INTO outcomes VALUES (NULL, ?, ?, ?, ?)",
                        (dareid, i, text, stepnr))

            cont = raw_input("""If this was the last step, type 'q' without quotes,
            If you want to continue adding steps, press any other key.""")

            if cont == "q":
                stop = True
            else:
                pass
        con.commit()




        stepnr += 1





class Menu:

    #Lists the current dare types and returns a list with ints corresponding
    #the types in de daretabase.
    def listDareTypes(self):

        #Get all the dare types from the database
        cur.execute("SELECT * FROM 'daretypes'")
        daretypes = cur.fetchall()

        #Create a list with dare numbers to check against.
        #Might be there is a way more elegant solution for this though
        darenumbers = []

        #Print a row for each of the types
        for daretype in daretypes:
            print(bcolors.HEADER
                   + "{0} - {1}"
                   + bcolors.ENDC).format(daretype[0], daretype[1])

            # Add the number of the current type to the list
            darenumbers.append(daretype[0])

        return darenumbers

    # Info for the dare listing menu
    def chooseTypeMenu(self):

        # Asks for the list of dare types and displays the menu.
        darenumbers = self.listDareTypes()

        # Get the input from the user
        daretype = raw_input("Choose a type of dare by typing a number: ")
        # Check if the input was actually a number
        #try to convert to int
        daretype = toInt(daretype)

        if daretype in darenumbers:
            # Clear the screen again and display the different dare types

            os.system('cls' if os.name == 'nt' else 'clear')
            cur.execute(
                        "SELECT * FROM dares WHERE daretype = (?)",
                        (daretype,))
            dares = cur.fetchall()
            for dare in dares:
                print(bcolors.HEADER
                      + "{0} - {1}"
                      + bcolors.ENDC).format(dare[0], dare[2])

            dare = raw_input("Which dare would you like from this category?: ")
            dare = toInt(dare)

            ShowDare().show(dare)

    def addDareMenu(self):
        print("""So you want to add a new dare to the daretabase? Great!
If you like to share your dare afterwards, you can do so by exporting
it to a file and emailing or PMing it to me.
""")
        AddDare().addDare()


#initiates the __main__ function
if __name__ == "__main__":
    main()