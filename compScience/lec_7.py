## CLASS PROGRAMS
## Finding max of 3 numbers(integers)

def findMax(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    else:
        if y>z:
            return y
        else:
            return z
        
def main():
    x=eval(input("Enter x: "))
    y=eval(input("Enter y: "))
    z=eval(input("Enter z: "))
    max=findMax(x,y,z)
    print("Max is: ",max)

# main()

## SIMPLE METHOD
def main():
    x=eval(input("Enter x: "))
    y=eval(input("Enter y: "))
    z=eval(input("Enter z: "))
    m=max(x,y,z)
    print("Max is: ",m)

main()

## ANOTHER METHOD
def findMax(x,y,z):
    if (x>y) and (x>z):
        return x
    elif (y>x) and (y>z):
        return y
    else:
        return z
    
def main():
    x=eval(input("Enter x: "))
    y=eval(input("Enter y: "))
    z=eval(input("Enter z: "))
    max=findMax(x,y,z)
    print("Max is: ",max)

main()