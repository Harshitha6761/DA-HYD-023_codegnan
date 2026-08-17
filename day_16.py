#dictionary --> collection of key value pairs which is used to store related data, mapping is done
'''
--> JSON,APIs,database records
--> dict() or data={} --> data={key:value}
--> indexing through key values
--> mutable,ordered,heterogeneous
--> keys should be unique -->int,string,float
'''
details={}
print(type(details))
details={'ids':'cgh6761',
         'name':'harshu',
         'gender':'female',
         'age':21,
         'batch':'DA23',
         'place':'HYD'}
print(details)
print(len(details))
'''
#details[0] -->key error
print(details.keys()) # return all the keys from the dictionary
print(details['ids']) # returns the value corresponding to ids key
print(details['ids'],details['name']) #returns both values corresponding to 2 keys
#print(details['marks'])# if the key is not present or key is wrongly entered then we get key error

#updating dictionary using keys
details['marks']=[] # marks key contains a list
print(details)

details['marks'].append(23)
print(details)

details['marks'].extend([45,36,47,78])
print(details)

details['practice']=('tuseday','thrusday','saturday')
print(details)
#accessing element
print(details['marks'][2])
print(details['practice'][1])
details['MI']=('monday','wednesday','friday')
print(details)

#operations --> mutable,indexing,membership
print('wednesday' in details) #false as we dont have 'wednesday' is not a key --> we cannot access the value directly
print('MI' in details) # true as we are accessing the key

###accessing keys
#keys() --> returns all keys from the dictionary
for i in details:
    print(i)

for i in details.keys():
    print(i)

###accessing values
#value() --> returns all values from the dictionary
for i in details.keys():
    print(details[i]) #all details

for i in details.values():
    print(i) # all details

###both key and values
for i in details.keys():
    print(f"key : {i}")
    print(f'value : {details[i]}')

#items() --> returns key-value pairs from the dictionary
for i in details.items():
    print(i)  # returns in the form of tuple--> (key,value)

for key,value in details.items(): #type error if () is not mention besides items   #value error if .items() is not mentioned
    print(key,value)   # returns in normal form


#update() --> add multiple items at a time
details.update({'marks':[],
               'ps':('tuseday','thrusday','saturday')})#{}  should be mandatory , so we need a dictionary to update a dictionary
print(details)
details['marks'].extend([23,45,67,89])
print(details)

m=map(int,input('enter the marks').split())
details['marks'].extend(m)
print(details)

#we can use eval() to take the values from the user into dictionary


#get() --> return the value if the key present else return nothing --> no error is raised
print(details.keys())
print(details.get('name'))
print(details.get('branch')) #returns none as we do not have brach as key

#setdefault() --> returns value if the key is present else the will be inserted into the dictionary --> setdefault() will not make any changes to existing keys but add key if not present and return none 
print(details.setdefault('age')) #returns value as key is present
print(details.setdefault('branch')) # returns none as branch is not a key
print(details.keys()) #branch is added to the keys by default
details['branch']='ds'
print(details)
print(details.setdefault('name','nani')) # no changes as name already exist and associated with some value

#pop(key) --> delete the specific key and all the asscociated values
print(details.pop('branch')) #error if key is not mentioned
print(details)

#popitem() --> removes or delete (key,value) from the last --> always delete last item
print(details.popitem())
print(details.popitem())

#del keyword
del details['ids']
print(details)
del details['marks'][2]
print(details)

#clear() --> delete comple dictionary
details.clear()
print(details)
'''
#fromkeys() --> creates a dictionary but values set to none
#converting list,tuples,sets,strings to dictionary
data=['saketh','sai','data']
new=dict.fromkeys(data) #create the dictionary by making the saketh,sai,data as keys and their values set to none
print(new)
#updating values to those dictionary key created from the fromkeys()
new['saketh']=23
print(new)

c=dict.fromkeys(['6761','ch543'],['code','gnan']) # here 1st arg is group of keys and 2nd arg is common values for all the keys
print(c)






























    
    
