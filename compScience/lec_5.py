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