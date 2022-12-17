
"""
Name: Athir AlAbri
ID: 133358
Section: 21
Problem: to calculating the spectral radiance of a body 
input: Planck, speed of light, Boltzmann, frequency, temperature              
output: Spectral radiance
algorithm:
    1. import math module
    2. set  PLANCKS = 6.62606957*10E-34
    3. set SPEED_OF_LIGHT = 2.99792458*10E8
    4. set BOLTZMANN = 1.3806488*10E-23
    5. from the user read  frequency as float input
    6. from the user read temperature as float input
    7. set the eqaution that calculate the spectral radiance of the body 
    8. print spectralRadiance with 3 decimal places
    
"""

from math import *

#setting constants
PLANCKS = 6.6260695710E-34 
SPEED_OF_LIGHT = 2.9979245810E8
BOLTZMANN = 1.380648810E-23

#setting variables
#input  float frequency value from the user
frequency = float(input("please inter the value of frequency:"))
#input  float temperature value from the user
temperature = float(input("please inter the value of temperature:"))

#calculating the spectral radiance of the body
spectralRadiance= (((2*PLANCKS*frequency**3)/SPEED_OF_LIGHT**2)) * ((1)/(exp((PLANCKS*frequency)/(BOLTZMANN*temperature))-1))

#printing the final value of spectral radiance
print()
print('frequency and temperature:', frequency, temperature)
print()
print('The spectral radiance of the body =', '%.3e'  %(spectralRadiance ))
