#!/usr/local/bin/python2.7
# encoding: utf-8
'''
ddapp -- Dice Dare CLI app

ddapp is small CLI application which lets you do different kind of dice dares.

It defines classes_and_methods

@author:     Muddz

@copyright:  2014 Muddz. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: 20-4-2014
'''

import sys
import os
import sqlite3

conn = sqlite3.connect('daretabase.db')
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

def showmenu(daretypes):
    print(daretypes)

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]


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

