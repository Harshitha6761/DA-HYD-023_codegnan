'''
tokens --> keywords, identifiers, literals, operators, punctuators,variables
operators --> numeric data(int,float,complex), bool
control flow --> if, else, elif
sequences --> string, list, tuple, mapping(dict)

# String --> collection of characters, we use ' ' or " " or ''' ''' to represent a string
# strings are immutable, order, indexed collection
str1="codegnan"
print(str1)
print(type(str1))
print(len(str1)) #length of string ,, space is also character

#index --> used to fetch the object(position) starts at 0 and ends at len(oj)-1 ,, [] is used fetch the character at that index
print(str1[2])
#print(str1[36]) #IndexError --> string index out of range
#Negative index --> starts with -1 and ends with -len
print(str1[-2])


#slicing --> we can access a group of characters at same time  ,, str[start: end] ,, default start is 0 and ends with n-1 
name="codegnan"
print(name[:]) # codegnan
print(name[0:]) #codegnan
print(name[:4]) # code
print(name[1:5]) # odeg
print(name[1:8:2]) #oenn
print(name[:45]) # string
print(name[45:]) # empty string
print(name[7:3]) # returns empty string
print(name[7:3:-1])
print(name[-5:-1])

name="python"
print(name[4:6])#on
print(name[-2:0])#empty string
print(name[-2:])
print(name[4:])
print(name[1:-2]) #yth
print(name[2:-6])#empty string
# +ve +ve / -ve -ve / +ve -ve /-ve +ve

#Striding --> [start:end:step] ,, default step =1 ,, step-1 values are skipped

crs ='DataAnalysis'
print(len(crs))
print(crs[:4])
print(crs[4:])
print(crs[-3:])
print(crs[::1])
print(crs[::2])# skips n-1 i.e 2-1=1 character
print(crs[1:6:3]) # [1:6] --> ataAn --> [1:6:3] skips 2 values aA
print(crs[2::3])
print(crs[::-1]) #reverse string
print(crs[::-2])#reverse string 1 value skipped

#immutable
name='nani'
name[2]='h' # error


#workout with all possibilites of scling and striding
#string operation : indexing, concatinatio, repeatation, membership
name= 'nani'
print(name * 3) # repitation
data='nani'+'harshu'+'harika'
print(data) #concat
print('123'*4) #numeric string
print('n' in name) #membership
for i in 'codegnan':
    print(i)
for i in 'codegnan':
    print(i,end=' ')

#Built in functions-->len()min(),max(),ord(),sorted()
name="dataCodegnan"
print(len(name)) #length of string
print(min(name)) #based on ASKI value retrive the least aski value letter
print(ord(A))    #odinal of value --> gives ASKI value of letter
print(chr(97))   #charecter of Aski value --> aski to alphabet
print(max(name)) #returns greatest ASKI value letter
print(sorted(name)) # returns sorted list of given string

#Methods on string --> case conversions, findings/searching
#case conversions --> upper(), lower(),title(),captalize()
name= "nani harshu"
a=name.upper() #converts complete string into capital
print(a)
b=a.lower() #converts complete string into smaller letters
print(b)
c=name.capitalize() # only 1st letter of string into capital
print(c) #Nani harshu
d=name.title() #converts every 1st letter of string to capital
print(d)  #Nani Harshu
'''

































