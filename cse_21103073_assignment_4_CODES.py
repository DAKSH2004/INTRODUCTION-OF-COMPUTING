# NAME:DAKSH KHANDELWAL
# SID: 21103073
#BRANCH: CSE
# ASSIGNMENT 4

# Q1:
print("Q1:")

def towerofhanoi(n,initial,destination,between):
	if n==1:
		print("move disk 1 from",initial,"to destination",destination)
		return 
	else:
		towerofhanoi(n-1,initial,destination,between)
		print("move disk",n,"from",initial,"to destination",destination)
		towerofhanoi(n-1,between,destination,initial)
n=3
towerofhanoi(n,'a','b','c')
print()

# Q2:
print("Q2:")

#using loops

import math

n=int(input("enter the no of rows: "))

print("using loops")

for i in range(n):
	for j in range(n-i+1):
                # for spaces
		print(" ",end="")

	for j in range(i+1):
                # ncr=n!/(r)!*(n-r)! combination formula
		print(math.factorial(i)//((math.factorial(j))*(math.factorial(i-j))),end=" ")

	print()	



#using recurssion
print("using recurssion")


def pascaltriangle(n,len=n):
    if n == 0:
        return
    pascaltriangle(n-1,len)
    #printing the spaces
    print('  '*(len-n), end='')

    # first number is always 1
    ini = 1
    for i in range(1, n+1):

        print(ini, end ='   ')
        
        # using Binomial Coefficient
        ini = ini * (n - i) // i
    print()
pascaltriangle(n)
print()

# Q3:
print("Q3:")

a=int(input("enter the 1st number: "))
b=int(input("enter the 2nd number: "))

Quotient=a//b
Remainder=a%b

# part a
print("a)")

print("checking caliability")
print(callable(Quotient))
print(callable(Remainder))

# part b
print("b)")

if(Remainder==0):
	print("remainder is 0")
if(Quotient==0):
	print("quotient is 0")
if(Remainder!=0 and Quotient!=0):
	print("both remainder and quotient are non zero")

# part c
print("c)")

list_c=[Remainder+4, Quotient+4, Remainder+5, Quotient+5,Remainder+6, Quotient+6]

result=[]
for i in range(len(list_c)):
	if list_c[i]>4:
		result.append(list_c[i])# append function is used to a number to the list
print(f"number that are greator than 4 int the list is: {result} ")

# part d
print("d)")

set_result=set(result)
print(set_result)

# part e
print("e)")

# frozen set is used to make set immutable
immutable_set=frozenset(set_result)
print("immutable set is: ",immutable_set)

# part f
print("f)")

print("maximum value: ",max(immutable_set))
# hash function is used to find hash value 
print("hash value of the max value of the above set is: ",hash(max(immutable_set)))
print()

# Q4:
print("Q4:")

class Student:
	def __init__(self,student,rollno):
		self.name=student
		self.rollno=rollno

	def __del__(self):
		print("object is destroyed")

# creating object

stud1=Student("rakesh",1234)
print("object is created")

print(f"students's name {stud1.name} and sid is {stud1.rollno}.")

# deleting object

del stud1
print()

# Q5:
print("Q5:")

class Employee:
	def __init__(self,employee_name,employee_salary):
		self.name=employee_name
		self.salary=employee_salary

# creating records of the employee

employee_1=Employee("mehak",40000)
employee_2=Employee("ashok",50000)
employee_3=Employee("viren",60000)

# part a
print("a)")

# updating employee_1 salary

employee_1.salary=70000
print(f"updated salary of {employee_1.name} is {employee_1.salary}.")


# part b
print("b)")

# deleting record of employee viren

print("record of viren deleted")
del employee_3
print()

# Q6:
print("Q6:")

a_word=input("enter a word: ")

word_test=input("enter a new word which has meaning using the the same letter to test friendship: ")

def new_dict_count(a_word):
	count={}
	listy=list(a_word)
	
	a=len(listy)
	for i in range(a):
		if listy[i] in count:
			count[listy[i]]+=1
		else:
			count[listy[i]]=1
	return count

# shopkeeper checks for friendship
def impi():
	if new_dict_count(a_word)!=new_dict_count(word_test):
		print("the friendship is fake as letters are different")
		return 
	
	user=input("check whether the formed word have a meaning(y/Y or n/N):")
	
	if user=='y' or user=='Y':
		print("friendship is real and friend passes the test")
	elif user=='n' or user=='N':
		print("frienship is fake and friend fails the test")
	else:
		print("invalid input,try again")
		impi()
impi()








       




