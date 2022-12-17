# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 04:00:52 2022

@author: Hp
"""

from math import *
def main():
    lstt=readData()
    printResults(lstt)
    
def mean_f(lst): 
    mean=sum(lst)/len(lst)
    return mean
def readData():   
    lst=[]
    num=int(input(" enter value such that the last value is -1"))
    while num!=-1 :
        lst.append(num)
        num=int(input(" enter value such that the last value is -1"))
    return lst

def sd(lst):
    s=0
    for i in range(len(lst)):
        s=s+(lst[i] -mean_f(lst))**2 
    sd=sqrt(s/len(lst))
    return sd

def printResults(lst):        
    mean_v= mean_f(lst)
    sdev=sd(lst)
    print("******report*******")
    print("list=",lst)
    print("mean= ",mean_v)
    print("SD=",sdev)
    
main()   