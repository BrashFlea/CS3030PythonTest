#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys

"""
Python exam
Problem 2
Secure password checker
"""

def IsValidPassword(password):
    #Password length check
    if(len(password) < 8):
        print("Password too short")
        return False
    #Using some reverse logic here. Checking to see if the password is:
    #islower() all lowercase (missing uppercase)
    #isupper() all uppercase (missing lowercase)
    #isalpha() all alphabetic characters (missing number)
    #This will validate the password as we want to not trip the if block.
    if(password.islower() or  password.isupper() or password.isalpha()):
        print("That password didn't have the required properties")
        return False
    else:
        print("Password satisfies conditions")
        return True


# Main function
def main(password):
    IsValidPassword(password)
    return


if __name__ == "__main__":
    # Call Main
    status = True
    while(status == True):
        firstPass = input("Enter your password: ")
        secondPass = input("Re-enter your password: ")
        while(firstPass != secondPass):
            print("Passwords didn't match")
            firstPass = input("Enter your password: ")
            secondPass = input("Re-enter your password: ")
        main(firstPass)
        quit = input("Would you like to quit? Y/N: ")
        if(quit == "Y" or quit == "y"):
            status = False

    exit(0)

