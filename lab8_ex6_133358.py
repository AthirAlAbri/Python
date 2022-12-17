# -*- coding: utf-8 -*-
"""
Name: Athir AlAbri
ID: 133358
Problem: a program that generates a random positive integer n devisable 
by 3 between 1 and30 (don’t forget to validate the input), then generate 
encryption key string based on the combination numbers starting from 1 
for each single component number of n that devisable by 3.
input: generate
output:key
algo: 
     answer="Y"
     while answer=="Y"
       key=""
         n=generate in range....
         validate n(positive, integer, div by 3, (1-30))
         for i=1 to n        for i in range(1,n+1)
            if i%3==0:
                for j=1 to i:   for j in range(1,i+1)
                   key=key+str(j)
                key=key+"x"
        print key
        answer=input("Do you want to continue?")
test plan: 
generate= 31
Error

generate= 6
key= 123x123456x
Do you want to continue? y

generate= 24 
key= 123x123456x123456789x123456789101112x12345678910111
2131415x123456789101112131415161718x12345678910111213141
5161718192021x123456789101112131415161718192021222324x
Do you want to continue? Y

generate= 17
key= 123x123456x123456789x123456789101112x123456789101112
131415x
Do you want to continue? n


"""

from sys import exit


answer="Y"

i=0
j=0

while answer=="Y":
    generate=int(input("Enter a value: "))
    key=""
    n=generate
    if n<1 or n>30:
        exit("Error")
    for i in range(1,n+1):
        if i%3==0:
            for j in range(1,i+1):
                key=key+str(j)
            key=key+("x")
    print(key)
    answer=input("Do you want to continue? ").upper()

            















