#operator overloading ---> operators will behave in diff ways as per the objects defined by the user
# + (addition-nunbers)(merging - lists)(contactination - strings)
'''
print(3+4)
print('code'+'gnan')
print([12,34,89]+[45,67,9])
#print(3.__add__(4)) #invalid using of literals
a=3
b=5
print(a.__add__(b))    #__add__() is magic method
a=[34,56,78]
b=[34,57,90]
print(a.__add__(b))
print(a)
print(a.__len__())
print(a.__mul__(2))

#lets apply above scenario of hotstar watch history
class WatchHistory:
    def __init__(self,hours):
        self.hours=hours
varun=WatchHistory(100)
print(varun.hours)
akash=WatchHistory(120)
print(akash.hours)
#print(varun+akash) ---> unsupported operand --> we are trying to add 2 objects
print(varun.hours+akash.hours) # 220
#print(varun.__add__(akash)) --> obj has no attribute __add__
'''
#using magic method to add
class WatchHistory:
    def __init__(self,hours):
        self.hours=hours
    def __add__(self,other):  # here is the other refer to the other object
        #return self.hours.__add__(other.hours) -->works correctly
        return self.hours+other.hours
    def __str__(self):
        return f'watch history is {self.hours}'
varun=WatchHistory(100)
print(varun.hours)
print(varun.__str__())
print(varun)
akash=WatchHistory(120)
print(akash.hours)
print(varun.__add__(akash))  # op--> 220
#print(varun)    #op --> <__main__.WatchHistory object at 0xffffa7387fd0>
