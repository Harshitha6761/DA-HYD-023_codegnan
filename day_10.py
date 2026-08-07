'''
#batman's innings alanysis
score=list(map(int,input("enter score in each ball").split(',')))
boundaries=dot=total=0
for i in score:
    if i==4 or i==6: # i in [4,6]
        boundaries+=1
    elif i==0: #using elif make the less time complexity like if i satisfies if condition we dont ckeck the elif condition
        dot+=1
    total+=i
print(f"no. of boundaries {boundaries}")
print(f"no. of dot balls {dot}")
print(f"total score {total}")

#phone password checking
ptn="nani2004"
max_atmpt=5
i=1
while i<=max_atmpt:
    pswd=input("Enter password -> ")
    if pswd == ptn:
        print("phone unlocked")
        break
    #else:
    #   print("wrong password,retry")
    i+=1
else:
    print("phone locked")
 
'''
#ATM verfification
pin="12@12"
max_atmpt=3
i=1
while i<=max_atmpt:
    pswd=input("Enter pin -> ")
    if pswd == pin:
        print("Account logged in")
        break
    else:
        i+=1
else:
    print("Account blocked")
