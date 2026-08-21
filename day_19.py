'''2 32 4
Exception handling and scope of variables / built in functions

exception handling --> it is a machanism that help to respond or make the flow of execution in normal way, without this error will occur and disrupt the flow of execution

common expections --> ValueError,TypeError, IndexError,AttributeError,ZeroDivisionError

--> we cannot throw multiple exception at a time --> but we make exceptions as tuple and check --> then msg will be 1st occured exception
--> statements after the error will not be executed even when the exception is handled
syntax:

try:
    #code that will cause the exception
except Exception as e:               --> we can have any no. of except block...which error occurs 1st that respective except block will be executed
    #code will catch the exeception 
finally:
    #runs irrespective of try/except
    ....

#basic exception
try:
    a=list(map(int,input().split()))
    print(len(a))
    #for i in a:
    #    result=20//i
     #   print(result)
    a.app(6)            # here exxception occured then direct goes to attributeError except block
    print("hello")      # does not print hello because in above line we got execption
    val=30//a[len(a)+3]
#except Exception as e:
#    print(e)      #--> throws exception as message 
#except Exception:
#    print(Exception) #---> throws exception as <class 'Exception'> , dont mention any error instead return class of exception
except ValueError:
    print(ValueError)  #--> value error is a class
except ZeroDivisionError:
    print("zero is not allowed as denominator")
except NameError as n:
    print(n)
except TypeError:
    print("we cannot perform division with single value with list")
except IndexError:
    print("list index out of range")
except AttributeError:
    print("list does not have function")
print("harshitha at codegnan")
    
##handling multiple error at once
try:
    a=[2,3]
    a.app(6)
    b=a[6]
except (TypeError,IndexError,AttributeError) as e:
    print("error due to wrong variable or index out of range or no function ")
    print(e)
print("harshitha at codegnan")

#bmi task:
while True:
    try:
        w=int(input("enter weight in kgs"))
        h=float(input("enter height in cms"))
        if w>0 and h>0:
            #break
            pass
        else:
            print("weight and height should be greater than 0")
    except Exception as e:
        print(e)
bmi=w/(h**2)
print(bmi)

#task ---> bmi using try,while,functions

##scope of variables --> scope is region/area where it is accessed
#1.local variables --> varibales defined inside the function and accessed inside the function/ block
#2.global variables --> defined outside(i.e.before or after ) the function and can be accessed anywhere in the program but once defined cannot be modified

#example
id='23da'      #global variable
def sample():
    print(id)
    name="harshu"   #local variable
    print(name)
    print(age)
age=54        #globl variable
sample()
#print(name) --> NameError bacause the name is not defined , here name is defined inside the function so it is limited to function
#age=89    --> age defined after function call so NameError


#if local and global variable has same name, then inside the function the local variable has more priority but outside global variable has more prioity
#modify global variable ---> using global keyword
count=20
def data():
    """usage of global keyword"""
    #global count   # accessing global varibale to modifyable using 'global' keyword,,,so once modified the change is permanenrt
    count=1         # here count is other variable that is local variable
    count=count+5  # when we try to modify it raise UnboundLocalError
    print("value inside function",count)
data()
print("value outside function",count)

#enclosing scope (nonlocal keyword

def outer():
    """outer function"""
    count=5
    def inner():
        """nested funtion"""
        nonlocal count # making outer function variables are modified inside inner function using 'nonlocal' keyword and change is permanent
        count=count+5 #UnboundLocalError as the count is not inside the inner and can't be modified
        print(count)
    inner()
    print(count)
outer()
'''
#builtin functions --> varible builtinScope
#builtin functions cannot be used as variables ...once used it lose its functionality and act as jst variable
len=10
print(len+10)

print(len('codegnan')) # above len is variable so it lost its functionality of calculating length and acting as variable



















