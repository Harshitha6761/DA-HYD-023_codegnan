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


#task 1
t=(1,45,23,[8,4,7],(2,4,7),'nani')
print(t[1]) #45
print(t[-1][-1]) #i
print(t[::2])
print(t[3][::2])
print(t[-1][::2])
t[3].append(5)
print(t)
t[3].extend([2,4,19])
print(t)
t[3].insert(3,17) #index,value
print(t)
t[3].pop()#19
print(t)
t[3].remove(4)
print(t)
print(t.index(23))
t[3].reverse()
print(t)
c=t[3].copy()
print(c)
t[3].sort()
print(t)
print(t[3].count(7))
t[3].clear()
print(t)


#task 2
name=[]
new=[]
val=input()
name.extend(val)
print(name)
for i in name:
    if i not in new:
        new.append(i)
        c=name.count(i)
        if c>1:
            print(f"{i} is repeating {c} times")
'''
#task 3
name=[]
new=[]
val=input()
name.extend(val)
print(name)
for i in name:
    index=[]
    if i not in new:
        new.append(i)
        c=name.count(i)
        if c>1:
            start=0
            print(f"{i} is repeating {c} times")
            while i in name[start:]:
                index.append(name.index(i,start))
                start=name.index(i,start)+1
            print(f" Index : {index}")











