# NAME:DAKSH KHANDELWAL
# SID: 21103073
# BRANCH: CSE
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
def NextDate():
    list_1=[1,3,5,7,8] #months with 31 days
    list_2=[4,6,9,11] # months with 30 days
    list_3=[2] # days wary from 28 to 29 during leap year
    list_4=[12] #month after the month cycle returns to 1
    
    #while loop is used so that if any wrong value is entered  then values will be entered again
    while(True):                
        Day=int(input("ENTER THE Day: "))
        if(1<=Day<=31):
            break
        else:
            print("Please Enter a valid Day")
    #while loop is used so that if any wrong value is entered  then values will be entered again        
    while(True):                 
        Month=int(input("ENTER THE MONTH OF THE YEAR: "))
        if(1<=Month<=12):
            break
        else:
            print("Please Enter a valid Month")
    #while loop is used so that if any wrong value is entered  then values will be entered agaign        
    while(True):                
        Year=int(input("ENTER THE YEAR: "))
        if(1800<=Year<=2025):
            break
        else:
            print("Please Enter Year from 1800 to 2025 only")
    if Month in list_1 :    
        if(Day==31):
            Day=1
            Month=Month+1
            print(Day,"/",Month,"/",Year)
        elif(Day<31):
            Day=Day+1
            print(Day,"/",Month,"/",Year)
        else:
            print("INVALID DATE TRY AGAIN")
            NextDate()
    
    elif Month in list_2 :
        if(Day==30):
            Day=1
            Month=Month+1  
            print(Day,"/",Month,"/",Year)   
        elif(Day<30):
            Day=Day+1
            print(Day,"/",Month,"/",Year)
        else:
            print("INVALID DATE TRY AGAIN") 
            NextDate()      
    elif Month in list_3:
        if(Year % 4 == 0):  # condition for leap year
            if(Day==29):
                Day=1
                Month=Month+1
                print(Day,"/",Month,"/",Year)
            elif(Day<29):
                Day+=1
                print(Day,"/",Month,"/",Year)
            else:
                print("INVALID DATE TRY AGAIN")
                NextDate()
        else:
            if(Day==28):
                Day=1
                Month=Month+1
                print(Day,"/",Month,"/",Year)
            elif(Day<28):
                Day=Day+1
                print(Day,"/",Month,"/",Year)
            else:
                print("INVALID DATE TRY AGAIN")
                NextDate()
    elif Month in list_4:
        if(Day==31):
            Day=1
            Month=1
            Year=Year+1  
            print(Day,"/",Month,"/",Year)
        elif(Day<31):
            Day=Day+1
            print(Day,"/",Month,"/",Year)
        else:
            print("INVALID DATE TRY AGAIN")
            NextDate()
        
    else:
        print("INVALID DATE TRY AGAIN")
        NextDate()
NextDate()


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
    print("your grade is 'D' and poor performance")
elif(grade==5):
    print("your grade is 'C' and Below Average performance")
elif(grade==6):
    print("your grade is 'C+' and Average performance")
elif(grade==7):
    print("your grade is 'B' and Good performance")
elif(grade==8):
    print("your grade is 'B+' and Very Good performance")
elif(grade==9):
    print("your grade is 'A' and Excellent performance")
else:
    print("your grade is 'A+' and outstanding performance")


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

Sid = int(input("Enter SID: "))
Name = input("Enter Name: ")
Student = {Sid:Name}

# asking the user whether to enter another student entry

while True:
    choice = input("Do you want to enter another student entry(Y or N):").upper()
    if choice == 'Y':
        Sid = int(input("Enter SID: "))
        Name = input("Enter Name: ")
        Student[Sid] = Name
    elif choice == 'N':
        break
    else:
        print('Invalid input!')

# A) print the dictionary
print("A)")
print(Student)

# B) sorting according to the names
print("B)")
print(sorted(Student.items(),key =lambda kv:(kv[1], kv[0]))) 

# C) sorting according to the SIDs
print("c)")
print({k:v for k,v in sorted(Student.items())})

# D) searching for a student by their SID
print("D)")
Sid = int(input("Search Name with SID: "))
print(Student[Sid])


Q7:

print("Q7")
# solving using recursion
def reccr_fibona(n):
   if n <= 1:
       return n
   else:
       return(reccr_fibona(n-1) + reccr_fibona(n-2))

#taking input
    
Terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))

# Check if the number of terms is valid
 
if Terms <= 0:    
   print("Enter a positive integer")
else:
   #printing fibonacci sequence
   print("Fibonacci sequence:")
   sum=0
   for k in range(Terms):
       print(reccr_fibona(k))
       sum=sum+reccr_fibona(k)
       
#taking average of the fibonacci sequence

avge=float(sum/Terms)
print("AVERAGE OF RESULTANT FIBONACCI SERIES IS",avge)


Q8:

print("Q8")
#information given

Set_1 = {1, 2, 3, 4, 5}
Set_2 = {2, 4, 6, 8}
Set_3 = {1, 5, 9, 13, 17}

# A)
print("A)")
Union_Sets = Set_1.union(Set_2)
Intersection_Sets = Set_1.intersection(Set_2)
SetA = Union_Sets-Intersection_Sets
print(SetA)

#B)
print("B)")
SetB = Set_1.union(Set_2.union(Set_3)) - Set_1.intersection(Set_2) - Set_2.intersection(Set_3) - Set_3.intersection(Set_1)
print(SetB)

#C)
print("C)")
SetC = ((Set_1.intersection(Set_2)).union((Set_1.intersection(Set_3)).union(Set_2.intersection(Set_3))))-(Set_1.intersection(Set_2.intersection(Set_3)))
print(SetC)

#D)
print("D)")
SetD = set()
for i in range(1, 11):
    if i not in Set_1:
        SetD.add(i)
print(SetD)

#E)
print("E)")
SetE = set()
for i in range(1, 11):
    if i not in Set_1 and i not in Set_2 and i not in Set_3:
        SetE.add(i)
print(SetE)
