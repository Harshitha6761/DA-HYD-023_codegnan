'''
#guess the number
secret=123
while True: #while 1:
    numb=int(input("Enter the number --> "))
    if numb==secret:
        print("correct guess")
        break
    elif numb<secret:
        print("lesser")
    else:
        print("greater")

sec=1234
guess=int(input())
while guess!=sec:
    if guess<sec:
        print("lesser")
    else:
        print("greater")
    guess=int(input())
print("guess correct")

#OTP verification
real_otp=564
i=1
while i<=7:
    otp=int(input("enter otp --> "))
    if otp==real_otp:
        print("correct otp entered")
        break
    i+=1
else:
    print("blocked")

#food order count
total_orders=0
while True:
    food_item=input("Enter your order --> ")
    if food_item=="Exit":
        break
    else:
        total_orders+=1
print(total_orders)

food=input("enter food")
count=0
while food != 'Exit':
    count+=1
    food=input("enter food")
print(count)

'''
#guess the word
secret="python"
total_chances=3
attempt=1
while attempt<=3:
    code=input("Enter the course -->")
    if code==secret:
        print(f"You won,you have {total_chances-attempt} chances")
        break
    else:
        
        print(f"You lose,you have {total_chances-attempt} chances")
    attempt+=1



























    
    

