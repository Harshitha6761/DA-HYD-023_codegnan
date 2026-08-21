'''
Functions
variable length arguments (*args) --> no. of arguments are varies, the no. of positional arguments are not limited but we need to use * representation
data is stored in tuple always

def sample(*args):
    """ simple demo for *args"""
    print(args)
    print(len(args))
    print(type(args))
sample()
sample(1,2,34,8)
details=[1,2,3,4,5,6]
sample(details) #here list is stored at index 0 of tuple so the length will be 1
sample(*details) #unpacking the collection --> list is converted to tuple --> len will 6

#representation of *
a,b,c=1,45,'da'
print(a,b,c)
a,*b,c='python','codegnan',23,56,9.6,'data'
print(a)
print(b) #b can store multiple value in the form of list
print(c)
a,b,*c='python','data'
print(a)
print(b)
print(c) #empty list as the no values are assigned
c.extend([23,56,78]) # c is list so we are extend()
print(c)


#task --> sum of given values where i cannot contraints to limit of numbers
def add(*args):
    print(args)
    print(type(args))
    res=0
    for i in args:
        if type(i) == int or type(i)== float: # int ,float are built in function
            res=res+i
            #print(res)
    return res
    
#val=list(map(int,input("enter").split()))
#print(add(3,4,5,'poll','bear',4.5))
#print(add(*val))
data=map(int,input("enter the values").split())
#print(add(*data))
print(*data) # we can use * to retrive the each value in the collection and print with space seperated--> like we are using for loop to retrive each value

#keyword variable length arguments(**args) --> we can pass any number of keyword arguments and represented by **
# always store in dictionary
def details(**kwargs):
    print(kwargs)
    print(type(kwargs))
details() # returns empty dictionary
details(name="harshu",place="hnk",batch="da") # kewywords should not be in " "
stu={'name':"nani",'place':"hnk"}
details(**stu) # ** is ued for unpacking the dictionary --> if we dont give ** the complete dictionary store as nested dictionary without key and throws error 

'''
#combining * and ** in function
def sample(*a,**b):
    """usage of both variable length and keyword variable length"""
    result=0
    data={}
    for i in a:
        if type(i) in (int,float,complex):
            result+=i
    #print(result)
    for key,value in b.items():
        data.extend(key,value)
    return result,data
print(sample(2,4,6,'police',7.4,
       name='harshu',
       place='hyd',
       batch='da'))
#sample(name="harshu",23,'police') --> the order should not be violated that variable length should be followed by keyword variable length
#sample(23,name='harshu',56,89,id='787d') --> positional arguments follows keyword arguments,, order violated















