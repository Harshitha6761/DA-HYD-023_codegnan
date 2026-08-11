#task 1
'''
data=input("enter sentence")
upper_data=data.upper()
print(f"Upper : {upper_data}")
lower_data=data.lower()
print(f"Lower : {lower_data}")
title_data=data.title()
print(f"Title : {title_data}")
cap_data=data.capitalize()
print(f"Capitalized : {cap_data}")
swap_data=data.swapcase()
print(f"Swap case : {swap_data}")
print(upper_data.isupper())
print(lower_data.islower())
print(title_data.istitle())

#task2
while True:
    data=input("enter data")
    if data=="quit":
        break
    else:
        if data.isalnum():
            print("contain both alphabets and numbers")
        else:
            print("does not contaion only letters and numbers")
        if data.isdigit():
            print("contain only numbers")
        if data.isalpha():
            print("only letters")
        if data.isascii():
            print("contain only ascii value")
        if data.isidentifier():
            print("valid python identifier")
        if data[0].isalpha():
            print("begins with letter")
        elif data[0].isdigit():
            print("begins with digit")
        else:
            print("begins with symbol")
        if 'a'<=data[0]<='z' or 'A'<=data[0]<='Z':
            print("begins with letter")
        elif '0'<=data[0]<='9':
            print("begins with a digit")
        else:
            print("starts with a symbol")
'''
#task3
name=[]
marks=[]
grade=[]
for i in range(3):
    n=input("enter name")
    m=int(input("enter marks"))
    if 80<=m<=100:
        g='A'
        name.append(n)
        marks.append(m)
        grade.append(g)
    elif 60<=m<=79:
        g='B'
        name.append(n)
        marks.append(m)
        grade.append(g)
    elif 40<=m<=59:
        g='C'
        name.append(n)
        marks.append(m)
        grade.append(g)
    elif 0<=m<=39:
        g='Fail'
        name.append(n)
        marks.append(m)
        grade.append(g)
    else:
        print("invalid value")
        
print("student report".center(25))
print("Name".ljust(8),"Marks".ljust(8),"Grade".ljust(8))
for i in range(len(name)):
    print(name[i].ljust(8),str(marks[i]).ljust(8),grade[i].ljust(8))

'''
#task4
data=input("enter the string")
letter_count=digit_count=space_count=printable_count=non_print=0
for ch in data:
    if ch.isalpha():
        letter_count+=1
    elif ch.isdigit():
        digit_count+=1
    elif ch.isspace():
        space_count+=1
    if ch.isprintable():
        printable_count+=1
    else:
        non_print+=1
print(f"letter count {letter_count}")
print(f"digit_count {digit_count}")
print(f"space count {space_count}")
print(f"printable count {printable_count}")
print(f"non printable count {non_print}")
print(data.islower())
print(data.isupper())
print(data.istitle())
    
'''







    
    
