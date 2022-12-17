# -*- coding: utf-8 -*-
"""

Name: Athir AlAbri
ID: 133358
Section: 21
Problem: This program calculates the payable amount of the electricity bill according to the
tariffs outlined in Table 1, and prints a summary report.
Inputs: account type, account number, units consumed, rate amount
Outputs: Payable Amount(cost)     
Algorithm:
   -import exit from sys
   -read account type(S,B,A), account number, units consumed from the user
      for account number and units consumed: check if the user entering no data, 
      entering invalid account type, and entering non-numeric or negative values
        exit('Error: invalid value')
   - define varebuls ans constant(cost, RATE1/2/3)
   - aply if statment for the 3 account types (S,B,A): 
   if account type is (S/ B/ A)
        set RATE1,RATE2, RATE3
        if units consumed =>0 and =<4000
         cost= unit Consumed * rate1
        elif unit Consumed >= 4001 and <= 6000:
         cost= 4000 * rate1 + unit Consumed - 4000 * rate2
        elif unit Consumed > 6000
         cost= 4000 * rate1 + 2000 * rate2 + unitConsumed - 6000 * rate3
    -calculate the payable amount
    -display the formated outputs
    


test plan:
input: accountType= e  accountNumber= 12345  unitConsumed= 3000  output: cost= ERROR: invalid account type. Try again!   
input: accountType= A  accountNumber= 12345  unitConsumed= -2783 output: cost= ERROR: invalid units consumed. Try again!    
input: accountType= a  accountNumber= -12345 unitConsumed= 4500  output: cost= ERROR: invalid account number. Try again!
input: accountType= s  accountNumber= 12345  unitConsumed= 1881  output: cost= 18.810
    
"""
#import exist
from sys import exit

print("-" * 80)
print( "                      Electricity Distribution Company")  #the title
print("-" * 80)

#read accountType and check validity 
accountType= input('Enter account type(S for Government Subsidy, B for Basic, A for Additional): ').upper()
if accountType != 'S' and accountType != 'B' and accountType != 'A':
    exit('ERROR: invalid account type. Try again!')

#read accountNumber and check validity 
accountNumber= input('Enter account number: ')
if not(accountNumber.isdigit()):
    exit('ERROR: invalid account number. Try again!')    
if int(accountNumber)<0:
    exit('ERROR: invalid account number. Try again!')

#read unitconsumed and check validity 
unitConsumed= input('Enter units consumed in KWH: ')
if not(unitConsumed.isdigit()):
    exit('ERROR: invalid units consumed. Try again!')
if int(unitConsumed)<0:
    exit('ERROR: invalid units consumed. Try again!')
else:
    unitConsumed = int(unitConsumed)


#Define
cost=""
RATE1=""
RATE2=""
RATE3=""



#aplaying equation for first company
if accountType == 'S': 
    accountType= 'government Subsidy'
    RATE1= int(10)/1000
    RATE2= int(13)/1000
    RATE3= int(20)/1000
    if unitConsumed >=0 and unitConsumed <=4000:
     cost= unitConsumed * RATE1
    elif unitConsumed >= 4001 and unitConsumed <= 6000:
     cost= (4000 * RATE1) + ( unitConsumed - 4000 ) * RATE2
    elif unitConsumed > 6000:
     cost= (4000 * RATE1) + (2000 * RATE2) + ( unitConsumed - 6000)  * RATE3
     
#aplaying equation for secend company
if accountType == 'B':
    accountType= 'Basic'
    RATE1= int(14)/1000
    RATE2= int(17)/1000
    RATE3= int(30)/1000
    if unitConsumed >=0 and unitConsumed <=4000:
     cost= unitConsumed * RATE1
    elif unitConsumed >= 4001 and unitConsumed <= 6000:
     cost= (4000 * RATE1) + ( unitConsumed - 4000 ) * RATE2
    elif unitConsumed > 6000:
     cost= (4000 * RATE1) + (2000 * RATE2) + ( unitConsumed - 6000)  * RATE3
     
#aplaying equation for third company     
if accountType == 'A':
    accountType= 'Additional'
    RATE1= int(20)/1000
    RATE2= int(25)/1000
    RATE3= int(30)/1000
    if unitConsumed >=0 and unitConsumed <=4000:
     cost= unitConsumed * RATE1
    elif unitConsumed >= 4001 and unitConsumed <= 6000:
     cost= (4000 * RATE1) + ( unitConsumed - 4000 ) * RATE2
    elif unitConsumed >6000:
     cost= (4000 * RATE1) + (2000 * RATE2) + ( unitConsumed - 6000)  * RATE3


#print formated results
print("-" * 80)
print("Account Type   %36s" %accountType )
print('Account Number %36s' %accountNumber)
print('Units Consumed (KWH) %30s' %unitConsumed)
print('Payable Amount (OMR) %30.3f' %cost)
print("-" * 80)





























