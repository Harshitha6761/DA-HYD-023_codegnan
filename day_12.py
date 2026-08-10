'''
String --> CaseCOnversion,,searching,finding,string testing methods,replace,space removal

#Searching,finding,replacing, joining
a="Codegnan"
print(len(a))
print(min(a))
print(max(a))

#index() --> gives the index of the character and throws error if the character doesnt present

b=a.index('g')
print(b)
c=a.index('n') # returns the 1st occurance of the n
print(c)
d=a.index('n',6)  # checks the character n from that index
print(d)
#e=a.index('n',8)   -->valueError as n not present from index 8
#print(e)
#f=a.index('t')      --> valueError as t not presnt in the string
#print(f)
#g=a.index('n',1,4)   --> giving range to check the occurance
#print(g)           -->valueError

#rindex()  --> returns the last occurance of the character
a="Codegnan"
b=a.rindex('g')
print(b)
c=a.rindex('n')
print(c)
#d=a.rindex('n',8)  --> here 8 is the starting index to search
#print(d)
e=a.rindex('n',6)
print(e)

# count
print("Codegnan".count('n')) # count() is used to find the count of the character in given string
print("code".count('w'))     # if character doesnt present then op is 0

#find() --> gives index of 1st occurance of character and no error if character doesnt present
print("nani".find('n'))
print("harshu".find('e')) # -1 if character is not presnt

#rfind() --> gives the index of last occurance of character, doesnt throw the error if the character is not there and returns -1 if the character doesnt present
print("codeganan".rfind('a'))
a="nani"
for i in a:
    print(i,a.count(i),a.index(i))
    
#Replacing, spliting,joining
a="Codegnan"
#a[4]=s  --> throws error as the strings are immutable
print(a.replace('g','h')) # temporary change
print(a) # original a is not changed evemn after replacing g with h in above line
a=a.replace('g','x') # replacing g with x and again stored in a
print(a) # a is modified
print(a.replace('n','y')) # replaced with y in the place of all occured n
print(a.replace('C','Course')) # string can be replace in 1 character place
print(a.replace('v','b')) # no change is made as v is not present in a

#split()
st="code is important"
b=st.split() # sentence is splitted into word at the place of space  --> split() default is space
print(b) #here string is converted to list
c=st.split(',') # as , is not present in the string the same string is printed --> no changes
print(c)

#join() --> arg inside the join() is more imporatant
a='code'
b='gnan'
c='x'
print(a.join(b)) # joins the b's each character is used the a's string gcodencodeacoden
print('nani'.join('*'))
print(a.join('*')) # * as the * is single character cannot be iretable
print(c.join(a))   # a has 4 characters so we can iterate 3 times


#String testing methods --> op is true or false
#isalpha()--> onlt alphabets, isalnum()--> both alphabets or numbers but not symbols, isdigit()--> only numbers, isupper()-->checks for uppercase, islower()
a='codegnan123'
print(a.isalpha()) #false
print(a.isalnum()) #true
print(a.isdigit()) #false
b='12334'
print(b.isdigit(),"returns true if all the characters are digits") #true
print(b.isalpha()) #false
print(b.isalnum(),"returns if any digits or alphabets are presnt") # true
c='nani'
print(c.isalpha(),"returns true only the all characters are alphabets") # true
print(c.isalnum(),"values") # true
d='HSIOA'
print(d.isupper()) #true for all upppercase
e='nsoi'
print(e.islower()) #true if all are lower case
print('1233455'.isnumeric()) # checks the numbers,fraction,roman numbers in data analysis
print(a.startswith('c'),"returns true if the starting letter is matched with given letter")
print(a.startswith('g'))
print(a.startswith('g',4)) # mentioning the start index to start the search
print("Code Python".istitle(),"true if all the strating letters are capital")

#space removal --> strip() removes the spaces starting and ending spaces
a=input().strip() # removes starting and ending spaces if the user enter them
print(a)
b=input().lower() #input is read in lower case whatever the user enters
print(b)

'''
#zfill --> fills zeros in the empty spaces on left side
print('1234'.zfill(6))  # 001234

#center --> insert spaces at end and start to make the given string as center
print('nani'.center(8)) # __nani__
print('nani'.center(8,'#')) # to fill the inserted spaces with # character ##nani##
print('nani'.ljust(8)) # adds spaces on only ending side
print('nani'.ljust(8,'*')) # nani****
print('nani'.rjust(6)) # add spaces on starting of string
print('nani'.rjust(6,'&')) # &&nani





































































