print("Hello")
x=2
print(x)
x=2.5
print(x)

###################
x=eval(input("Enter the first number: "))
y=eval(input("Enter the second number: "))
print(x+y)
print(type(x))

##################
# Conversion rules
# int --> float
# int --> string
# str --> float //Not all strings can be converted
# str --> int //Not all strings can be converted
# float --> int //Data loss may happen
# float --> str 

# Simultaneous assignment
x,y=2,3
# print(x)
# print(y)
x,y=y,x
print(x)
print(y)