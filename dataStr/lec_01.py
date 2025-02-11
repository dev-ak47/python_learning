# Function: It is reusable blocks of code that perform specific task.

# def --- Keyword to define a function. Then, Function name, then parameters(official), function body

# def add(a,b):
#   return a+b

# print(add(5,10))

# def pow(a,b):
#   power=1
#   for i in range(abs(b)):
#     power*=a
#   return power
# print(pow(2,4))

#Write a program for factorial n.
# def fact(m):
#   factorial=1
#   for i in range(1,m+1):
#     factorial*=i
#   return factorial
# fact(6)

## Default Argument: It is a parameter that assumes default value if a value is not
## provided in the function call for that argument

## Keyword Arguments The idea is to allow the caller to specify the argument name 
## with values so that no need to remember the order of the parameter

# def student(firstname, lastname):
#   print(firstname, lastname)

# student(lastname ="Kumar",firstname= "Priyanshu")

def mydetail(name,age):
  print("I am", name)
  print("My age is",age)
mydetail("Akanksha",19)
