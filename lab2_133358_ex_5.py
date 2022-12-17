
"""
Name: Athir AlAbri
ID: 133358
Problem: to find the area of the triangle
i/o: input: a, b, c      output: area

algorithm:
    1. set tringle sides values a = 5, b = 7, c = 10
    2. find the value of s=(a+b+c)/2
    3. find the area of tringle area= sqrt(s*(s-a)*(s-b)*(s-c))
    4. print area
    

"""
from math import *

a = 5
b = 7
c = 10
s = (a+b+c)/2

area= sqrt(s*(s-a)*(s-b)*(s-c))
print ('The area of the triangle i:', area)



