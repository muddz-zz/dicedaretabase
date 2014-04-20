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

con = sqlite3.connect('daretabase.db')
cur = con.cursor()

__all__ = []
__version__ = 0.1
__date__ = '2014-04-20'
__updated__ = '2014-04-20'

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


#Get all the dare types from the database
cur.execute("SELECT * FROM 'daretypes'")
daretypes = cur.fetchall()

#Print a row for each of the types
for daretype in daretypes:
    print(bcolors.HEADER + "{0} - {1}" + bcolors.ENDC).format(daretype[0], daretype[1])

# Get the input from the user
daretype = raw_input("Choose a type of dare by typing a number: ")
# Check if the input was actually a number
try:
    #todo: replace this by checking the actual list
    daretype = int(daretype)
except:
    print("Got shit in your eyes, you did not enter a number?")

if daretype <= 6:

    os.system("clear") #This only works at linux, I guess?
    cur.execute("SELECT * FROM dares WHERE daretype = (?)", (daretype,))
    dares = cur.fetchall()
    for dare in dares:
        print(bcolors.HEADER + "{0} - {1}" + bcolors.ENDC).format(dare[0], dare[2])

    dares = raw_input("Which dare would you like from this category?: ")



