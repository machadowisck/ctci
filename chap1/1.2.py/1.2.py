#! /usr/bin/env python
# -*- coding : utf-8 -*-

import sys


""" Could also have added a test for printable characteres and make sure it reverses only those"""

def reverse_string_old(strTest):
    auxstr = ''
    print strTest + ' size: ' + str(len(strTest))
    i = len(strTest)-1
    while i >= 0: 
        auxstr += strTest[i]
        i-=1
    print auxstr+ ' size: ' + str(len(auxstr))

def reverse_string(strTest):
    auxstr = ''
    print strTest + ' size: ' + str(len(strTest))
    i = len(strTest)-2 # -2 = last index before \0
    while i >= 0: 
        auxstr += strTest[i]
        i-=1
    auxstr +='\0' # makes sure it still have a C-Style string
    print auxstr+ ' size: ' + str(len(auxstr))

#print str(None)

print 'None is ' + str(None)
test_string = "abcredf"
if len(sys.argv) > 1:
    test_string = sys.argv[1]
if test_string[-1] != None:
    test_string += '\0'

reverse_string(test_string)

