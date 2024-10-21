## Global and Local variable

x=15##Global

def func1(y,z):
    global x ##(I wrote this and now x=6 will become global)
    x=6##Local
    y=5
    z=6
    print("In func1: ",x,y,z)

def func2(y,z):
    y=7
    z=8
    print("In func2 before func1 call: ",x,y,z)
    func1(y,z)
    print("In func2 after func1 call",x,y,z)

func2(2,3)

## PYTHON LAB-2
## Ques-01

import math
import cmath ##For handling complex numbers

def root(a,b,c):
    d= (b**2)-4*a*c

    if d>0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("The equation has two real and distinct roots.")
        print("Root1: ",r1)
        print("Root2: ",r2)
    elif d==0:
        print("The roots are real and equal.")
        root=-b/2*a
        print("Root: ",root)
    else:
        print("The roots are complex.")
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("Root1: ",r1)
        print("Root2: ",r2)

##Input from user
a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))

##Ensure that a is not zero.
if a==0:
    print("This is not a quadratic equation,as a cannot be zero.")
else:
    root(a,b,c)

## Ques-02
import math

def findCenterDist(x1,y1,x2,y2):
    D2=(x1-x2)**2+(y1-y2)**2
    return math.sqrt(D2)

def main():
    x1=eval(input("Enter x1: "))
    y1=eval(input("Enter y1: "))
    x2=eval(input("Enter x2: "))
    y2=eval(input("Enter y2: "))
    r1=eval(input("Enter radius of circle1: "))
    r2=eval(input("Enter radius of circle2: "))

    r=findCenterDist(x1,y1,x2,y2)
    if r==r1+r2:
        print("The circles touch externally.")
    elif r>r1+r2:
        print("The circles are completely separate.")
    else:
        print("The circles intersect.")

main() 

## Ques-03
import math

def height(v,theta):
    g=9.8
    # Convert theta from degrees to radians
    theta_rad = math.radians(theta)
    h=((v**2*math.sin(theta_rad)**2)/(2*g))
    return h

def main():
    v=eval(input("Enter initial velocity(m/s): "))
    theta=eval(input("Enter angle of projection(degrees): "))
    h=height(v,theta)
    print("Maximun height reached by the projectile: ",h)

main()

##Ques-04

def complexdiv(a,b,c,d):
    real=(a*c+b*d)/(c**2+d**2)
    imag=(b*c-a*d)/(c**2+d**2)
    print("The result is: ",real,"+",imag,"i")

def main():
    a=eval(input("Enter real part of first complex number: "))
    b=eval(input("Enter complex part of first complex number: "))

    c=eval(input("Enter real part of second complex number: "))
    d=eval(input("Enter complex part of second complex number: "))
    complexdiv(a,b,c,d)

main()

##Ques-05

def totalAmount(p,t,r):
    mr=r/(12*100)
    A=p*(1+mr)**t
    return A
    
def CompoundI(p,t,r):
    mr=r/(12*100)
    A=p*(1+mr)**t
    CI=A-p
    return CI

def main():
    p=int(input("Enter Principal(initial deposit): "))
    r=float(input("Enter annual interest rate(as a percentage): "))
    t=int(input("Enter number of months: "))
    
    total=totalAmount(p,t,r)
    compoundInterest= CompoundI(p,t,r)
    
    print("Interest: ",total)
    print("Compound Interest: ",compoundInterest)
    
main()
