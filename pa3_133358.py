"""

Name: Athir AlAbri
ID: 133358
Section: 21
Purpose: The purpose of this assignment is to practice Problem Solving and	Computational
Thinking to	develop a Python solution to the trajectory problem [1]. In	 particular	 the
leverage the use of repetitions and	selection control structures and the Turtle library.
Inputs: 
    m, g, initial_v, V, Cd, dt, x, y, time, y_apix, x_apix, angle
Outputs:
    initial_v, angle, g, Cd, dt, y_apix, x_apix, range
Algorithm:
  - import math and turtle libraries
  - Create turtle instance t
  - initial values:
     m = 2.0, g = 9.8, initial_v = 150, V=150, Cd= 0.005,
     dt= 0.09, x=0, y=0, time=0, y_apix=0, x_apix=0
  - Specify shape, pensize, fillcolor
  - loop to draw the counter(4)
  - print the header in formated way
  - read angle and validate it
  - convert angle to radians
  - put the ball in the firts position (0,0)
  - print initial x and y
  - vx= V*cos(angle)
  - vy= V*cos(angle)
  - loop to update
    while flag true:
        fd=Cd*V^2
        ax=-fd*cos(angle)/m
        ay=-g-(fd*sin(angle))/m
        vx= vx+ax*dt
        vy= vy+ay*dt
        V= sqrt(vx^2+vy^2)
        x= x+vx*dt
        y= y+vy*dt
        time= time+dt
        t go to x, y
        if y>0 print x and y   else.. flag= false
        if y > y_apix... y_apix= y , x_apix= x
   - t go to x_apix
   - t go to y_apix
   - print formated output
   - turtle.done()
   


Test plan:
##################################################
WELCOME TO THE PROJECTILE TRAJECTORY SIMULATOR
##################################################
1. Enter the angle (20-60) in degrees: 10
Invalid hit force's angle!
2.Enter the angle (20-60) in degrees:80
Invalid hit force's angle!
3.
x y
0 0
6.522187500000001 11.217380126490637
12.833914316640822 21.990851656407507
18.950759153014353 32.3473976950218
......
411.82390740920954 26.98045140429184
412.68723878905774 17.997625217957456
413.4487745346993 8.759103821188447

Initial velocity:  150 [m/s]
Angle:  60.0 [degrees]
Acceleration due to gravity  9.800 (m/s^2)
Drag coefficient:  0.005
Time step in  0.090 [s]

The apex position coordinates are:
x_apex = 256.566 , y_apex = 274.115
The range is = 414.103

"""
from math import *
import turtle
t = turtle.Turtle()

# initial varibles and constants
M = 2.0
g = 9.8  #gravity
initial_v = 150
V = initial_v
Cd = 0.005
dt = 0.09
x = 0
y = 0  #velocity
time = 0
y_apix = 0
x_apix = 0


# drawing the contour
t.pensize(5)
t.fillcolor("cyan")
t.begin_fill()
for i in range(1, 5):
    if i % 2 != 0:
        t.forward(2 * 300)
        t.left(90)
    else:
        t.forward(300)
        t.left(90)
t.end_fill()

# program header
print('#' * 50)
print("WELCOME TO THE PROJECTILE TRAJECTORY SIMULATOR")
print('#' * 50)

# ask user to input angle between 20 and 60
angle = int(input("Enter the angle (20-60) in degrees:"))
# keep asking the user if the angle outside range
while angle < 20 or angle > 60:
    print("Invalid hit force's angle!")
    angle = int(input("Enter the angle (20-60) in degrees:"))
angle = radians(angle)  # convert angle to rad

# start drawing
t.fillcolor("black")
t.shape("circle")
t.pensize(5)

t.goto(x, y)
t.stamp()
# starting point
print()
print("x", "y")
print(x, y)

# magnitude	of	velocity
vx = V * cos(angle)
vy = V * sin(angle)

# loop to update laws
flage = False
while not flage:
    fd = Cd * V ** 2  # air resistance	drag force
    ax = -(fd * cos(angle)) / M  # a means acceleration
    ay = -g - (fd * sin(angle)) / M
    vx = vx + ax * dt
    vy = vy + ay * dt
    V = sqrt(vx ** 2 + vy ** 2)
    x = x + vx * dt
    y = y + vy * dt
    time = time + dt
    t.shape("circle")
    t.goto(x, y)

    if y > 0:
        print(x, y)
    else:
        flage = True  # stop the loop
    # find y apix and x apix
    if y > y_apix:
        y_apix = y
        x_apix = x

# draw the y and x apix
t.stamp()
t.hideturtle()
t.pensize(1)
t.color("blue")
t.goto(x_apix, 0)
t.goto(x_apix,y_apix)
t.goto(0,y_apix)


# print formated outputs
print()
print("Initial velocity: ", initial_v, "[m/s]")
print("Angle: ", "%.1f" % (degrees(angle)), "[degrees]")
print("Acceleration due to gravity ", "%.3f" % g, "(m/s^2)")
print("Drag coefficient: ", Cd)
print("Time step in ", "%.3f" % dt, "[s]")

print()
print("The apex position coordinates are:")
print("x_apex =", "%.3f" % x_apix, ",", "y_apex =", "%.3f" % y_apix)
print("The range is =", "%.3f" % x)  # range=final x- initial x (initial x=0)

turtle.done()    
    
    
    
    
    
    
    
    