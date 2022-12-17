# -*- coding: utf-8 -*-
"""
Name: Athir AlAbri
ID: 133358
Program: a python program that reads line of data from file and calculate the average
and print the values that is above the avarage.
Inputs: data.txt
Outputs: outputFile
Algorithm: 
1-open input file 
2-loop read line:
    line(remove  \n)
    lst= creat list from the line lst=line.split()
    avg= sum(lst.../ len...)
    if lst[0]=="up" :
        for i: 1 to len of lst:
            check if lst[i] >= avg then print on the output file on the same line
         
    elif lst[0]=="down"
        for i: 1 to len of lst:
            check if lst[i] <= avg then print on the output file on the same line

    write  \n on the output file
test plan:
35 30 40 30 
20 30 25 25 
35 45 40 

"""
#opening files
inputFile= open("data.txt", "r")
outputFile=open("sorted.txt", "w")

	
	
for line in inputFile:
    #remove the new line
    line.strip("\n")
    lst=line.split()
    sum=0
    for i in (lst[1:len(lst)]):
        sum=sum+int(i)
    #find the average
    avg = sum/len(lst) - 1
    if lst[0]=="UP":
        for i in lst[1:len(lst)]:
            i=int(i)
            #check if i more than average
            if i>= avg:
                outputFile.write(str(i)+" ")
                print(i,"",  end="")
        print()
        outputFile.write("\n")
    elif lst[0]=="DOWN":
        for i in lst[1:len(lst)]:
            i=int(i)
            if i>= avg:
                outputFile.write(str(i)+" ")
                print(i,"", end="")
        outputFile.write("\n")
        print()
#closing files        
inputFile.close()        
outputFile.close()

     