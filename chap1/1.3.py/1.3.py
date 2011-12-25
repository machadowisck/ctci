#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
Test cases: 
- funtion should retrn a fail when removing duplicates from an empty string
- function should not return duplicates in answer, no matter how n=many occurrences are found for a letter
- function should return letters  
"""

def remove_duplicates(strParam):
    print strParam
    found = []
    strParam = list(strParam)
    print strParam
    for i in range(len(strParam)):
        print i
        print 'found: ' + str(found)
        if strParam[i] not in found:
            found.extend(strParam[i])
    print ''.join(found)
        



test_string = 'abacadab'
if len(sys.argv) > 1 :
    test_string = sys.argv[1]

remove_duplicates(test_string)
