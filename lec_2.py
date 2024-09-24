x1=24
x2=5
y1=x1+x2
y2=x1%x2
print("Sum of ",x1," and ",x2," is ",y1)
print(y2)
##
x=[9,12,3,29,2,10,2,54,67]
print(len(x))
print(x[1])
print(x[3],x[4],x[5])
print(x[3:6])
print(x[:5])  #kahan tak
print(x[3:])  #kahan se
print(x[-2:])
print(x[:-2])
##
x=['Ram',1,2,3,5,7,5,"Iksha"]
print (x.count(5))  #How many 5 are there
x.extend([9,'Sita',3])
print(x)
##
m=[3,9,3]
m.remove(3)
m.remove(3)
print(m)
##
print(1!=0)
##
y=int(input("Enter a number to check if a number is positive or negative "))
if y > 0:
    print(" y is positive")
elif y==0:
    print("y is zero")
else:
    print("y is negative")
##c
age=int(input("Enter your age: "))
citizen=int(input("Enter 1 for indian or 0 for not an indian: "))
if age >= 18 and citizen==1:
    print("You are eligible")
else:
    print("You are not eligible")
