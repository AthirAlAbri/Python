# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:26:13 2022

@author: Hp


strint="hello world"
tupple=("world", "hello")
result=strint.endswith(tupple)
print(result)
"""

def main():
    num1,num2,num3= input("enter 3 numbers: ").split()
    if num1.isdigit() and num2.isdigit() and num3.isdigit():
        addint(int(num1), int(num2), int(num3))
    else:
        num1,num2,num3= input("enter 3 numbers: ").split()
        addint(int(num1), int(num2), int(num3))
    printresult(int(num1), int(num2), int(num3))
        
        
    
    
    
def addint(x,y,z):
    sumation=x+y+z
    #print(sumation)
    return sumation
    
    
    
def printresult(x,y,z):
    print("="*20)
    summ= addint(x,y,z)
    av= summ/3
    maxx=max(x,y,z)
    print(summ)
    print(av)
    print(maxx)
    
    
main()