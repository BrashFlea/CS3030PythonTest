#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys

"""
Python test
Problem 1
Computes financial assistance for families based on income and children
"""

def calcAssist(income, children):
    assist = 0
    #$30k-$40k
    if(income >= "30000" and income <= "40000"):
        if(children >= "3"):
            assist = (1000 * int(children))
    #20k-30k
    if(income >= "20000" and income < "30000"):
        if(children >= "2"):
            assist = (1500 * int(children))
    #Under 20k
    if(income < "20000"):
        assist = (2000 * int(children))
    #Print assistance amount    
    print("The assistance amount is ${}".format(assist))


# Main function
def main(income, children):
    calcAssist(income,children)
    return


if __name__ == "__main__":
    # Call Main
    income = 0
    children = 0
    
    income = input("What is the household income? (-1 to quit) ")
    while(income != "-1"):
        children = input("How many children? ")
        main(income,children)
        income = input("What is the household income? (-1 to quit) ")
    print("Goodbye")
    exit(0)

