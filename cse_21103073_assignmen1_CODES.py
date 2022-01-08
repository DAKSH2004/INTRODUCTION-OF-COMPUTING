# NAME:DAKSH KHANDELWAL
# SID: 21103073
#BRANCH: CSE
# ASSIGNMENT 1

Q1:
#taking input
num1=int(input("enter the value of num1: "))
num2=int(input("enter the value of num2: "))
num3=int(input("enter the value of num3: "))
#taking average
avg=(num1+num2+num3)/3
#printing output
print("the average is: ",avg)


Q2

#taking input
#all values are in dollars

gross_income=float(input("enter the gross income: "))
no_of_dependents=int(input("enter the no. of dependents: "))

#there is an extra 3000 deduction for each dependents
dependent_deduction=3000

#information given
standard_deduction=10000

#tax rate=20%

#finding taxable income
taxable_income=((gross_income)-(standard_deduction)-(dependent_deduction*no_of_dependents))

#finding tax
tax=(taxable_income*20)/100

#printing output
print("taxable income: ",taxable_income)
print("tax: ",tax)


Q3
student=["SID","Name","Gender","Course Name","CGPA"]

#taking input
SID=int(input("Enter student id: "))
Name=input("Enter name: ")
Gender=input("Enter gender: ")
Course_Name=input("Enter the name of the course: ")
CGPA=float(input("Enter the cgpa: "))

#let the input value be stored in a list name data
data=[SID,Name,Gender,Course_Name,CGPA]

#printing output
print(student)
print(data)


Q4
#taking input
student_1_marks=int (input("Enter the student 1 marks: "))
student_2_marks=int (input("Enter the student 2 marks: "))
student_3_marks=int (input("Enter the student 3 marks: "))
student_4_marks=int (input("Enter the student 4 marks: "))
student_5_marks=int (input("Enter the student 5 marks: "))

#storing the marks int list
marks=[student_1_marks,student_2_marks,student_3_marks,student_4_marks,student_5_marks]

#printing output
print("list: ")
print(marks)

#sorted list
print("sorted list: ")
print(sorted(marks))


Q5(A)
#(a)
#information given
list=['Red','Green','White','Black','Pink','Yellow']

#printing list
print("list: ")
print(list)

#getting the 4th term
print("The 4th term is: ",list.pop(3))

#printing the list without the 4th term
print("After removing the 4th term new list: ")
print(list)

(B)
#(b)
#information given
list=['Red','Green','White','Black','Pink','Yellow']

#printing list
print("list: ")
print(list)

#removing 'Black(4th place)' and 'Pink(5th place)' from the list and replacing it with 'Purple'
list[3:5]=['Purple']

#printing required output
print("new list after removing and replacing: ")
print(list)



