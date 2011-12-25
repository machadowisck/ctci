#! /usr/bin/env python
# -*- coding: utf-8 -*-

test_string = "abcd123a"

def unique_chars(strTest):
    char_bank = []
    unique = 1
    for chr  in strTest:
        if chr in char_bank:
            unique = 0
        else:
            char_bank.append(chr)
    print unique

unique_chars(test_string)



        
    
