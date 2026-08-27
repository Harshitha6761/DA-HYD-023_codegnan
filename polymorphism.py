'''
Polymorphism --> poly--many morphism--forms
--> it is one of the key feature of OOP
--> methods with same name can take different paramenters(arguments)
1. Method overloading -- compile time polymorphism
2. Method overriding -- run time
3. Operator overloading -- (symbols)(Dunder methods(magic methods) -- __add__, __str__)

HOtSTAR
free user -- movies with adds
primium user -- no adds, movies
vip user -- content quality,live, primium content

#MethodOverloading :

class Hotstar:
    def watch(self):
        print("user logged in .... opening home page")
    def watch(self,movie):
        print(f"user watching {movie}")
app=Hotstar()
#app.watch()  ##error as the watch() needs 1 positional arg , always takes the lastly mentioned method when the methods have same name
app.watch("vishwanatham and Sons")

#same method in diff forms--> 2 behaviours in 1 method (using default arguments)
class Hotstar:
    def watch(self,movie=None):
        if movie is None:
            print("user logged in and home page is loading")
        else:
            print(f"user watching {movie}")
app=Hotstar()
app.watch()      # here we have single method but we are using it with and without args, their behaviour is diff in both cases
app.watch("teach you a lesson")

#same method in diff forms--> 2 behaviours in 1 method (using variable length arguments)
class Hotstar:
    def watch(self,*args):
        #if not args: #checks whether list is empty or not return true if list is empty
        #if len(args)==0: #if list is empty 
        #   print("user logged in and home page is loading")
        #else:
            #print(args) #args is tuple
            for i in args:
                print(f"user watching {i}")
app=Hotstar()
app.watch()      
app.watch("teach you a lesson","hello")
'''
#method over loading with types of arguments usage
'''Hotstar --> one movie at a time
        ---> multiple movies at a time
        
# using type of arg and then the method behaviour is diff based upon the type of args
class Hotstar:
    def watch(self,content):
        if isinstance(content,str):    # meaning of this line is --> checking the type of the content 
            print(f"user watching {content}")
        elif isinstance(content,list):
            print(content)
            for m in content:
                print(f"user watching {m}")
app=Hotstar()
data=list(map(str,input("enter movies names").split()))
app.watch("hello")
app.watch(data)
#app.watch()  --> type error as no args passed to the method 

####Method Overriding --> in inheritance
#it happens when the child class have the same method as the parent class method then the overriding occurs
#super() and diff obj -- can solve the overriding problem

#same method in both classes but using diff obj to access that methods
class FreeUser:
    def watch(self):
        print("user logged in and homepage..........")
class PrimiumUser(FreeUser):
    def watch(self,movie):
        print(f"user watching {movie}")
mp=PrimiumUser()
mp.watch("Hello")
mf=FreeUser()
mf.watch()
'''
class FreeUser:
    def watch(self):
        print("user logged in and homepage..........")
class PrimiumUser(FreeUser):
    def watch(self,movie):
        super().watch()
        print(f"user watching {movie}")
mp=PrimiumUser()
mp.watch("Hello")