# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:44:28 2022

@author: Hp
"""

def main():
    firstlst=readList()
    print("Before: ", end="")
    for i in firstlst:
        print (i, "" , end="")
    #rint()
    num=int(input("enter a numbet: "))
    finallst=shiftList(firstlst, num)

    print("After:", end="")
    for i in finallst:
        print(i, "" , end="")
   
    



def readList():
    data=1
    lst=[]
    while data>0:
        data=int(input("enter a value or -1 to finish: "))
        if data>0:
            lst.append(data)
    #print(lst)
    return lst
        
def shiftList(lst,n):
    lastLst=[0]*len(lst)
    for i in range(len(lst)):
        lastLst[i]=lst[i-n]
        #lastLst.append(lst[i])
    return lastLst
    
    
    
    
main()   