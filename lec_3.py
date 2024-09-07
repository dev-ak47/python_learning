x=[9,12,3,29,2,10,2,54,67]
print(x[1:6:2])  # 2 means it is skipping 1 number in between
print(x[::2])
print(x[::-1])   #-1 means reverse
print(x[::-2])
print(x[-2:])
print(x[:-2])

##

c=int(input('Enter a number:'))
print('The number entered is:',c)

##

print(1 == 0)
print(1!=0)

##

word=input('Enter a word to find if it is palindrome or not:')
if word == word[::-1]:
    print(word,"is a palindrome.")
else:
    print(word,"is not a palindrome.")

#write a python code to check the grade of a student based on their score: if score > 90 then give A,
# If score >80 then give B, for 70 and 60 give C and D, otherwise students is failed, or give F grade

grade=int(input('Enter your marks:'))
if grade>90:
    print('Grade is A')
elif grade>80:
    print('Grade is B')
elif grade>70:
    print('Grade is C')
elif grade>60:
    print('Grade is D')
else:
    print("Student is failed.")
    print("And his grade is F.")

# write a python code to check the type of a triangle. if all sides are equal then say equilateral,
# If any two sides are equal then say isosceles, and if no sides are equal then say scalene triangle.
# Check this also that the sides form a valid triangle.

a1=input("Enter first angle:")
a2=input("Enter second triangle")
a3=input("Enter third triangle")

if a1+a2>a3 or a2+a3>a1 or  a3+a1>a2:
    if a1==a2==a3:
        print('Equilateral Triangle')
    elif a1==a2 or a2==a3 or a3==a1:
        print('Isosceles triangle')
    else:
        print('It is a scalene triangle')
else:
    print('Not a triangle')

#Write a python code that calculate the fare of a taxi ride based on the distance travelled.
# The fare is calculated as follows: for the first 5 km, the fare is 20/-.
# For each additional km 5 to 20, the fare is 3/- per km.
# For distance beyond 20 km, the fare is 2/- per km.

dis=int(input("Enter distance travelled:"))
if dis <= 5:
    print("The fare is 20/-")
elif dis > 5 and dis <= 20:
        print("The fare is",3*(dis-5)+20,'/-')
else:
        print("The fare is",2*(dis-20)+65,'/-')