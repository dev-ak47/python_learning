# def findAvg(n):
#     sum=0
#     for i in range(n):
#         a=eval(input("Enter number: "))
#         sum+=a
#     avg=sum/n
#     return avg
    
# def main():
#         n=int(input("Enter the number of elements whose average is to be calculated: "))
#         avg=findAvg(n)
#         print("The average of",n,"given numbers is: ",avg)

# main()

##The objective is to print the odd numbers from 0 to n, where n is input by the user.

# def findOdd(n):
#     for i in range(n+1):
#         if i%2!=0:
#             print(i,end=" ")

# def main():
#     n=int(input("Enter the ending number: "))
#     findOdd(n)
# main()

##Suppose you want to print the odd numbers from 1 to n inclusive,where n is input by the user.

# def findOdd1(n):
#     for i in range(n+1):
#         if i<5:
#             pass ##It will simply pass and do nothing.
#         else:
#             if i%2==1:
#                 print(i,end=" ")


# def main():
#     n=int(input("Enter the ending number: "))
#     findOdd1(n)
# main()

##Do the same thing without using the pass
# def printOdd2(s,n):
#     for i in range(s,n+1):
#         if i%2==1:
#             print(i,end=" ")

# def main():
#     s=int(input("Enter the starting number: "))
#     n=int(input("Enter the ending number: "))
#     printOdd2(s,n)

# main()

##Changing stepsize in range() function 
def printOdd3(s,n):
    step=2
    for i in range(s,n+1,step):
        print(i,end=" ")

def main():
    s=int(input("Enter the starting number: "))
    n=int(input("Enter the ending number: "))
    printOdd3()

main()