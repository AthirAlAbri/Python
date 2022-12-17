# -*- coding: utf-8 -*-
"""

name: Athir AlAbri
ID: 133358
program: program that asks the user to enter a vehicle registration number, then reads the input file
and displays for each provided service on that vehicle, the total duration and the number of visits.
input: num, input file
output: Service,Tot Duration,Nb Visits 
algorithm: 
read num from the user and convert to int
series = num[1]
creat new list newlst = []
try:
   open the file inspection
   for i in file:
    i = i.strip()
    i = i.split("/")
    newlst.append(i)
except FileNotFoundError:
    if there is an error print file not exist

services = {"periodic":[0, 0], "emission":[0, 0],"pre-sale":[0, 0], "other":[0, 0]}
incorrect = 0
correctData = []

for row in newlst:
  if len(row) != 4:
   incorrect += 1

  elif row[2].lower() not in services:
   incorrect += 1
  else:
     try:
         row[0] = int(row[0])
         row[3] = int(row[3])
     except ValueError:
      incorrect += 1
     else:
       correctData.append(row)
       check if row[0] = num  and row[1] = series:
       if row[0] == num and row[1] == series:
           convert row[2] to lower case
          services[key][0] += row[3]
          services[key][1] += 1

print formated output

"""



#read values from the user
num = input("Enter vehicle's registration number: ").split()
num = int(num[0])
series = num[1]


newlst = []
try:
    #open the file
  with open("inspection.txt", "r") as file:

   for i in file:

    i = i.strip()
    i = i.split("/")
    newlst.append(i)

except FileNotFoundError:
    #if there is an error print.......
    print("file not exist!")

services = {"periodic":[0, 0], "emission":[0, 0],"pre-sale":[0, 0], "other":[0, 0]}
incorrect = 0
correctData = []

for row in newlst:
  if len(row) != 4:
   incorrect += 1

  elif row[2].lower() not in services:
   incorrect += 1
  else:
     try:
         row[0] = int(row[0])
         row[3] = int(row[3])
     except ValueError:
      incorrect += 1
     else:
       correctData.append(row)
       #check if values are equal 
       if row[0] == num and row[1] == series:
           #convert to lower case
          key = row[2].lower()
          services[key][0] += row[3]
          services[key][1] += 1

#print formated output
print("=" * 65)
print("{0}{1}{2}".format("Service".ljust(10), "Tot Duration".rjust(15), "Nb Visits ".rjust(15)))
print("=" * 65)

for key, value in services.items():

  print(key.ljust(10) + str(value[0]).rjust(10) + str(value[1]).rjust(15))
print("=" * 50)
print("Number of bad records = ", incorrect)

#close file
file.close()
