'''
#ecommerce website total product cost
product_price=list(map(int,input().split(',')))
total_cost=0          
for i in product_price:
    total_cost+=i
print(total_cost)

#password analyzer and count of total uppercase values,lowercase,digits,special_characters

password=input("enter password")
upper_count=0
lower_count=0
digit_count=0
symbol_count=0
for i in password:
    if i in ['1','2','3','4','5','6','7','8','9','0']:
        digit_count+=1
    elif i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        lower_count+=1
    elif i in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
        upper_count+=1
    else:
        symbol_count+=1
print(f"upper case count : {upper_count} \n lower case count : {lower_count} \n digit count : {digit_count} \n symbol count : {symbol_count}")


password=input("enter password")
upper_count=0
lower_count=0
digit_count=0
symbol_count=0
for i in password:
    if ord(i)>=48 and ord(i)<=57: #as odinal number of 0=48 and 9=57
        digit_count+=1
        print(digit_count)
    elif ord(i) >= ord('a') and ord(i)<= ord('z'):
        lower_count+=1
    elif ord(i)>= ord('A') and ord(i)<=ord('Z'):
        upper_count+=1
    else:
        symbol_count+=1
print(f"upper case count : {upper_count} \n lower case count : {lower_count} \n digit count : {digit_count} \n symbol count : {symbol_count}")


password=input()
digit_count=symbol_count=lower_count=upper_count=0
for ch in password:
    if 'A' <=ch<='Z':
        upper_count+=1
    elif 'a'<=ch<='z':
        lower_count+=1
    elif '0'<=ch<='9':
        digit_count+=1
    else:
        symbol_count+=1
print(f"upper case count : {upper_count} \nlower case count : {lower_count} \ndigit count : {digit_count} \nsymbol count : {symbol_count}")


#domain name extraction 
mail=list(map(str,input("enter mail").split(',')))
for i in mail:
    name,data=i.split('@')
    print(data)

email=input().split()  #.split() made email as a list 
for m in email:
    print(m.split('@')[1]) # we are converting it into string to apply split() function ,, [1] is the index after spliting we have 2 parts 

mail=input()
print(mail.split('@')[1])


#movie names with serial number

movie=input().split(',')
for j in range(1,len(movie)+1):
        print(j,movie[j-1])

mv=list(map(str,input().split(',')))
i=1
for m in mv:
    print(i,m)
    i+=1

#fibbonacci series
n=int(input("enter limit"))
c=0
a,b=0,1
for i in range(n):
    print(a,end=' ')
    #c=a+b
    #a,b=b,c
    a,b=b,a+b

n=int(input("enter limit"))
a,b,i=0,1,1
while i <=n:
    print(a,end=' ')
    a,b=b,a+b
    i+=1

''''
























    
    
    
    


























