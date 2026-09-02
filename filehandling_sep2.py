'''
file handling in python : files are mainly used to nstore the data
---> it supprots read mode,write mode and append mode (using open() function)

import os

if os.path.exists('sample.txt'): #we can give complete path of the file if we dont be in the same folder 
    file=open('sample.txt','r')  #default read mode --even we dont mention 'r' if the file exist
    print("file loaded successfully") #we should be in same folder to execute this---> cd DA-023
else:
    print("file not found")

#now lets access the content from the file
file=open('sample.txt') #default mode is read
#print(file) # return wrapper file  --> if file don't exist then return FileNotFound error
#print(file.read())
#print(type(file.read()))  #return the type of content that file hold
#print(len(file.read()))
#a=file.read()
#print(a)
#print(len(a))
#readline(), readlines()
print(file)
#print(file.readline()) # reads the 1st line in the file and provide \n when we have more than 1 line in the file
print(file.readlines()) # reads all lines in file and provide content in the list

# 'w' mode --> it automatically creates a newe file if the file does not exist  ---> and overrides if the content if the file exist
file = open('data.txt','w')
print(file)
file.write("this file is created by the write mode and the file has no content")
file.write("good moring") # content will be appended at end of the file
file.close() #close() is mandatory when we open a file... we need to close it after operation

#we can use with keyword to avoid close()
with open ('data.txt','w') as f:
    f.write("good night...")  #content will be over rided

with open('data.txt','a') as g:
    g.write("have a sound sleep") # appeneded at the end of the file

# + --> read and write
with open('data.txt','r+') as h:
    #print(h.read())
    h.write("please stop") # 1st write and then next read ---> in that case the file content is over ridden by no of new characters
    print(h.read())
'''
#file operations like size and path
import os
#file=open('data.txt','r')
if os.path.exists("data.txt"):
    print("file size is",os.path.getsize("data.txt"),"Bytes")
    print("file absolute path",os.path.abspath("data.txt"))
else:
    print("file not found")    