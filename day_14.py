'''
lists, tuples
List --> mutable,ordered,heterogeneous
#index(),count(),copy(),sort(),reverse()

#index() --> returns the index of 1st occurance by default, if we mention the start index then we can get the index of that value from that index
details = ['codegnan',7,2018,'hyd']
print(details.index(7))
print(details[0].index('d'))
details.extend([7,21,45,21])
print(details)
print(details.index(21)) # returns 5 as 21 occured 1st in 5th index
print(details.index(21,6)) # starts search of 21 from the 6th index and returns 7
#print(details.index('python')) # value error as the python not present in details


#copy() --> create a shallow copy of the list, both old and new lists are independent when there is no nested list
old = ['codegnan',7,2018,'hyd']
new = old.copy()
print(new)
print(type(new))
print(len(new))

new[2]='harshu' # changes made in new list will not effect old list
print(new)
print(old)

old[1]='nani' # changes made in old list will not effect new list
print(old)
print(new)

old.pop()
print(new)
print(old)

data=[1,4,5,[21,34,45],23]
duplicate=data.copy()
print(data)
print(duplicate)

data[3][2]='agents'
print(data) # changes made in data effects the duplicate list as the changes are made in the nested list
print(duplicate) 

duplicate[3][1]='nani' # in the same way, changes made in the nested list of duplicate list will effect the original list 
print(duplicate)
print(data)

data[1]='harshu' #no changes effected as the changes are made on the normal value not nested list
print(data)
print(duplicate)


#sort() --> by default sort the list in ascending order, if arg reverse is used then decending order. it only works with same type of elements the changes made are permanent so list is modified
marks=[14,24,-45,27,35] # if string present in list then sort will return type error becoz we compare a int with string
print(marks)
marks.sort() # returns in ascending order
print(marks)
marks.sort(reverse=True) # retuens in decending error
print(marks)


#reverse() --> perform permanent changes, return the reverse order of the list, it can have any type of elements in list
marks=[14,24,-45,27,'nani',35]
marks.reverse()
print(marks)

#type(),len(),max(),min(),print() --> built in funtions that applies on every element of list
#sorted() --> built in function that sorts any kind of collections, and returns the result in new list
print(sorted('codegnan')) #ascending order --> taking list and providing a list
print(sorted('codegnan',reverse=True)) #decending order
#print(sorted(['code','23',45,35])) #type error

#tuple --> immutable, ordered, heterogeneous,indexed ---> mainly used in stroing dimensions,coordinates,database records
#tuple-->(), can contain nested list, nested tuple
a=()
print(type(a))
print(len(a))

dim=1.5,2.5 # create a tuple
print(dim)
print(type(dim))
print(len(dim))
#operations--> membership, slicing,striding,indexing,repitation,merging
course=('pfs','jfs',('da','ds'),'agentic Ai',[100,6,6]) # nested tuple
print(course)
print(len(course))
print(course[3][-2:])
print(course[3][8:])
#course[2]=23 # tuple does not support item modification
course[4].append('codegnan') # here we are making changes in the list that is inside tuple, and len of tuple is not effecting
print(course)

print('pfs' in course)
d=course*2 # complete tuple is repeated twice
print(d)
e= course+(2,3,4) # merigng 2 tuples , only tuples can be merged not list, set cannot be concatenated
print(e)

#operations --> index(), count()
#index(value,start,end) --> returns the index of 1st occurance of the value
print(course.index('jfs'))
print(course.index('agentic Ai',2))

#count(value) --> count the no. of occurance of the value inside the tuple
print(course.count('jfs'))

#sorted() --> built in function that can be applied on the tuple only when the tuple has same data types.
#print(sorted(course)) #type error
course=('pfs','jfs',('da','ds'),'agentic Ai',[100,6,6]) # nested tuple
print(sorted(course[-1]))

#type casting
d=tuple(sorted([23,45,11,76,54])) # list converted to tuple
print(d)
print(type(d))

#accept group of integers space seperated
a,b=map(int,input().split())
print(a,b)

a = tuple(map(int,input().split()))
print(a)
'''
print('9+2')
print(eval('9+2'))# it takes the source and evaluate the value
#eval() --> we can use it to read value from user and the type will decide based up on the user given values
a=eval(input('enter values'))
print(type(a)) # type of a depends on the user input
print(a)
'''
1st input
enter values[2,5,6,8]
<class 'list'>
[2, 5, 6, 8]

2nd input
enter values(28,46,23,56,78)
<class 'tuple'>
(28, 46, 23, 56, 78)
'''
'''
#task
#create a nested tuple and work on slicing,striding,list function

1. give the count of each repeating character
test case 1: programming
r is repeating 2 times
g is repeating 2 times

2.
r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]






























