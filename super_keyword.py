#constructors woith arg in both parent and child class
'''
class Father:
    """ usage of parent and child constructor"""
    def __init__(self,property):
        self.property=property
    def father_property(self):
        print("father property is ",self.property)
class Kid(Father):
    pass
    def __init__(self,earned,property):
        self.earned=earned    
        super().__init__(property)  #passing values to father class constructor in child constructor
    def kid_property(self):
        print("kid property is ",self.earned)
        print("final prooperty",self.earned+self.property)
#obj=Kid()
#obj.father_property()
girl=Kid(250000,100000)
girl.father_property()
girl.kid_property()

#what if the child class is having same method as of the parent class
#parentclass method --> override by child class method
#area of rectangle and square
class Square:
    def __init__(self,z):
        self.z=z
    def area(self):
        print(f"area of square {self.z**2}")
class Rectangle(Square):
    """method overriding"""
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        super().__init__(z)
    def area(self):
        super().area()
        print(f"area of rectangle {self.x*self.y}")

r=Rectangle(4,2,6)
r.area()
print(r.z)

#Hierarchial inheriance --> single parent multiple parents
class Atm:
    def transaction(self):
        print("you can start transaction through ur contacts")
class Credited(Atm):
    def send_from(self):
        print("money send from user1")
class Debited(Atm):
    def send_to(self):
        print("money send to amma ")
d=Debited()
d.transaction()
d.send_to()
c=Credited()
c.transaction()
c.send_from()
'''
#hybrid inheritance --> combination of 2 or more types of inheritance
class Spotify:
    def purpose(self):
        #print("listen to your fav music")
        return "hello"    #---> we can have multiple return for the function but always function rerturn the 1st return statement
        return "hi"

class Primimum(Spotify):
    def price(self):
        print("experience music without interuption")
class Account(Spotify):
    def details(self):
        print("user details are here")
class User(Account):
    def display(self,name):
        print(f"user name is {name}")
u1=User()
u1.display("harshu")
u1.details()
print(u1.purpose())    # op --> Hello
p=Primimum()
p.price()
print(p.purpose())