'''
Sequences --> Strings, lists,tuples, sets
Mapping --> Dictionary

#List --> collection of heterogeneous elements(diff or same kinds of data types)
#List --> indexed, mutable, ordered, hetrogeneous, we use [ ] to create and store elements
marks = [10,30,45]
print(len(marks))
print(type(marks))
print(10 in marks)
#operations --> indexing, slicing, striding, membership, merging, repitation
#nested list --> list inside another list
name=['codegnan',25,4.5,[12,45,67,89],29,'nani']
print(type(name[0]))
print(name[0])
print(len(name[0])) # length of string stored in list
print(name[0][4:])
print(name[-3])
print(name[0][::2])
name[0]=name[0][::-1]
print(name)

print(name[3])
print(len(name[3])) #length of inner list
print(name[3][:2])
print(name[3][2])

#indexing,slicing --> mutable
name[2]='hasrhu' # by indexing if we replace the element then the list length will not change 
print(name)
name[4]=['pfs','jfs','da','ds','aaa']
print(name)
print(len(name))

#length can be increased using index if we insert more elements in given index
name[2:4]='abc','shi'
print(name)
name[2:4] = 'jash',97,'harshu',9823
print(name)
print(len(name))
names=['codegnan',25,'abiram','sai','saketh','java','da26',34]
names[3:6:2]='python','java'
print(names)

#create a nested list with string, lists and work on indexing,striding, slicing,and add string functions also

#list funtions --> append(), index(), remove(),pop(),insert(),extend(),count(),clear(),copy(),sort(),reverse()

lst = ['codegnan','saketh']
#append() --> add single element at end of the list --> exactly 1 element
print(lst.append('data'))
#lst.append('analysis','agent') --> Type error as 2 elements are added as rule is breaked
lst.append(['analysis','agent']) # as [] used,list  is added at the end of lst and length incremented by 1
print(lst)
print(len(lst))
lst[3].append('chatgpt') #adding element to inner list
#print(lst[3].append('chatgpt')) # None is printed as append is used for list and that updated value is stored in lst, print will treat append differently 
print(lst)

#entend --> inserts multiple elements at the end of list
#lst.extend('analysis') # extend is iteratble so analysis is splitted as a, n,a,l,y,s,i,s  as it is not inside list
lst.extend(['analysis'])
lst.extend([45,75,24,56]) # extend takes only 1 arg so we take it in list and the items in list are added at the end 
print(lst)
#lst.extend('data','gpt') # Type error as extends takes only 1 arg

#insert() --> add element at specific position without disturbing order and not removing the exxsisting items
lst.insert(1,'python') # needs 2 args, what index and what value and all the remainig will move backside
print(lst)
#lst.insert([1:4],'a','b','c') --> syntax error as insert should have 2 args and no : 
lst.insert(-1,'AAA') # -1 index means -1-1 = -2 index will be changed this applies only in negative index
print(lst) 

#pop() --> delete by last/end element and if index is mentioned then the value in that indexx is removed
lst.pop() #default last value is removeed
print(lst)
lst.pop(-1) # reverse order index
print(lst)
lst.pop(7) #specific index value is remove
print(lst)

#remove() --> delete the first occurance of the given value,, delete by value
lst.remove('data')
print(lst)
#lst.remove('harshu') # as harshu is not in list then we get error

#del keyword --> removes multiple values using index
del lst[1:3]
print(lst)

#clear() --> deletes all elements in list
lst.clear() # [ ] is output , represnts empty list
print(lst)

#task
data=['codegnan','saketh','python','java']
op:
0 : codegnan
1 : saketh
2 : python
3 : java

'''
data=['codegnan','saketh','python','java']
for i in data:
    print(f"{data.index(i)} : {i}")
    


































