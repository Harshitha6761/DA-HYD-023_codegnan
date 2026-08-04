#for with else --> the else keyword will only be executed when the loop is completely without any break

'''
else block will be executed only when the break keyword is not used
break--> terminate the excution of loop and exit the loop and execute the remaining statements

#longest streak using for else

work_log=[0,1,1,1,0,1,0]
longest = 0
current = 0
for i in work_log:
    if i == 1:
        current+=i
        if longest<current:
         longest=current
    else:
        current=0 #streak break
else:
    print(f"longest streak is {longest}")
    
--------------------------------------------------------

# longest steak code using break

work_log=[0,1,1,1,0,1,0]
longest = 0
current = 0
for i in work_log:
    if i == 1:
        current+=i
        if longest<current:
         longest=current
         print(longest) # this print statement will be execute as 1 because we could not encounter the break keyword yet
         break
    else:
        current=0 #streak break
else:
    print(f"longest streak is {longest}") # the print statement will not be executed as the loop does not fully iterated
print(f"longest streak is {longest}") # this print will be executed as this print is outside the for loop and return 1 as output

-----------------------------------------------

#for else with notifications scenario

msgs=list(map(int,input("enter values").split()))
for i in msgs:
    if i==1:
        print("unread notifications")
        break                # in this case we dont iterate through the complete list, the loop will break at the first appeareance of 1
else:
    print("all are caught")
    
'''
#while --> it relies on the condition, if the condition is true then the loop statements, loop will be executed until the condition becaomes false

'''
initialization
while <condition>:
    statements
    updation

#infinite loop
while 1:
    print("nani")

while True:
    print("harshu")

while 2:
    print("nani")

while <value>:
    print("name")

while loop without updation if condition is true

#0 and False are consider as false so the statements are not executed

val=0
i=1
while i<=10:
    val=11-i
    print(val)
    i+=1

#decrement from 10
i=10
while i>=1:
    print(i)
    i-=1

i=0
while i<=10:
    print(10-i) #new thought

#banking scenario --> pin authentication, if more than 3 attempts - account block

pin="nani2004"
max_attempt=3
i=1
while i<=max_attempt:
    p=input("enter pin")
    if p==pin:
        print("login successful")
        break
        #continue --> skips the remaining statements i.e when condition is true
    else:
       print("retry")
    i+=1
else:
    print("account block")

---------------------------------------------

practice


#sum of numbers
num=int(input("enter range"))
res=0
for i in range(num+1):
    res=res+i
print(res)

num=int(input("enter range"))
res=0
i=1
while i<=num:
    res=res+i
    i+=1
print(res)

lst=list(map(int,input("enter values").split()))
res=0
print(lst)
for i in lst:
    res=res+i
print(res)
'''




























    














































