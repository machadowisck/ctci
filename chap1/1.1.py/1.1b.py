#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def unique_chars(strTest):
    if not len(strTest):
        strTest = test_string
    unique = 1
    i=0
    print len(strTest)
    #return 
    while i < len(strTest):
        print i; print strTest[i]
        for chr in strTest[i+1:]:
            print chr
            if str(chr) == str(strTest[i]):
                unique = 0
                pass
        i+=1
            
    print bool(unique)

test_string = "abc3a"
if len(sys.argv) >1 :
    test_string = sys.argv[1]
unique_chars(test_string)



        
    
