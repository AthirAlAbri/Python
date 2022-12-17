"""
Name: Athir AlAbri
ID: 133358
Program:a Python program that creates a list containing ten random integers in the range 1 to 50.
Then,create two additional lists: one contains the non-duplicate values and the other one contains
the duplicate values. Print the three lists.
Input:
    -
Output:
    list of randomly numbers(original list)
    list of non-duplicate numbers from the original list 
    list of duplicate numbers from the original list
Algorithm:
    -generate listt[] randomly
    -print listt
    -create  dupList[], non_dupList[] 
    -make while loop:
        while(len listt)!=0:
            item=list[0]
            count=0
            for i in range(len listt):
                if item=list[i]
                count=count+1
            if count>1:
                add item to duplist[]
                remove item from list
            else:
                add item to non_duplist[]
                remove item from list
      -print dupList and non_dupList
                
Test plan:
(1):  
Original list:       [25, 42, 24, 33, 24, 39, 29, 43, 9, 37]
Non-Duplicate list:  [25, 42, 33, 24, 39, 29, 43, 9, 37]
Duplicate list:      [24]

(2):
Original list:       [36, 50, 4, 25, 5, 33, 28, 16, 29, 41]
Non-Duplicate list:  [36, 50, 4, 25, 5, 33, 28, 16, 29, 41]
Duplicate list:      []

(3):
Original list:       [8, 8, 2, 44, 33, 7, 3, 38, 46, 8]
Non-Duplicate list:  [2, 44, 33, 7, 3, 38, 46, 8]
Duplicate list:      [8, 8]

"""


from random import *

dupList = []
non_dupList = []
# generate random list
listt = []
for i in range(10):
    listt.append(randint(1, 50))
print("%-20s" % "Original list:", listt)
# start processing lists
while len(listt) != 0:
    item = listt[0]
    #creat a counter
    count = 0  
    for i in range(len(listt)):
        if item == listt[i]:
            count += 1
    if count > 1:
        #item is duplicated
        dupList.append(item) 
        listt.remove(item)
    else:
        #item is not duplicated
        non_dupList.append(item) 
        listt.remove(item)
        
print("%-20s" % "Non-Duplicate list:", non_dupList)
print("%-20s" % "Duplicate list:", dupList)









