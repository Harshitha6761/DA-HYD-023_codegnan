#oop_21-08
'''
object oriented programming
class --> blueprint(templet) of a obj
object --> it is a real instance (physical thing) which utilises the class
--> oop is a machanism or a process  which revolves around creating objects
sit consists of 2 imp properties --> attribute(variables that carry data to the object)
                                --> methods (function defined inside a class, which carry the behaviour of the object)
features of oop --> modularity, scalability,
    encapsulation(biding the data (attributes) features to class)
    abstraction-(show only relevant information to the class
    inheritance -(acquiring the properties from super class
                -single inheritance
                -multi level inheritance
                -multiple inheritance

syntax:

class Class_Name:
    """doc string"""
    attributes (characteristics)
    ....
    def func(self): (behaviour)
        ..
        .....
    .......
obj=Class_Name()

#student class with basic details --> static data --same data for all obj
class Student:
    """understanding the usage of oop"""
    name="nani"
    ids="da4054"
    gender="female"
    email="nani@gmail.com"
    def display(self):
        print(f"student name is {self.name}")
        print(f"student id is {self.ids}")
        print(f"student mail is {self.email}")
u2=Student       # <class '__main__.Student'>
print(u2)
u1=Student()      # <__main__.Student object at 0x0000023924AED7F0> --> () is responsible for object creation at location
print(u1)
print(dir(u1))  #returns all available methods and attributes inside the class
u1.display()
u3=Student()
print(u3.name)

#class for multiple inputs --> multiple objects but only once input  --> same ip for diff obj
class Students:
    """understanding the usage of oop"""
    name=input("enter name")
    ids=input("enter the id")
    gender=input("enter the gender")
    email=input("enter email")
    def display(self):
        print(f"student name is {self.name}")
        print(f"student id is {self.ids}")
        print(f"student mail is {self.email}")
u1=Students()
u1.display()
u2=Students()
print(u1.__dict__) #empty dictionary
print(u2.__dict__) # empty dictionary as the input is taken only once


#multiple objects but multiple times taking inputs --> diff op for diff obj
class Students:
    """understanding the usage of oop"""
    def data(self,name,ids,gender,email):
        self.name=name #self is used to differentiate the values from current variable to arg
        self.ids=ids
        self.gender=gender
        self.email=email
    def display(self):
        print(f"student name is {self.name}")
        print(f"student id is {self.ids}")
        print(f"student mail is {self.email}")
u1=Students()
u1.data("nani",'da6761','male','nani@gmail')
u1.display()
u2=Students()
u2.data("harshu",'da854','female','harshu@gamil')
u2.display()
print(u1.__dict__) #create a dictionary with keys and values
'''

#create a class with car brand name,color,price --> display()
class Cars:
    def read(self,brand,name,color,price):
        self.brand=brand
        self.name=name
        self.color=color
        self.price=price
    def display(self):
        print(f"Car brand is {self.brand}-->name is {self.name}-->color is {self.color}-->price is {self.price}")
c1=Cars()
c1.read("bmw","sedan","black",650000)
c1.display()
print(c1.__dict__)
c2=Cars()
c2.read("Hyndai","Exter","red",700000)
c2.display()
























