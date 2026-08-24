'''
inheritance --> it is one of the key feature of OOP where we inherite the properties(attributes,methods) from one class to another class (base(Parent) class) -->derived class)(child class)
whatsapp --> personal user, business user,communities --> (all these class uses some common methods and attributes so then we can reuse some lines of code by inheriting )
featues--> code reuseablity, avoiding code duplication,code maintainability,polymorphism(method overriding, method over loading, operator over loading)

different types of inheritance
1.single -- single parent and single child
2.multiple -- multiple parents and child
3.multi level -- grand parent-->parent-->child 
4.hierarchial -- single parent-->multiple childs 
5hybrid -- it can carry 1 or more types of inheritance

syntax:
 #single inheritance
class BaseClass:
    statements..
    ......
class DerivedClass(BaseClass):
    statements..
    .......

#whatsapp scenario
class User:
    """ single inheritance usage"""
    def send_msg(self):
        print("sending message")
    def voice_call(self):
        print("user can make vioce call")
    def vedio_call(self):
        print("user can make vedio call")
class BussinessUser(User):
    #pass --> it has nothing to return but used to avoid indentation errors and syntax error
    def create_catalog(self):
        print("display product catalog")
u1=BussinessUser()
#print(dir(u1))
u1.send_msg()
u1.voice_call()
u1.vedio_call()
u1.create_catalog()

#what if the base class has a constructor
#social media login --> users --> update_users
class Users:
    company="Codegnan" #class attribute , its is same for every object and return before the constructor
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname+self.lname
#class Login(Users):
#   def full_name(self):
#        return self.fname+self.lname
class UpdateUser(Users):
    def update(self):
        return self.fname.title()+" "+self.lname.title().strip()

#u1=Login("harshu","veeragoni")
#print(u1.full_name())
u2=UpdateUser("nani"," veeragoni")   # we are passing values to parent class constructor through the child class obj creation
print(u2.update())
u3=Users("sweety","gande")
print(u3.company)
print(u3.full_name())
print(u3.fname)
print(u3.lname)
#print(u3.update()) # AttributeError --> as parent objct cannot access the methods of child

#what if child class has also a constructor
#father--kid (property)
class Father:
    """ usage of parent and child constructor"""
    def __init__(self):
        self.property=1000000
    def father_property(self):
        print("father property is ",self.property)
class Kid(Father):
    pass
    def __init__(self):
        self.earned=50000     #constructor overriding as both the parent and child constructor has same vatriable name so overrided
    def kid_property(self):
        print("kid property is ",self.earned)
#obj=Kid()
#obj.father_property()
girl=Kid()
girl.father_property()
girl.kid_property()
#in above example both parent and child have constructor so the constructor overriding is happening even the attributes are different , to avoid we use super()
#super().__init__()
#super().__init__(args)
#super().method() ---> method over riding
'''
class Father:
    """ usage of parent and child constructor"""
    def __init__(self):
        self.property=1000000
    def father_property(self):
        print("father property is ",self.property)
class Kid(Father):
    pass
    def __init__(self):
        super().__init__()  # it is used to avoid the constructor overiding when base and derived class both have constructor
        self.property=50000     
    def kid_property(self):
        print("kid property is ",self.property)
#obj=Kid()
#obj.father_property()
girl=Kid()
girl.father_property()
girl.kid_property()
