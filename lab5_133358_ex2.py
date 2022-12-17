# -*- coding: utf-8 -*-
'''
Name: Athir Al Abri
ID: 133358
program:  The program should print the result of performing the required operation on the input operands.
i/o: i( operand1, operand2, operation ),  o(result of operation)
Algo:
    - read operand1, operand2, operation
      check if operation not valid (+, -, *, /)
        exit('Error: invalid operation')
      check if operand2 is 0
        exit('Error: division by zero')
    - if operation '+' preform addition resurt= operand1 + operand2
      else if operation '*' preform  resurt= operand1 * operand2
      else if operation '/' preform  resurt= operand1 / operand2
      else if operation '-' preform  resurt= operand1 - operand2
    -ptint result
     
Test plan:
1.input: operand1= 2 , operand2= 0 , operation= / , output: Error: division by zero
2.input: operand1=-5 , operand2= 8 , operation= - , output: The result of -5 - 8 is: -13
3.input: operand1= 3 , operand2= 4 , operation= % , output: Error: invalid operation
4.input: operand1= 0 , operand2= 11, operation= + , output: The result of 0 + 11 is: 11      


'''

from sys import exit

operand1= int(input('Enter operand 1: '))
operand2= int(input('Enter operand 2: '))
operation= input('Enter operation: ')

if operation != '+' and  operation != '-' and operation != '*' and operation != '/':
    exit('Error: invalid operation')
if operation == "/" and operand2==0 :
    exit('Error: division by zero')    
   
if operation == '+' :
 result= operand1 + operand2
 op= "+"
elif operation == '*' :
 result= operand1 * operand2
 op="*"
elif operation == '/' :
 result= operand1 / operand2
 op="/"
elif operation == '-'  :
 result= operand1 - operand2
 op="-"
 
print() 
print('The result of', operand1,op,operand2,"is:", result)
