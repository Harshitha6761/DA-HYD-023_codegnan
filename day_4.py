#identity operators
'''
x = 5
y = 5
z = 10
print(x is y)  # True
print(x is z)  # False
print(x==z)  # False
print(x is not z)  # True
a =[ 1, 2, 3]
b =[ 1, 2, 3]
print(a is b)  # False
print(a is not b)  # True
print(a == b)  # True
#bitwise operators -> we perform bitwise operations over operands
#numbers will be converted into binary format and then the bitwise operations are performed
# & (and) 
# | (or)
# ^ (xor)
# ~ (not)
# << (left shift)
# >> (right shift)
5 & 3  # 1
5 | 3  # 7
5 ^ 3  # 6
~5     # -6
5 << 1 # 10
5 >> 1 # 2
5 and 3  # 1
5 or 3  # 5
0 or 5  # 5
5 and 0  # 0
5 >> 2 # 1
5 << 2 # 20
15<<2 # 60

#input formatting --> input() function is used to take input from the user. By default, it takes input as a string. We can format the input using various methods like split(), map(), etc.
# int(input())  # takes integer input
#float(input())  # takes float input
#2 or 3 inputs--> map()
names=input("Enter names separated by space: ").split()
#we can have the any number of the input values separated by space and we can store them in a list using split() method.
name1, name2=map(str, input("Enter two names separated by space: ").split())
#map() should have 2 arguments, first is the type of input and second is the input itself. It will take the input and convert it into the specified type.
# flow of program ---> we have 3 types of flow control statements in python. They are:
# 1. Conditional statements (if, elif, else) , nested if else statements, ternary operator
# 2. Looping statements (for, while)
# 3. Control statements (break, continue, pass)
# by ddefault 4 space indentation is used in python. We can use any number of spaces but it should be consistent throughout the program.
# syntax --> if <condition> : statements
entry_time = int(input("Enter the entry time in 24 hour format: "))
if entry_time > 9 :
    print("You are late")
'''
#if 5: execute statements, if 0: do not execute statements
#if True: execute statements, if False: do not execute statements
income = int(input("Enter your income: "))
if income >= 10000 : 
    print("You are eligible for the loan")
else :
    print("You are not eligible for the loan as ur income is less than by our criteria by", 10000-income)




