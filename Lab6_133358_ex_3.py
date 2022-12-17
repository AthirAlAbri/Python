# -*- coding: utf-8 -*-
"""
Name: Athir AlAbri
ID: 133358
Program: program that reads from the user an integer n between 1 and 20, and then computes and 
prints all intermediary summations from 1 up to and including n.
c
    -read n
    -check if n is invalid then exit
       if n<0 or n>=20 then exit
    -loop to find summations
      i=0
      sum=0
      while i <= n 
          sum=sum+i
       print(sum)
Test plan:
1-
input: 4
output: 
n        sum        
1        1       
2        3       
3        6       
4        10     
-----------------
2-
input: 2
output:
n        sum         
1        1       
2        3       
-----------------
3-
input: 0
output: ERROR: invalid data
-----------------
4-
input: 1
output:
n        sum     
1        1       
    
"""
   
from sys import exit


#reading n
n= int(input("PLZ input a value of n: "))
#checking validty
if n<=0 or n>=20:
    exit('ERROR: invalid data') 
else:
    print("%-8s %-8s" %("n","sum"))
    print("%-8s %-8s" %("=","==="))
    


i= 0
sum= 0
#looping
while i <= n-1 :
   i= i+1
   sum= sum+ i   #summations
   print("%-8s %-8s" % (i, sum))   #print outputs

