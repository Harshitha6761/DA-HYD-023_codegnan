'''
#task 1
def calculated_grade(m):
    grade='fail'
    if m>=80:
        grade='A'
    elif 60<=m<=79:
        grade='B'
    elif 40<=m<=59:
        grade='C'
    return grade
for i in range(3):
    m=int(input("enter marks"))
    if m>100 or m<0:
        print("invalid")
    else:
        print(calculated_grade(m))

#task 2
def calculate_bill(p,q=1,d=0):
    total=p*q
    total=total-d
    return total
print(calculate_bill(50))
print(calculate_bill(price=60,2))
print(calculate_bill(100,1,30))

#task 3
def calculate_bmi(n,w,h):
    bmi=(w)/(h**2)
    print(f"{n} bmi is{bmi}")
    return bmi
def bmi_status(bmi):
    if bmi < 18.5:
        print("underweight")
    elif 18.5<=bmi<=24.9:
        print("normal")
    elif 25<=bmi<=29.9:
        print("overweight")
    else:
        print("obese")
for i in range(3):
    name=input("enter name")
    w=int(input("enter weight"))
    h=int(input("enter height"))
    bmi=calculate_bmi(name,w,h)
    bmi_status(bmi)

#task 4
def marks_summary(*args):
    count=len(args)
    print(count)
    res=0
    #avg=0
    if count==0:
        print("no arguments passed")
    else:
        for i in args:
            res=res+i
        avg=res/count
        print(avg)
marks_summary(5)
marks_summary(4,3,7,8)
marks_summary()
'''
#task 5
def display_employee(**kwargs):
    print(kwargs.keys())
    if 'salary' not in kwargs.keys():
        print("salary is missing")
    if 'department' not in kwargs.keys():
        print("department is missing")
    for key,value in kwargs.items():
        print(f"{key} --> {value}")
display_employee(name="harshu",role="data analyst",salary=1200000,department="da")
display_employee(name="nani",role="developer",department="software")    
