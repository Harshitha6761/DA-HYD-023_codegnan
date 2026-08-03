#Tasks regarding if - elif - else statements
'''
Task-1 : "grade checker"

marks= int(input("Enter the marks"))
if marks >= 0 and marks < 50:
        print("Grade : F")
        print("Remark: Failed,needs to reappear")
elif marks >= 50 and marks <60:
        print("Grade : E")
        print("Remark: Poor, needs serious improvement")
elif marks >= 60 and marks <70:
        print("Grade : D")
        print("Remark: Fair,needs improvement")
elif marks >= 70 and marks <80 :
        print("Grade : C")
        print("Remark: Good")
elif marks >= 80 and marks< 90:
        print("Grade : B")
        print("Remark: Excellent")
elif marks >= 90 and marks <= 100:
        print("Grade : A")
        print("Remark: Outstanding")
else :
    print("Invalid marks entered")
----------------------------------------------------

Task-2 "even odd checker"

val=int(input("enter value"))
if val>0 and val%2 == 0:
    print("Even Number")
elif val>0 and val%2 != 0:
    print("Odd Number")
elif val<0 and val%2==0:
    print("Negative Even Number")
elif val<0 and val%2!=0:
    print("Negative Odd Number")
else:
    print("Zero is neither even nor odd")

-------------------------------------------
Task 3: "season checker"

month=int(input("Enter month number from 1-12"))
if month in [12,1,2]:
    print("Winter")
elif month in [3,4,5]:
    print ("Spring")
elif month in [6,7,8]:
    print("Summer")
elif month in [9,10,11]:
    print("Autumn")
else:
    print("Invalid month entered")

-------------------------------------------
'''

