##Function

def hello():
    print("Hello World")
    print("Programming is fun.")

hello()

#Parameters of a function
#Suppose a program takes as input a user name and prints a personalized welcome note
#Welcome Jay
#Programming is fun
#We will use a function to print the welcome note

name=input("Enter your name: ")
print("Welcome",name)
print("Programming is fun!!")

##Function

def welcomeprint(name):
    print("Welcome",name)
    print("Programming is fun!!")

a=input("Enter your name: ")
welcomeprint(a)

##Write a function named,find_sum() that takes 2 integers as arguments and prints the sum of integers

def find_sum(a,b):
    sum=a+b
    print("The sum is: ",sum)

a=int(input("Enter first no.: "))
b=int(input("Enter  second no.: "))
find_sum(a,b)

##Write a function that multiplies two numbers

def find_mul(a,b):
    mul=a*b
    print("Multiple: ",mul)

a=int(input("Enter first no.: "))
b=int(input("Enter second no.: "))
find_mul(a,b)

##Find the area and perimeter of rectangle

def rect(l,w):
    a=l*w
    p=2*(l+w)
    print("Area: ",a)
    print("Perimeter: ",p)

l=int(input("Enter length: "))
w=int(input("Enter width: "))
rect(l,w)

##Suppose the user wants to extend the code so that the area and perimeter is calculated for different shapes depending upon the choice 
##of the shape,which is provided by the user.

def rect():
    l=int(input("Enter length: "))
    w=int(input("Enter width: "))
    a=l*w
    p=2*(l+w)
    print("Area of the rectangle is: ",a)
    print("Perimeter of the rectangle is: ",p)

def circle():
    rad=int(input("Enter the radius of the circle: "))
    area=22/7*(rad**2)
    circumference=2*22/7*rad
    print("Area of the circle is: ",area)
    print("Circumference of the circle is: ",circumference)

choice=input("Enter the shape whose area and perimeter to be calculated(Enter R for rectangle or C for circle): ")
if choice=="R":
    rect()
else:
    circle()

##Local and Global variables
xg=100

def func(x,y):
    z=4
    print(x,y,z,xg)

func(2,3)
print(xg)


xg=100 #(Global variable)

def func(x,y):
    z=4 #(Local variable)
    #global xg (Then it will be global and value will change in another function also)
    xg=20 #(Local variable)
    print(x,y,z,xg)

func(2,3)
print(xg)

##Getting results from a function.Suppose we want a function to calculate the square of a number and return the result to the calling 
##function so that it can be used there.

def find_sq(x):
    sq=x**2
    return sq

x1=5
result=find_sq(x1)
print("The square of",x1,"is",result)