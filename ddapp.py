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



cur.execute("SELECT * FROM 'daretypes'")
daretypes = cur.fetchall()
for type in daretypes:
    print("{0} for {1}").format(type[0], type[1])

# Get the input from the user
daretype = raw_input("Choose a type of dare by typing a number: ")
# Check if the input was actually a number
try:
    #todo: replace this by checking the actual list
    daretype = int(daretype)
except:
    print("Got shit in your eyes, you did not enter a number?")

if daretype < 9:
    print(daretype)