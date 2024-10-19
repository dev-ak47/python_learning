##Lab Assignment-1 problems
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

##Lab Assignment-2 problems
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the average: "))

x=(c*3)-(a+b)
print("The third number is ",x)

## Lab Assignment-3 
tInMin=int(input("Enter minutes to convert it into hours and minutes: "))
hrs=tInMin//60
min=tInMin%60
print("The time in ",tInMin,"minutes is equivalent to",hrs,"hours and",min,"minutes.")

##Lab Assignment-4
r=int(input("Enter radius: "))
area=2*3.14*(r*r)
perimeter=2*3.14*r
print("Area and Perimeter of circle is ",area,"and",perimeter)

##Lab Assignment-5
u=float(input("Enter initial velocity: "))
a=float(input("Enter acceleration: "))
t=int(input("Enter time: "))
s=u*t+1/2*a*(t*t)
print("The distance is: ",s)

##Lab Assignmnet-6
c=int(input("Enter the temperature in centigrade: "))
f=(9/5*c)+32
print("Temperature in fahrenheit is: ",f)