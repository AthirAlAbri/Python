# -*- coding: utf-8 -*-
"""
Name: Athir AlAbri
ID: 133358
Program:  program to read three numbers and prints “All the same” if they are all the same,
“All different” if they are all different, and “neither” otherwise.
Inputs: num1, num2, num3
Outputs: All the same/ All different/ Neither
Algorithm:
    - import exit from sys
    - read 3 numbers from the user(num1, num2, num3)
    - check if the values are digits 
    - if they are digits check:
        if num1== num2== num3  print All the same
        elif num1!= num2!= num3 print All different
        else print Neither
    - else exit the 3 values must be numbers
--------------------------------------------------------------
Test plan:
1- the 3 values: 2 2 2   the result: All the same
2- the 3 values: 3 2 5   the result: All different
3- the 3 values: 2 2 3   the result: Neither   
4- the 3 values: 5 s 1   the result: SystemExit: The 3 values must be numbers  
--------------------------------------------------------------
"""

from sys import exit

#reading inputs from the user
num1, num2, num3 = input('please enter 3 numbers: ').split()

#if statments
if num1.isdigit() and num2.isdigit() and num3.isdigit(): #check validity
    if num1== num2== num3 :    #inpurs are valid
         print( "All the same")
    elif num1!= num2!= num3 :
         print("All different")
    else:
         print( "Neither")
else:                          #inpurs are not valid
  exit("The 3 values must be numbers ")    


