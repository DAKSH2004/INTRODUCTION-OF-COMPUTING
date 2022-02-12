# NAME:DAKSH KHANDELWAL
# SID: 21103073
#BRANCH: CSE
# ASSIGNMENT 3

Q1:

print("Q1")
#taking input

str=input("enter the string:" )

#checking if str is just a word or not

if " " in str:
	print(-1)
	
else:
	#counting alphabets

	counts=dict()
	words=list(str)

	for word in words:
		if word in counts:
			counts[word]+=1
		else:
			counts[word]=1

	#printing output
	print(counts)


Q2:

print("Q2")
def Next_Date():
    list1=[1,3,5,7,8] #months with 31 days
    list2=[4,6,9,11] # months with 30 days
    list3=[2] # days wary from 28 to 29 during leap year
    list4=[12] #month after the month cycle returns to 1
    
    #while loop is used so that if any wrong value is entered  then values will be entered again
    while(True):                
        day=int(input("ENTER THE DAY: "))
        if(1<=day<=31):
            break
        else:
            print("Please Enter a valid day")
    #while loop is used so that if any wrong value is entered  then values will be entered again        
    while(True):                 
        month=int(input("ENTER THE MONTH OF THE YEAR: "))
        if(1<=month<=12):
            break
        else:
            print("Please Enter a valid month")
    #while loop is used so that if any wrong value is entered  then values will be entered agaign        
    while(True):                
        year=int(input("ENTER THE YEAR: "))
        if(1800<=year<=2025):
            break
        else:
            print("Please Enter year from 1800 to 2025 only")
    if month in list1 :    
        if(day==31):
            day=1
            month=month+1
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
    
    elif month in list2 :
        if(day==30):
            day=1
            month=month+1  
            print(day,"/",month,"/",year)   
        elif(day<30):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN") 
            Next_Date()      
    elif month in list3:
        if(year % 4 == 0):  # condition for leap year
            if(day==29):
                day=1
                month=month+1
                print(day,"/",month,"/",year)
            elif(day<29):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
        else:
            if(day==28):
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif(day<28):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
    elif month in list4:
        if(day==31):
            day=1
            month=1
            year+=1  
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1;
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
        
    else:
        print("INVALID DATE TRY AGAIN")
        Next_Date()
Next_Date()


Q3:

print("Q3")
#taking input

input_list=input('Enter elements of list seperated by spaces: ')
new_list=input_list.split()

# printing the entered list

print('list: ',new_list)

# converting each items in integer

for i in range(len(new_list)):
	new_list[i]=int(new_list[i])

#getting the resultant squared tupple

sq_list=[(new_list[i],new_list[i]**2) for i in range(len(new_list))]  

#printing the result

print('The Resultant tuple is:')
print(sq_list)


Q4:

print("Q4")
def input_num():
	number=int(input("Enter the grade points: "))

	#checking the condition on the grade points

	if number>10 or number<4:
		print("Invalid input, Try Again")
		input_num()
	return number
grade=input_num()

#pocessing input and printing output

if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")


Q5:

print("Q5")
#taking input

n=int(input("no of times pattern to be formed:",))

#taking a random number which is equal to the input number
      
p=n

#performing operation to get output      
for i in range(n):
    for j in range(0,i):
        print(' ', end="")
    for k in range(0,2*p -1):
        #ascii value of A=65,B=66 and so on..
        print(chr(65+ k),end="")
    p=p-1
# for line break    
    print()
    

Q6:

print("Q6")
# Taking input

sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

# asking the user whether to enter another student entry

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

# A) print the dictionary
print("A)",students)

# B) sort acc to the names
print("B)",sorted(students.items(),key =lambda kv:(kv[1], kv[0]))) 

# C) sort acc to the SIDs
print("C)",{k:v for k,v in sorted(students.items())})

# D) search for a student by their SID
sid = int(input("Search Name with SID: "))
print("D)",students[sid])


Q7:

print("Q7")
# solving using recursion
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

#taking input
    
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))

# Check if the number of terms is valid
 
if no_of_terms <= 0:    
   print("Plese enter a positive integer")
else:
    #printing fibonacci sequence
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
       
#taking average of the fibonacci sequence

avg=float(sum/no_of_terms)
print("AVERAGE OF RESULTANT FIBONACCI SERIES IS",avg)


Q8:

print("Q8")
#information given

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# A)

Union_Sets = Set1.union(Set2)
Intersection_Sets = Set1.intersection(Set2)
SetA = Union_Sets-Intersection_Sets
print(SetA)

#B)

SetB = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print(SetB)

#C)

SetC = ((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print(SetC)

#D)

SetD = set()
for i in range(1, 11):
    if i not in Set1:
        SetD.add(i)
print(SetD)

#E)

SetE = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        SetE.add(i)
print(SetE)

		
		

