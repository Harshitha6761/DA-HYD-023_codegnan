#functions
'''
procedure oriented programming
Functions --> A function is a block of code which performs a specific task
--> it is reusable block of code where we define using def keyword

Advantages --> reusablity, code maintainability,ease of debbugging,avoiding code duplication,modularity...

syntax:
def fname(parameters):   --> function defination
    """Doc string""" -->desciption about function
    statement(s)....
    ....                ---> function body
    return value(s)     --> final line of function
fname(arg1,arg2...)       ---> function call

#basic code
def add(a,b):
    """sum of objects of any data types"""
    c=a+b
    return c
print(add(12,15))  #addition
print(add('nani','harshu')) #concatination
print(add([1,2,3],[4,5,6])) #merging
c,d=map(int,input("enter values").split())
print(add(c,d))

#without return keyword
def add1(a,b):
    """sum of items without return keyword"""
    print(a+b)
add1(12,15)
print(add1(23,1)) #none becaues print have nothing to print

#usage of return 
#name,age,salary='nani',22,50000   #global variables
def details():
    return name,age,salary
    #return         --> op is none because there is nothing to print
name,age,salary='nani',22,50000  #global variables --> variables outside the function that can be accessed anywhere in the program
print(details())

there are 5 types of arguments:
1. positional arguments
2. default arguments
3. keyword arguments
4. variable length arguments(*args)
5. keyword variable length arguments(**kwargs)

#positional arguments --> no.of arguments in function definition should match with the parameters in function call(order should be maintained)
#print(len(12,34))  --> Type error as len will accept only 1 arg
def details(n,p):
    """ name and place storing"""
   # n='codegnan' replacing the user n and p values  with static so we get same op even the user input changes
   # p='hyd'
    return n,p
print(details('nani','hnk'))
#print(details('harshu','pkl',21)) #Type error becaues details() takes only 2 positional arg
print(details('wgl','ram')) # we will get op as the machine will take 2 arg and dont know whether wgl is place or name
print(details(n='sheshi',p='jangalapally'))
c,d=map(str,input("enter name and place").split())
print(details(c,d))


#default arguments --> we can make arg as default but not 1st arg as default when more than 2 args present , we can make arg as default by using = ,so if we miss that arg while calling then the default value is retrived
#case1
def grocery(item,price=35):  #2nd arg as default
    print(f"the {item} is {price} rupees")
grocery('eggs',25)
grocery(60,'book') # the values can be anything here order matters not the value
grocery('jacket') #here we did not gave price , but the default value is printed

#case2
def grocery(item='samosa',price=35):  # all arg as default
    print(f"the {item} is {price} rupees")
grocery('milk',54)
grocery()
grocery('jam')
#grocery(,32)#we cannot give 2nd arg without 1st

#case3
def grocery(item='sandwich',price): #syntax error as non default arg cannot follow default arg
    print(f"the {item} is {price} rupees")
grocery('salt',67)
'''
#keyword arguments--> whenever you want to specify the name of arguments , keyword matching is done
def employee(name,role,salary):
    """employee details storing"""
    print(f"the name is {name},where role is {role} and salary is{salary}")
employee(6761,'student','78444')
employee(salary=67200,name='nani',role='data analyst') # we mentioned the variable so these varibles match with the arg then print in correct order























