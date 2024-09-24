#Ask a number from user. Repeatedly divide the number by 2 if it's even or multiply by 3 and add 1 if it's odd.
#The sequence continues untill the number reaches 1.

user=int(input("Enter a number: "))
while user!=1:
    print(user,end=" ")
    if user%2==0:
       user=user/2
    else:
        user=user*3+1
print(user)

#Find mean of the numbers.
sum=0
count=0
mean=0
num=int(input("Enter a number: "))
while num!=0:
    sum=sum+num
    count=count+1;
    mean=sum/count
    num=int(input("Enter a number"))

print("Mean: ",mean)

#Teacher's method of finding mean
numbers=[10,20,30,40,50]
total=sum(numbers)
count=len(numbers)
mean=total/count
print(mean)

##
A=[11,20,30,40,50]
total=sum(A)
count=len(A)
mean=total/count
print(mean)

#Function
def find_mean(numbers):
    total=sum(numbers)
    count=len(numbers)
    mean=total/count
    return mean

A=[10,20,30,40,50]
mean=find_mean(A)
print(mean)

################################
def find_mean(numbers):
    total=sum(numbers)
    count=len(numbers)
    mean=total/count
    return mean

X=input("Enter number giving spaces: ")
Y=X.split()
Z=[]
for y in Y:
    z=float(y)
    Z.append(z)
    ## Z=[float(z) for z in X.split()]
    mean=find_mean(Z)
print(mean)
#######################

import statistics

A=[10,20,30,40,50]
mean=statistics.mean(A)
print(mean)

##############################
A=[10,20,30,40,50]
freq=[1,2,1,4,5]

Af= [ A[i]*freq[i] for i in range(len(A)) ]
mean=sum(Af)/sum(freq)
print(mean)
