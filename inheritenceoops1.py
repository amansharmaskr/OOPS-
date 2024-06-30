class Car():
    def __init__(self, name, origin):
        self.name=name
        self.origin=origin
    
    def drive(self):
        return (f"name is {self.name} and origin is {self.origin} ok" )
        

c1=Car("mercedes", "usa") 
print(c1.drive())
print(c1.name)        

#ok till now, now make a derived (child) clss out of base (parent) class


class BMW (Car):
    def __init__(self,name,origin,newattribute):     # ALL ATTRIBUTES TO BE INSERT WHETHER OLD OR NEW
        super().__init__(name, origin)                  #ATTRIBUTES WHICH WE ARE IMPORTING
        self.newattribute=newattribute
    
    def activitybychild(self):
        return f"this car is {self.name} and origin is {self.origin} and new feature is {self.newattribute}"
        

bmwobject = BMW("GX", "GERMANY", "6 AIR BAGS")
print(bmwobject.activitybychild())

#if have 2 or more parents let say two
#just write those two in there normal way
#while writing child or derived just follow upper concepts + 
# #ATTRIBUTES WHICH WE ARE IMPORTING from both PARENT1.__init__(WHAT TO IMPORT FROM 1) +
#  AGAIN IN NEXT LINE  PARENT2.__init__(WHAT TO IMPORT FROM 2)
#AND PROCEED 

