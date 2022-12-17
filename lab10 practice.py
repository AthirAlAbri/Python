# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:54:31 2022

@author: Hp
"""

from random import *

Items=["cake", "coffee", "iced coffee"]
prices=[0.550, 0.300, 0.250]
quan=[]
for i in range(len(Items)):
    num=randint(1,50)
    quan.append(num)
    
rev=[]
co=0
for i in range(len(Items)):
    result=prices[i]*quan[i]
    rev.append(result)
    co+=1
    
print("%-12s %-8s %-9s %-6s" %("Item", "Price", "Quantity", "Revenue"))
print("*"*40)
for i in range(len(Items)):
    print("%-12s %-8.3f %-9d %-6.3f" %(Items[i],prices[i] ,quan[i] ,rev[i] ))
print("*"*40)    

total=0    
for element in rev :
    total= total+element

ave=total/co
    
print("Total revenue= ", total ,"OMR")
print('The average= ', ave) 

for i in range(len(rev)):
    if rev[i]< ave:
        print("%-12s"%Items[i], "", rev[i])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    