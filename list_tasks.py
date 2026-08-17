#task 1 --> Student Marks manager
'''
marks=[]
n=int(input("no of students"))
for i in range(n):
    m=int(input("enter marks"))
    marks.append(m)
print(marks)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
print(marks.pop())
print(marks)
print(len(marks))
    
#task 2 --> 
numb=[20,10,30,20,40,20]
numb.sort()
for i in numb:
    print(i)
numb.reverse()
print(numb)
number=int(input("enter the number to search"))
if number in numb:
    print(f"count of the {number} is {numb.count(number)}\nindex of first occurance is {numb.index(number)}")
else:
    print(f"{number} is not found")
print(max(numb))
print(min(numb))
print(sum(numb))

#task 3
number=[10,15,20,25,30,35]
backup=number.copy()
even=[]
odd=[]
for i in number:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(number[:3])
print(number[-3:])
print(even)
print(odd)
number.clear()
print(backup)
print(number)

#task 4
names=['Asha','Rahul','Asha','John','Rahul']
unique=set(names)
print(unique)
unique.add('Meera')
print(unique)
unique.update(('Arun','Priya'))
print(unique)
if 'John' in unique:
    unique.remove('John')
else:
    print("John not present")
unique.discard('David')
for i in unique:
    print(i)
'''
#task 5
python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}
total=python_students.union(da_students)
print(total)
for i in total:
    print(i)
for i in python_students.intersection(da_students):
    print(i)
only_python=python_students.difference(da_students)
print(only_python)
only_one=python_students.symmetric_difference(da_students)
print(only_one)
if da_students.issubset(python_students):
    print("Da is a subset of Python.")
else:
    print("Da is not a subset of Python.")

if python_students.issuperset(da_students):
    print("Python is a superset of DA.")
else:
    print("Python is not a superset of DA.")

if python_students.isdisjoint(da_students):
    print("The two sets are disjoint.")
else:
    print("The two sets are not disjoint.")




















        
