'''
marks=int(input("enter marks"))
if marks >= 0 and marks <= 100 :
    if marks < 60:
        print(" fail")
    if marks >= 60 and marks <70:
        print("grade d")
    if marks >= 70 and marks <80 :
        print("grade c")
    if marks >= 80 and marks< 90:
        print("grade b")
    if marks >= 90 :#and marks <= 100:
        print("grade a")
else :
    print("invalid marks entry")
'''
#elif -> if - elif - else ( multiple conditions )
''' syntax
if <condition 1>:
    statements
elif <condition2>:
    statements
elif <condition3>:
    statements
else:
    statements

marks= int(input("enter the marks"))
if marks >= 0 and marks < 60:
        print(" fail")
elif marks >= 60 and marks <70:
        print("grade d")
elif marks >= 70 and marks <80 :
        print("grade c")
elif marks >= 80 and marks< 90:
        print("grade b")
elif marks >= 90 and marks <= 100:
        print("grade a")
else :
    print("invalid marks entry")

#age eligibility
age=int(input("enter age"))
if age >=18 and age<=100:
    print("access granted")
elif age <18 and age >0:
    print(" not eliguble, need to wait", 18-age,"years")
else:
    print("not valid values")
'''
#output formatting --> presenting the output format in the console
'''
1. old style formatting( using commas )
2. % usage (%f,%d), .format() usage , fstring function

name = " nani" ; batch="DA" # ; is used to declare multiple variables in single line
print(name,batch) #op--> nani DA ( by default sep is having space)
print(name, batch,sep='<<<>>>') # sep is used to tell how to seperate the values
# new line = '\n'  tab space= '\t'
print(name,batch,end='\t')  # end is used to merge the two print values
print (7,5)  #op---> nani DA      7 5 ( new line print values are concatinated with tab space)
print(name,batch,end='')
print(10,3)   #op---> nani DA 10 3 (added with space)


# usage of commas
name='nani'
place='hyd'
print(name," is in ",place) #op---> nani is in hyd  ( message and variables are seperated by the commas)

#%d--->integer, %s---> string, %f--->float
salary=25000
print("my salary is %d"%salary) # retrive the value of salary and print at place of %d
salary=2345.678
print("my salary is %d"%salary) # remove the decimal part
print("nani salary is %f"%salary) # print all decimal part
print("sheshi salary is %.1f",%salary)  # round of to 1 digit decimal part op--> 2345.7
# we can use .f, .1f, .2f, .3f and so on to round off the decimal part with number of decimals

# .format()
print("{} is in {}".format(name,place)) #order should be followed   op---> nani is in hyd

#fstring usage
print(f'{name} is in {place}') # variable is called in the {}

----------------------------------------

#even or odd
val=int(input("enter value"))
if val%2 == 0:
    print("even")
else:
    print("odd")

#credentials match
usrn="harshu"
pwd="n2004"
username=input("enter username")
password=input("enter password")
if username == usrn and password== pwd:
    print("correct credentials")
else:
    print("incorrect credentials")

# +ve or -ve
numb=int(input("enter value"))
if numb>0:
    print("positive")
elif numb<0:
    print("negative")
else:
    print(" value is zero")

#atm min balance
minimum=500
balance=700
wdrw=int(input("enter with draw amount"))
if balance > minimum and (balance-wdrw)> minimum:
    balance=balance-wdrw
    print("your balance amount is",balance)
else:
    print("withdrawal impossible")
    
#vowels in name
name=input("enter name")
vowels = ['a','e','i','o','u']
for i in name:
    if i in vowels:
        print(i)

#vowels using if
val=input("enter alphabet")
if val in ['a','e','i','o','u']:
    print(val,"is vowel")
else:
    print(val,"is consonant")

----------------------------------------------------

Task-2 "even odd checker"

val=int(input("enter value"))
if val>0 and val%2 == 0:
    print("Even Number")
elif val>0 and val%2 != 0:
    print("Odd Number")
elif val<0 and val%2==0:
    print("Negative Even Number")
elif val<0 and val%2!=0:
    print("Negative Odd Number")
else:
    print("Zero is neither even nor odd")

-------------------------------------------
Task 3: "season checker"

month=int(input("Enter month number from 1-12"))
if month in [12,1,2]:
    print("Winter")
elif month in [3,4,5]:
    print ("Spring")
elif month in [6,7,8]:
    print("Summer")
elif month in [9,10,11]:
    print("Autumn")
else:
    print("Invalid month entered")

-------------------------------------------
'''






































    
