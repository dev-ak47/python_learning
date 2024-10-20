##Write a function that takes as parameters the coeffecients a,b, and c of a quadratic equation ax^2+bx+c=0 and finds the solutions of the same.
##Assume that the solutions are real.
##We know that the solutions are given as x= (-b+sqrt(b^2-4ac))/2 and (-b-sqrt(b^2-4ac))/2

import math

def findRootsQE(a,b,c):
    d=math.sqrt(b**2-4*a*c)
    r1=(-b+d)/(2*a)
    r2=(-b-d)/(2*a)
    print("The roots of the QE is given as ",r1,"and",r2)

def main():
    a=eval(input("Enter coefficient a: "))
    b=eval(input("Enter coefficient b: "))
    c=eval(input("Enter coeffecient c: "))
    findRootsQE(a,b,c)

main()

##Let us consider agai our celcius to fahrenheit temperature program

c=int(input("Enter the temperature in centigrade: "))
f=(9/5*c)+32
print("Temperature in fahrenheit is: ",f)

if(f>=90):
    print("Heat warning")
else:
    print("Cold warning")

##How can we enhance this program to print a suitable warning when the temperature is extreme(say over 90 degrees F, it deserves a heat 
##warning,and under 30 degree it deserves a cold warning).

##For the quadratic equation,check whether discriminant b^2-4ac > 0.If yes print the result,else print the result is complex and 
##then print result is same.

import math 

def findRootsQE(a, b, c):
    d = (b**2 - 4*a*c)
    if d >= 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("The roots of the quadratic equation are:", r1, "and", r2)
    else:
        d1 = math.sqrt(abs(d))
        r_real = -b / (2*a)
        r_complex = d1 / (2*a)
        print(f"The roots of the quadratic equation are: {r_real} + {r_complex}i and {r_real} - {r_complex}i")

def main():
    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))
    findRootsQE(a, b, c)

main()
