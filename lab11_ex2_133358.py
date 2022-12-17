# -*- coding: utf-8 -*-
"""
Name: Athir AlAbri
ID: 133358
Program: a program that reads form the keyboard student test scores in the 
range 0 – 100, and store these scores in a list.
Inputs: scores
Outputs: number of students in each score range
Algorithm: 
    -function main():
        calling functions
          list=readData()
          (a,b,c,d)= splitIntoRange()
        print formated output (len(list), ranges, a,b,c,d )
    -function readData():
        creat empty list lst=[]
        loop to read and validate score list
        append scores to the list
        retun the list
    -function splitIntoRange(list):
        initiliaze counters for each range
        loop i to len(list)
          check if list[i] in range 1:
              co+1
          elif list[i] in range 2:
              co2+1
          elif list[i] in range 2:
              co3+1
          else:
              co4+1
          return the counters
      -main()
    
Test plan:
_________________________________________________

enter value such that the last value is -1: 66

enter value such that the last value is -1: 98

enter value such that the last value is -1: 73

enter value such that the last value is -1: -1

Number of students: 3
0-59  60-79 80-89 90-100
===== ===== ===== ===== 
0     2     0     1      
_________________________________________________

enter value such that the last value is -1: -1

Number of students: 0
0-59  60-79 80-89 90-100
===== ===== ===== ===== 
0     0     0     0    
_________________________________________________

enter value such that the last value is -1: 5444

Number of students: 0
0-59  60-79 80-89 90-100
===== ===== ===== ===== 
0     0     0     0     
_________________________________________________  
"""


def main():
    #functions call
    lst= readData()
    (a,b,c,d)= splitIntoRanges(lst)
    #print formatted output
    print("\nNumber of students:", len(lst))
    print("%-6s%-6s%-6s%-6s"%("0-59",  "60-79", "80-89", "90-100"))
    print("===== "*4)
    print("%-6d%-6d%-6d%-6d"% (a,b,c,d))

    
    
def readData():
    lst=[] #empty list 
    score=int(input("enter value such that the last value is -1: "))
    while score>=0 and score<=100: #validate the inputs
          lst.append(score)
          score=int(input("enter value such that the last value is -1: "))
    return lst

def splitIntoRanges(lst):
    #creat counters 'co'
    co1=0 ; co2=0 ; co3=0 ; co4=0  
    for i in range(len(lst)):
        if lst[i] in range(0,60):
            co1+=1
        elif lst[i] in range(60,80):
            co2+=1 
        elif lst[i] in range(80,90):
            co3+=1
        else:
            co4+=1
    #return values as tuple
    return(co1, co2, co3, co4) 

#main function call    
main()