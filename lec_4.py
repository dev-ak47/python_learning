# Class = {"Raju":14,"Sahil":15,"Rani":15}
# X = {"Fruit":"Banana","Color":"Blue","Amount":10}
# contacts={"Raju":4367,"Rani":1234}

# print(contacts["Raju"])
# print(contacts.get("Rani"))

# contacts["Raju"]=8790
# print(contacts.get("Raju"))

# #
# grades={"Raju":47,"Rani":98,"Sahil":80}
# grades["Raju"]=96
# print(grades["Raju"])

# For loop
# fruits=["Apple","Banana","Cherry"]
# for fruit in fruits:
#     print(fruit,end=" ")
#     print(fruit," is tasty")

# #
# for i in range(5):
#    print(i**2,end=" ")


# for letter in "Python":
#     print(letter,end=" ")
# print("End")

#
# numbers=[10,20,15,89,45,37,14]
# even=[]
# for i in numbers:
#     if i%2==0:
#         i.append(i)
# print("even no. are:",even)

#
list=[1,2,3,4,5,6,7,8,9,10]
odd_no=[]
for i in list:
    if i%2!=0:
        odd_no.append(i**2)
print(odd_no)
