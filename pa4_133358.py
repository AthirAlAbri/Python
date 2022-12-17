# -*- coding: utf-8 -*-
"""
Name: Athir AlAbri
ID: 133358
Section: 21
Problem: a program that simulate the look and say generator
Inputs: Terms, Input file
Outputs: Output file, term1, ==> Look and Say ==> , term2
Algorithm:
1. import exist from sys
2. function readAndValidate(line):
    creat an empty list (lst=[])
    convert line to string
    remove the new line character from line using rstrip() method
    for i in line:
        if i.isdigit(): >> append it to lst
        else: >> exit
    return the list
        
3. function lookAndSay(term): 
    convert term to string
    creat an empty list (newList=[])
    loop for the len of term
    while i<len(term):
        creat a counter =1
        while i+1 < len(term) and term[i] = term[i+1]:
            add 1 to i to change the condition of the loop
            counter=counter+1
        append the counter and term[i] to the newlist
        add 1 to i to change the condition of the loop
    return the new List    
    
4. function display(term1,term2,outfile):
    print formated outputto the console and the output  file
        (term1, "==> Look and Say ==>", term2)    
    
5. function main():
    read input and output file from the user 
    open input and output file 
    read a line from input file and save it to variable term1
    remove the new line character from term1 using rstrip() method
    call function readAndValidate and send term1 to it(readAndValidate(term1))
    print the header of the program
    read a number from the user
    loop for the number of number that user entered
    for i in range num :
        call the function lookAndSay( term2 = lookAndSay(term1) )
        remove the new line character from term2 using rstrip() method
        call the function display ( display(term1,term2,outputFile) )
        term1 = term2 
    close input and output file 
    
6. call main() function

    
Test plan: 
____________________________________________________________
-run: 1
-Input file: 1
-screen output:
    Input file name: data.txt

    Output file name: output.txt
    ********************
    This program will generate a sequences of
    terms using look and say sequence generator.
    The initial term is given in the input file.
    ********************

    Enter how many terms in the sequences to generate: 3

    1 ==> Look and Say ==> 11
    11 ==> Look and Say ==> 21
    21 ==> Look and Say ==> 1211
    
-Output file: 
    1 ==> Look and Say ==> 11
    11 ==> Look and Say ==> 21
    21 ==> Look and Say ==> 1211
____________________________________________________________
-run: 2
-Input file: 1234
-screen output: 
    Input file name: data.txt

    Output file name: output.txt
    ********************
    This program will generate a sequences of
    terms using look and say sequence generator.
    The initial term is given in the input file.
    ********************

    Enter how many terms in the sequences to generate: 2

    1234 ==> Look and Say ==> 11121314
    11121314 ==> Look and Say ==> 311211131114
-Output file: 
    1234 ==> Look and Say ==> 11121314
    11121314 ==> Look and Say ==> 311211131114 	
____________________________________________________________
run: 3
Input file: #824
screen output: 
    Input file name: data.txt

    Output file name: output.txt
    An exception has occurred, use %tb to see the full traceback.

    SystemExit: Error: invalid input data
Output file: 
    there is no output file	
____________________________________________________________
"""

from sys import exit

def readAndValidate(line):  
    #creat an empty list
    lst=[]
    line = str(line)
    #remove the new line character from right
    line = line.rstrip("\n")
    for i in line:
        #cheack if elements are valid
        if i.isdigit():
            lst.append(int(i))
        #if not valid >> exit
        else:
            exit("Error: invalid input data")
    #return the list
    return lst


def lookAndSay(term):
    #convert term to string
    term=str(term)
    newList=[]
    i=0 #initialize i
    while i<len(term):
        count=1
        while i+1 < len(term) and term[i] == term[i+1]:
            i=i+1
            count=count+1
        newList.append(str(count) + term[i]) 
        i=i+1
    #return the newList
    return ''.join(newList) 

    
def display(term1,term2,outfile):
    #printing formatted output
    print(term1, "==> Look and Say ==>", term2, file=outfile)
    print(term1, "==> Look and Say ==>", term2)

    
    
def main():
    file1=input("Input file name: ")
    file2=input("Output file name: ") 
    #open files
    inputFile= open(file1, "r")
    outputFile=open(file2, "w")
    term1=inputFile.readline()
    term1=term1.rstrip("\n")
    #call readAndValidate function and save the result into varible
    result=readAndValidate(term1)
    #header of the program
    print("*"*20)
    print("This program will generate a sequences of\nterms using look and say sequence generator.\nThe initial term is given in the input file.")
    print("*"*20)
    
    num=int(input('Enter how many terms in the sequences to generate: ')) 
    print()

    #loop for the number of terms that user entered
    for i in range(num):
        term2=lookAndSay(term1) 
        term2=term2.rstrip("\n")
        display(term1,term2,outputFile)
        term1=term2        
        
    #close filse
    inputFile.close()
    outputFile.close()
    
    
    
    
#call main function    
main()  





  