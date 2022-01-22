# NAME:DAKSH KHANDELWAL
# SID: 21103073
# BRANCH: CSE
# ASSIGNMENT 2


Q1
#given
str="Python is a case sensitive language"

#a
print("A:")
print("length of the string:",len(str))

#b
print("B")
print("Reverse of the string is:","'",str[::-1],"'")

#c
print("C")
#slicing "a case sensitive" having index 9 to 26
new_str=str[slice(9,26)]
print("new string is:","'",new_str,"'") 

#d
print("D")
#repacing "a case sensitive " with "object oriented"
replaced_str=str.replace("a case sensitive","object oriented")
print(replaced_str)

#e
print("E")
#finding index of 'a'
print("Index of 'a' in the given string is:",str.index('a'))

#f
print("F")
#removing the spaces
print(str.replace(" ",""))


Q2
#taking input
Name=input("Enter your name:")
SID=int(input("enter your SID:"))
Department_Name=input("Enter your Department Name:")
CGPA=float(input("Enter your CGPA:"))

#printing output
print("Hey,",Name,"here!\nMy SID is",SID,"\nI am from ",Department_Name,"Department and my CGPA is",CGPA)


Q3
#given
a=56
b=10

#a
print("A")
print("a&b:",a&b)

#b
print("B")
print("a|b:",a|b)

#c
print("C")
print("a^b:",a^b)

#d
print("D")
print("left shift a by 2:",a<<2,"\nleft shift b by 2:",b<<2)

#e
print("E")
print("right shift a by 2:",a>>2,"\nright shift b by 4:",b>>4)


Q4
#taking input
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
num3=float(input("Enter third number: "))

#applying condition for finding greatest number
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

#printing largest number
print("The largest number is:", largest)


Q5
#taking input
str=input("enter the string:")

#applying condition and getting the output
if "name" in str:
    print("Yes")
else:
    print("No")


Q6
#taking input of sides of triangle
side1 = int(input("Enter the value of side a:"))
side2 = int(input("Enter the value of side b:"))
side3 = int(input("Enter the value of side c:"))

#applying condition on the value of sides in order to form a triangle.
#condition : sum of any two sides should be greator than remaining third side.
if side3 < side1+side2 and side2 < side1+side3 and side1 < side2+side3:
    print("Yes")
else:
    print("No")




