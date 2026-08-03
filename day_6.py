'''
#control statements-->control the flow of execution of the program
                   -->conditional statement  == if,elif,else
                   -->repetation statements  == for, while (for with else, while with else)
                   --> jumping statements  == break,continue,pass,assert

--> loops == loops are helful for the repetation (automative tasks)
--> for keyword will be helpful to iterate over the sequence or range (used when the limit is known)
#synatax of for keyword: 
for <temp_variable> in sequence or range:
    statements

# range(start,stop,step) --> if start is not mentioned then default is zero,,  if step is not mentioned then default 1 is taken and step should not be zero,,, always excute upto n-1

for i in range(10):
    print(i)  # we get 10 iterations and the values are 0,1,2,3,4,5,6,7,8,9

for i in range(1,10):
    if i>5 and i%2==0 :
        print(f"value of i is {i}") # 6,8

for i in range(1,10,2):
    print(i) #odd numbers are printed , optimized way of printing odd numbers less time complexity

for i in range(-10,0,1):
    print(i)


#sequence
[] == list

names =['nani','harshu','harika']
print(len(names)) # len() --> returns no. of items in the container
for i in names:
    if i=='nani':
        print(f"student is {i}")

#sum of 1st 10 numbers
sum1=0
for i in range(11):
    sum1+=i
print(sum1)

#sum of 1st 10 even numbers
res=0
for i in range(21):
    if i%2==0:
        res+=i
print(res)
'''
# ***task : longest steak ==> workout=1, miss =0
work_log=[0,1,1,1,0,1,0]
longest = 0
current = 0
for i in work_log:
    if i == 1:
        current+=i
        if longest<current:
         longest=current
    else:
        current=0
print(f"longest streak is {longest}")
        














