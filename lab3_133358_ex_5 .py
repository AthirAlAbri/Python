# -*- coding: utf-8 -*-
"""
Name: Athir AlAbri
ID: 133358
Problem: to calculate and display the total sales, the VAT (Value Added Tax) and the net price ,
for given number of units sold and unit price.
input: numOfItem, unitPrice      
output: totalSales, VAT, netPrice 
algorithm:
    1. from the user read  numOfItem and print it
    2. from the user read unitPrice and print it 
    3. find totalSales = numOfItem * unitPrice
    4. find VAT= 9/100 * totalSales
    5. find netPrice= totalSales-VAT
    6. print the output table in formatted way

"""

numOfItem= int(input("please enter the number of items sold?"))
print(numOfItem)
unitPrice= float(input("please enter the unit price?"))
print(unitPrice)

totalSales = numOfItem * unitPrice
VAT= 9/100 * totalSales #VAT(Value Added Tax)
netPrice= totalSales-VAT

print("*"*80)
print("%-15s %-15s %-15s %-15s %-15s" %("Unit","Number of","Total","VAT","Net Price"))
print("%-15s %-15s %-15s" %("Price", "Items", "Sales"))
print("*"*80)
print("%-15.3f %-15.0f %-15.3f %-15.3f %-15.3f" % (unitPrice, numOfItem, totalSales, VAT, netPrice))
print("*"*80)



