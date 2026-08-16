'''
sequences --> Strings,lists,tuples,set,frozenset
mapping --> dictionary

#Set --> set is a unique collection of objects,unordered, mutable, Hashing(helps indexing and stores the data faster), Unindexed, heterogenous, can not store lists inside it
#set() is used to create a set, denoted by { }
# a={} # by default a is dictionary
a= set()
print(type(a))
print(a)
stu_id={123,345,234,564,234} # create a set when the values are passed, based upon type of data it differ the dict and set
print(type(stu_id))
print(len(stu_id)) # 4 because 234 is repeated twice
print(stu_id)
#print(stu_id[2]) --> type error as the set dont have indexing because the set is unordered
print(234 in stu_id) #membership
print(stu_id * 2) # type error as set cannot store duplicated values --> repitation not supported
#stu_id+ stu_id # merge is not possible

#operations on set
#data={12,3,4,5,[1,3,4],'nani'} # type error, unhashed type nested list is not possible
data={12,5,7,(6,4,8),'nani'} # tuple and string can be stored inside the set as they are mutable
print(data)
print(len(data))
for i in data:
    print(i) #  we can access every element
#data={1,5,9,{4,9,7},85} # set can not have nested set as set can only store mutable object
#print(data)

#method --> add(),remove(),update(),discard(),pop()
#add() --> add single element each times only that value does  not exist in the set
names={'sai','saketh','kiran','codegnan'}
print(len(names))
names.add('python') # cannot take if we give existed value and python  can be added anywhere in set as it is unordered
print(names)
#names.add('data','analytics') --> add should have single parameter
names.add(('poll','police')) # --> adding a tuple to existing set
print(names)

#update() --> update a set with multiple values here braces does not matter
da_names={'mani','akash','sai','sonu'}
names.update(da_names) # we can update 1 list with another
print(names) # old set added with unique items that present in new set but not in old set --> updating list with multiple elements
print(len(names))
print(da_names) # no changes in new set
print(len(da_names))

#remove element  --> remove(),pop(),clear()
#remove() --> remove by value , raise key error if element is not present
da_names.remove('sai') # if given value present then it will be removed
print(da_names)
#da_names.remove('sai') # key error when the given value does not present in the set
#print(da_names)

#discard() --> remove by value, but does not raise a error even the element is not present, insted it will ignore
da_names.discard('sai')  # does not raise error as sai is not in set
print(da_names)
da_names.discard('codegnan')  
print(da_names)

#pop()--> removes and return the removed element and removes any element from the set until list becomes empty
da_names={'mani','akash','sai','sonu'}
print(da_names.pop()) # gives the removeed element from the list
print(da_names) # returns the complete set after removal of element

#clear() --> removes all elements from the set and returns empty set
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update([3,6,9]) # no insertion order maintained , [] does not indicate a list, it indicates a group of values
print(da_names)
da_names.update((31,61,91))# here it is not tuple, group of elements
print(da_names)

#copy() --> shallow copy
d=da_names.copy()
print(d)
d.update([7,90,67],[54,86,43])# 2 individual grp of values are added to set
print(d)
'''
#mathematical operations: union(),intersection(),difference(),symmetric(),issubset(),issuperset(),isdisjoint()
da_23={12,23,34,45,23,36}
da_24={34,46,47,23}
da_25={46,23,89,101}
'''
#union() --> | --> union of 2 or more sets
print(da_23.union(da_24))
event=da_23.union(da_24,da_25)# | is for union,returns new set of combination 2 or more sets with out duplicates
print(event)
print(len(event))
#intersection() --> & --> common values of the 2 or more sets
common=da_23.intersection(da_24)
print(common) # & is for intersection,returns new set with common values of 2 or more sets
print(len(common))
print(da_23 & da_25)
#intersection_update() --> takes intersection values and update them into 1st set
com=da_23.intersection_update(da_24) 
print(com) # returns none beacues the values are stored in da_23 not in com
print(da_23)

#difference() --> - --> removes the common elements and returns the 1st set
diff=da_23.difference(da_24)
print(diff)
diff=da_23-da_24
print(diff)
diff_up=da_23.difference_update(da_25)
print(diff_up)
print(da_23)

#symmetric_difference() --> ^ --> removes the common elements and return the values of both sets as one set
sym=da_24.symmetric_difference(da_25)
print(sym)
sym=da_24^da_25
print(sym)
sym_up=da_24.symmetric_difference_update(da_25)
print(sym_up)
print(da_24)
'''

#issubset() --> returns boolean value by checking whether the given set presnt in the main set
print(da_24.issubset({46,23,34,47,45,12,56})) # --> da_24 is subset of given set spo true

#issuperset() --> returns boolean value by checking the given set present in superset
print(da_24.issuperset({46,23})) # --> da_24 is superset of given set

#isdisjoint() --> returns true if the both sets dont have common values else false
print(da_23.isdisjoint(da_24))


#task
'''
length of unique student ids in a class, where the user can enter first input he should enter the ids nxt'''
n=int(input("enter the limit"))
stu_ids=set(map(int,input().split()))
print(len(stu_ids))



























































